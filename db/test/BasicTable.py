#############################################################################
###################### THIS IS AN AUTO GENERATED CLASS ######################
#############################################################################


import lib.sqlexecution as sqlexec
from db.test._BasicTable.attribute import Attribute

PrimaryID = Attribute(None)
Message = Attribute(None)

def put(PrimaryID = None, Message = None):
	new_attributes = list()
	new_values = list()
	if PrimaryID != None:
		new_attributes.append('PrimaryID')
		new_values.append(PrimaryID)
	if Message != None:
		new_attributes.append('Message')
		new_values.append(Message)
	sqlexec.insert_into_table('test', 'BasicTable', new_attributes, new_values, 'd:\GitRepos\easyquery')