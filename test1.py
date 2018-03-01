#Given an assignment. Program it!
import subprocess

def getManPages(command):
    return subprocess.check_output("man {}".format(command), shell=True)

foobar=open("foobar.txt", "a")

'''text had to be made to a list of commands by
a="ls, rm, mkdir, rmdir, pwd, ln, chmod, umask, ping, cut, sort, which, grep, whereis, w, who, whoami, last, file, strings, top, ps, nice, nohup, kill, signal, more, less, ifconfig, arp, nslookup, cat, uname, history, netstat, ifconfig, dig, man, lsof, crontab, nc, uniq, id, groups, df, du, touch, ip"
b=a.split(", ")
'''
commands=['ls', 'rm', 'mkdir', 'rmdir', 'pwd', 'ln', 'chmod', 'umask', 'ping', 'cut', 'sort', 'which', 'grep', 'whereis', 'w', 'who', 'whoami', 'last', 'file', 'strings', 'top', 'ps', 'nice', 'nohup', 'kill', 'signal', 'more', 'less', 'ifconfig', 'arp', 'nslookup', 'cat', 'uname', 'history', 'netstat', 'ifconfig', 'dig', 'man', 'lsof', 'crontab', 'nc', 'uniq', 'id', 'groups', 'df', 'du', 'touch']
for command in commands:
    #get manual pages from standard output. @Return type: bytes
    manPage=getManPages(command)
    
    #change bytes to string
    manStr=manPage.decode("utf-8")

    #split string into list of lines
    linesList=manStr.split("\n")

    #starting index
    index=linesList.index("DESCRIPTION")

    #Build perfection by finding complete sentences and ending the description of the tool there.
    
    foobar.write(command + "\t--")
    for line in linesList[index +1:index+7]:
        foobar.write(line)
    foobar.write("\r\r")

foobar.close()
print("DONE")



    
