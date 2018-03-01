#Given an assignment. Program it!
import subprocess

def getManPages(command):
    return subprocess.check_output("man {}".format(command), shell=True)

foobar=open("foobar.txt", "a")
commands=["arp", "ls", "rm"]
for command in commands:
    #get manual pages from standard output. @Return type: bytes
    manPage=getManPages(command)
    
    #change bytes to string
    manStr=manPage.decode("utf-8")

    #split string into list of lines
    linesList=manStr.split("\n")

    #starting index
    index=linesList.index("DESCRIPTION")
    foobar.write(command + "\t--")
    for line in linesList[index +1:index+7]:
        foobar.write(line)
    foobar.write("\r\r")

foobar.close()



    
