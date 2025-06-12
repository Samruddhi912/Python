import schedule
import time

def Display1():
    print("LunchTime!")
def Display2():
    print("Wrap up work!")

def main():
    print("Application started:")
    schedule.every().day.at("13:00").do(Display1)
    schedule.every().day.at("18:00").do(Display2)
    while True:
        schedule.run_pending()
        time.sleep(43200)
if __name__=="__main__":
    main()