import schedule
import time
def Display():
    print("Namskar..")
def main():
    print("Application has started")
    schedule.every().day.at("9:00").do(Display)
    while True:
        schedule.run_pending()
        time.sleep(43200)
if __name__=="__main__":
    main()