import user_lib.logger as logger
import user_lib.general as general

from os import listdir, mkdir
from os.path import isfile, join, realpath, dirname, isdir

TYPES = ['integer', 'text', 'bit']
PREFIX_WORDS = ['CREATE', 'TABLE', 'IF', 'NOT', 'EXISTS']
TRIMED_CHARACTERS = [ ']', '[', '(', ')', ';', '\n' ]

MODEL_PATH = ''

AUTO_GEN_COMMENT = '''#############################################################################
###################### THIS IS AN AUTO GENERATED CLASS ######################
#############################################################################\n\n'''

def generate_model(database: str, file_name: str, location: str):
    attributes = {}
    name = ''
    MODEL_PATH = location + "/db/"
    
    with open(file_name) as reader:
        content = reader.read()
        prefix = content.split('(', 1)[0]
        data = content.split('(', 1)[1]
        prefix_words = prefix.split(' ')

        for p_word in prefix_words:
            if not p_word.upper() in PREFIX_WORDS and not p_word == '':
                name = p_word

        words = data.split(' ')

        for i, word in enumerate(words):
            if general.trim_characters(word.lower(), TRIMED_CHARACTERS) in TYPES:
                attributes.append(general.trim_characters(words[i-1], TRIMED_CHARACTERS))
            
    generate_class_file(name, attributes, database, location)
    generate_attribute_file(name, database, location)
    
def generate_attribute_file(name: str, database: str, location: str):
    MODEL_PATH = location + "/db/"
    if not isdir(MODEL_PATH + database + "/_" + name): mkdir(MODEL_PATH + database + "/_" + name )
    f = open(MODEL_PATH + database + "/_" + name + "/attribute.py", "w")
    
    f.write(AUTO_GEN_COMMENT)
    f.write("\nimport lib.sqlexecution as sqlexec\n")
    f.write("class Attribute:\n\tdef __init__(self, value):\n\t\tself.value = value")
    f.write("\n\n\tdef put(self, value): \n\t\tsqlexec.insert_into_table('" + database + "', '" + name  + "', str(self.__name__), value, '" + location + "')")
    
    f.close()
    
def generate_class_file(name: str, attributes : str, database: str, location: str):
    MODEL_PATH = location + "/db/"
    if not isdir(MODEL_PATH + database): mkdir(MODEL_PATH + database)
    f = open(MODEL_PATH + database + "/" + name + ".py", "w")

    f.write(AUTO_GEN_COMMENT)
    f.write("\nimport lib.sqlexecution as sqlexec\n")
    f.write("from db." + database + "._" + name + ".attribute import Attribute\n\n")

    for attribute in attributes:
        f.write(attribute + " = Attribute(None)\n")
    
    f.write("\n" + generate_put_method(name, attributes, database, location))
    f.close()

    logger.log("created class model " + name)
    
def generate_put_method(name: str, attributes: str, database: str, location: str):
    method = "def put("
    for attribute in attributes:
        method += attribute + " = None, "
    method = method[0:len(method)-2]
    method += "):"
    method += "\n\tnew_attributes = list()\n\tnew_values = list()"
    for attribute in attributes:
        method += "\n\tif " + attribute + " != None:"
        method += "\n\t\tnew_attributes.append('" + attribute + "')"
        method += "\n\t\tnew_values.append(" + attribute + ")"
    method += "\n\tsqlexec.insert_into_table('" + database + "', '" + name  + "', new_attributes, new_values, '" + location + "')"
    return method