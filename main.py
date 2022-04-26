import datetime as dt
import smtplib
import pandas as pd
import os
import random

EMAIL = "example@gmail.com"  # TODO-Must change to make code functional
PASSWORD = "examplePassword"  # TODO- Must change to make code functional
person_email = "example@gmail.com"
text_body = "examplePassword"

now = dt.datetime.now()
date = now.day
month = now.month

birthdays = pd.read_csv("birthdays.csv", index_col=False)
name = ""
email = ""


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=person_email,
                            msg=f"Subject:Happy Birthday!!\n\n{text_body}")


def construct_email():
    global text_body
    list_of_templates = os.listdir("letter_templates/")
    chosen_template = random.choice(list_of_templates)
    with open(f"letter_templates/{chosen_template}", "r") as template_orig:
        text_body = template_orig.read().replace("[NAME]", name)


for index, row in birthdays.iterrows():
    if row.month == month and row.day == date:
        person_email = row.email
        name = row["name"]
        construct_email()
        send_email()
