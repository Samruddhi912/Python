import schedule
import time
import datetime
def Display():
    print("DO CODING..!")
def main():
    print("Application has started")
    schedule.every(30).minutes.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(50)
if __name__=="__main__":
    main()