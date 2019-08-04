#############################################################################
###################### THIS IS AN AUTO GENERATED CLASS ######################
#############################################################################


import lib.sqlexecution as sqlexec
class Attribute:
	def __init__(self, value):
		self.value = value

	def put(self, value): 
		sqlexec.insert_into_table('test', 'BasicTable', str(self.__name__), value, 'd:\GitRepos\easyquery')