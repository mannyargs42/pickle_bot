from utils.web_scraper import WebScraper
from utils.date_calculator import format_date

def main():
    """
    Executes functions from utils:
    *url: for pickleball rec.us website
    *email and password: for rec.us
    *days_ahead: should be days from today that the website will open slots.
    *optimal_time: ideal time to book in the form XX:XX XM
    *participant: account owner who is booking, as it shows up on website
    
    Formats date and time to match buttons on the website and clicks through all
    the steps necessary to book a reservation. At the verification code step, the
    app will prompt the user to input the verification code quickly to finish the
    reservation. It automatically books the longest amount of time (up to 90 min)
    for the time slot selected.
    """

    url = ""
    email = ""
    rec_password = ""
    days_ahead = X
    optimal_time = ""
    participant = ""

    formatted_days_ahead = format_date(days_ahead)
    scraper = WebScraper()
    scraper.navigator(url)
    scraper.login(email, rec_password)
    scraper.choose_date(formatted_days_ahead)
    scraper.choose_time(optimal_time, participant)
    vcode = input("Enter verification quickly!: ")
    scraper.book_with_code(vcode)
    

if __name__ == "__main__":
    main()