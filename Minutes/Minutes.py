import datetime
import string
import os

 #print("{},{}".format(__doc__,__file__))
currnt_file = __file__
#print("{}".format(currnt_file.rfind("\\")))
currnt_folder = os.path.dirname(os.path.abspath(currnt_file))
with open(os.path.join(currnt_folder,"template","BasicMinutes.md"),"r") as tmp_file:
    with open("test.md",'w') as md:
        now = datetime.datetime.minute
        ss=tmp_file.read()
        md.write(ss.format(now=now))