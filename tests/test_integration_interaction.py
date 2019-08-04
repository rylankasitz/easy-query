import dbbuilder
import db.test.BasicTable as BasicTable

class Test_DBInteraction(unittest.TestCase):
    def test_put_row(self):
        BasicTable.put(Message="Test")
        self.assertEqual(1, 1, "test2")