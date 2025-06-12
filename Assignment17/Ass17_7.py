import schedule
import time
import datetime

def BackUp():
    obj=open("BackUp.log","a")
    timestamp=time.ctime()
    obj.write(timestamp+"\n")
    obj.close()

def main():
    print("Application has started:")
    fobj=open("BackUp.log","w")
    schedule.every(1).hour.do(BackUp)
    while True:
        schedule.run_pending()
        time.sleep(1800)


if __name__=="__main__":
    main()