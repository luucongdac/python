from selenium import webdriver 
from time import sleep 
import re
time_repeat = 10 #time
time_cycle = 10 #second
time_restart = 1 #second
def open_facebook():
    usr= 'luucongdac'
    pwd= 't6vwu2pd' 
  
    driver = webdriver.Chrome('D:/test_py/chromedriver')
    driver.get('https://www.facebook.com/stories/')
    #print ("Opened facebook") 
    sleep(1) 
  
    username_box = driver.find_element_by_id('email') 
    username_box.send_keys(usr) 
    #print ("Email Id entered") 
    sleep(1) 

    password_box = driver.find_element_by_id('pass') 
    password_box.send_keys(pwd) 
    #print ("Password entered") 

    login_box = driver.find_element_by_id('loginbutton') 
    login_box.click() 

    smile_1 = driver.find_element_by_id('UFIReactionsMenu/reaction_1') 
    smile_1.click() 

    sleep(time_cycle)
    content_newfeed = driver.page_source

    with open('data_base.txt', 'w') as f:
        f.write(str(content_newfeed.encode('utf-8')))

    #print ("Done") 
    #input('Press anything to quit') 
    driver.quit() 
    #print("Finished") 

#///////////////////////////////////////////////////////////////////////////////////
def reg_ex_data():
    regex = r"data-id=(\"\d*\")"

    file_log = open("D:/test_py/data_base.txt", "r")
    test_str = str(file_log.read())
    matches = re.finditer(regex, test_str, re.MULTILINE)
    result = ''
    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        for groupNum in range(0, len(match.groups())):
            result = result + str(match.groups())
            #groupNum = groupNum + 1
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    # Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
    def delete(string):
        a = string.replace('\'','')
        b = a.replace('\"','')
        c = b.replace('(','')
        d = c.replace(')','')
        return(d[0:-1])
    result = delete(result)
    result = result.split(',')
    return(result)

#main functin
log = open("D:/test_py/log.txt", "w+")

try:
    for i in range(time_repeat):
        open_facebook()
        raw_data = reg_ex_data()
        print(i)

        for i in range (len(raw_data)):
            log.write(raw_data[i] +'\n')
            print(raw_data[i])
        sleep(time_restart)
        log.write('------- \n')
finally:
    log.close()