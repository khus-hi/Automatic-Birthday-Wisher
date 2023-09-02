import datetime as dt
import smtplib
import pandas as pd
import random

my_email="teli.khushi@gmail.com"
password="isfxsgyrbhwolrjs"

today=dt.datetime.now()
today_tuple=(today.month,today.day)
data=pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'],data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday \n\n {contents}")




