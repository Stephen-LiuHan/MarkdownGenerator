import datetime
import string
import os

#print("{},{}".format(__doc__,__file__))
currnt_file = __file__
#print("{}".format(currnt_file.rfind("\\")))
currnt_folder = os.path.dirname(os.path.abspath(currnt_file))
with open(os.path.join(currnt_folder,"template","BasicMinutes.md"),"rt",encoding="UTF-8") as tmp_file:
    ss=tmp_file.read()
with open("test.md",'w',encoding="UTF-8") as md:
    start = datetime.datetime.now()
    end = start+datetime.timedelta(hours=2) 
    md.write(ss.format(start=start.strftime("%Y %b %d (%a) %H:%M"),end=end.strftime("%H:%M")))