import dbbuilder

import unittest   
import os
        
class Test_Dbbuilder(unittest.TestCase):
    def test_db_basic_creation(self):
        dbbuilder.destroy_database("test")
        dbbuilder.build_tables("test", "./tests/sqlfiles/BasicTable.sql")
        filedir = os.path.abspath(os.path.dirname(__file__)) + "\\..\\"
        self.assertEqual(os.path.isdir(filedir + 'db'), True, "db directory created")
        self.assertEqual(os.path.isdir(filedir + 'db\\test'), True, "db/test directory created")
        self.assertEqual(os.path.isfile(filedir + 'db\\test\\BasicTable.py'), True, "BasicTable model created")
        self.assertEqual(os.path.isfile(filedir + 'db\\test\\_BasicTable\\attribute.py'), True, "Attribute model created")
    
    def test_db_basic_destroy(self):
        dbbuilder.build_tables("test", "./tests/sqlfiles/BasicTable.sql")
        dbbuilder.destroy_database("test")
        filedir = os.path.abspath(os.path.dirname(__file__)) + "\\..\\"
        self.assertEqual(os.path.isfile(filedir + 'db\\test\\_BasicTable\\attribute.py'), False, "Attribute model is destroyed")
        self.assertEqual(os.path.isfile(filedir + 'db\\test\\BasicTable.py'), False, "BasicTable model is destroyed")
        self.assertEqual(os.path.isdir(filedir + 'db\\test'), False, "db/test directory is destoryed")


        

if __name__ == '__main__':
    unittest.main()