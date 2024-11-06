# example only, remember to adjust later
import schedule
import time

from utils.web_scraper import WebScraper
from utils.sms_handler import SMSHandler
from utils.scheduler import Scheduler

def main():
    # Initialize the components
    scraper = WebScraper()
    sms_handler = SMSHandler()
    scheduler = Scheduler()

    # Schedule the reservation task
    scheduler.schedule_task(scraper.reserve_court, time_of_day)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()