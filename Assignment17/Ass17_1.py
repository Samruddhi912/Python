import schedule
import time
import datetime
def Display():
    print("Jay Ganesh")
def main():
    print("Application Started:")
    print("Current time is:",datetime.datetime.now())
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
