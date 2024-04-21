


from datetime import datetime
import pandas
import random
import smtplib
import os

#env in bash to see all environment variables
#saved the email key in environment in pythonanywhere
#export ABHIMAIL=""   -- syntax in bash
MY_EMAIL = os.environ.get("ABHIMAIL")
#saved the app key in environment in pythonanywhere
#export APPKEY="" --syntax in bash
MY_PASSWORD = os.environ.get("APPKEY")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents} "
        )
