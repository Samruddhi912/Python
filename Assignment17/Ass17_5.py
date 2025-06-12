import schedule
import time
import datetime
def DisplayTime():
    timestamp=time.ctime()
    obj=open("marvellous.txt","a")
    obj.write("Current time is:"+timestamp+"\n")
    data=obj.read()
    print(data)
    obj.close()

def main():
    print("Application has started")
    print("Current time is:",datetime.datetime.now())
    fobj=open("marvellous.txt","w")
    print("File is created!")
    schedule.every(2).minutes.do(DisplayTime)
    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()