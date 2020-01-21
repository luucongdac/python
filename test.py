import re

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
for i in range (len(result)):
    print(result[i])