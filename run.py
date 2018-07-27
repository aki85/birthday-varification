import birthday
import sys

args = sys.argv
app = birthday.BirthdayVerification()

def error():
    print("err: bad argument")
    print("ex: python run 365 23")
    print("ex: python run 365 23 5")

try:
    days = int(args[1])
    attackCount = int(args[2])
    if(days > 0 and attackCount> 0):
        app.set(int(args[1]), int(args[2]))
        app.run()
        app.log(0)
    else:
        error()
except:
    error()

try:
    roop = int(args[3])
    if(roop > 0):
        for i in range(roop)[1:]:
            app.run()
            app.log(i)
except:
    pass