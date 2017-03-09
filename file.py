import os
d = {"Python 2" : ".py", "PyPy 2" : ".py", "GNU C++" : ".cpp", "GNU C++11" : ".cpp", "GNU C++14" : ".cpp", "Java 8" : ".java"}

class file:
	path = '/home/codeforces'
	def __init__(self):
		if not os.path.exists(self.path):
			os.makedirs(self.path)
	def insert_file(self, code, file_name, file_type):
		if(file_type in d):
			file_path = self.path + '/' + file_name + d[file_type]
		else:
			file_path = self.path + '/' + file_name + '.txt'
		f = open(file_path, 'w')
		f.write(code.encode('utf8'))
		f.close()
 
if(__name__ == '__main__'):
	a = file()
		
		
		
