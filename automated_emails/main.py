import yagmail
import pandas as pd
import news_feed as news


if __name__ == "__main__":
    
    df = pd.read_excel('automated_emails/people.xlsx')
    
    for index, row in df.iterrows():
        news_feed = news.NewsFeed(interest=str(row['interest']),
                                  search_for=str(row['search_for']),
                                  from_date=str(row['from_date']),
                                  to_date=str(row['to_date']),
                                  language=str(row['language']),
                                  sortBy=str(row['sort_by']))
        email = yagmail.SMTP(user="pythoncourse16@gmail.com", password="passwordForEmail(app access)") # password for email
        email.send(to=row['email'],
                subject=f"Your {row['interest']} news",
                contents=f"Hello, {row['name']}! \n See what's on about {row['interest']} today. {news_feed.get()} \n\n You're welcome!",
                )