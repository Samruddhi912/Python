import schedule
import time
import datetime
def DisplayTime():
    print("Current date and time:",datetime.datetime.now())
def main():
    print("Script Started")
    schedule.every(1).minute.do(DisplayTime)
    while True:
        schedule.run_pending()
        time.sleep(30)
if __name__=="__main__":
    main()