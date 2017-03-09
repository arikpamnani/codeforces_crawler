import selenium
import sys
from file import file
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# do not allow selenium to display the browser
display = Display(visible = 0, size = (800, 600))
display.start()

# mkdir '/home/codeforces'
directory = file()

# load two separate instances of the webdriver
driver = webdriver.Chrome("/usr/bin/chromedriver")
seat = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("http://www.codeforces.com/enter")

# check for 'Codeforces' in title
try:
	assert "Codeforces" in driver.title
	print "assertion successful"
except:
	print "assertion failed"

# driver.get("chrome://settings/advanced")
# get username and password (optional)
username = sys.argv[1] 
passkey = "#"
# passkey = sys.argv[2]
handle = driver.find_element_by_name("handle")
password = driver.find_element_by_name("password")

# try to login (if password is provided)
try:
	handle.send_keys(username)
	password.send_keys(passkey)
	password.send_keys(Keys.RETURN)
	driver.implicitly_wait(10)	# 10 seconds
	# sub = driver.find_element_by_link_text("Submissions").click()
	# pagination = driver.find_element_by_class_name("pagination")
	number_of_pages = driver.find_elements_by_class_name("page-index")
	maxm = 1
	for i in number_of_pages:
		if(i.get_attribute("pageindex") > maxm):
			maxm = i.get_attribute("pageindex")	# number of solution pages (in pagination)
except:
	print ":("

total_submissions_ac = 0	# total AC submissions
k = 0
while(k < int(maxm)):
	try:
		# get to each submission page of the user
		driver.get("http://www.codeforces.com/submissions/" + username + "/page/" + str(k+1))
		driver.implicitly_wait(5)
		table = driver.find_element_by_class_name("status-frame-datatable")
		l = table.find_elements_by_tag_name("tr")

		# prints problems with verdict "OK"
		for i in range(1, len(l)):
			data = l[i].find_elements_by_tag_name("td")	# row of the table
			problem_name = data[3].find_element_by_tag_name("a")
			solution_lang = data[4].text
			status = data[5].find_element_by_tag_name("span")
			# solution_number = data[0].find_element_by_tag_name("a").get_attribute("submissionid")
			solution_url = data[0].find_element_by_tag_name("a").get_attribute("href")
			# print url
			if(status.get_attribute("submissionverdict") == "OK"):	
				total_submissions_ac += 1
				print problem_name.text
				# go to the solution url
				seat.get(solution_url)
				code = seat.find_element_by_xpath("//*[@id = 'pageContent']/div[3]/pre").text
				# driver.execute_script("window.history.go(-1)")
				directory.insert_file(code, str(problem_name.text), str(solution_lang))
		k += 1
	except:
		print ":("
		k += 1

print "You have " + str(total_submissions_ac) + " AC submissions."
driver.close()
seat.close()

