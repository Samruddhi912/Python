import schedule
import time

def Updates():
    print("Checking mail...")

def main():
    print("Application started:")
    schedule.every(10).seconds.do(Updates)
    while True:
        schedule.run_pending()
        time.sleep(5)
        
if __name__=="__main__":
    main()