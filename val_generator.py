# Title: BattleNet generator
#
# Description: Goes to battle net website an makes accounts
#
# Author: Mr_bond#2732


from playwright.sync_api import sync_playwright
from threading import Thread
import time
from webbrowser import get
from playwright.sync_api import Page, expect
import time
import string
from termcolor import colored
import json
import requests
import threading
import sys
import os
from time import sleep
from datetime import datetime
import random
import hashlib
from urllib import response
import colorama

colorama.init()


def create_account():
    with open('settings.json') as f:
        data = json.load(f)
        username = data[0]['Username']
        riot_id = data[0]['RiotID']
        email_domain = data[0]['Email Domain']
    f.close()

    def random_char(char_num):
        return "".join(random.choice(string.ascii_letters) for _ in range(char_num))

    def random_num(charnum1):
        return "".join(random.choice(string.digits) for _ in range(charnum1))

    first_name = [
    "Michael",
    "Christopher",
    "Jessica",
    "Matthew",
    "Ashley",
    "Jennifer",
    "Joshua",
    "Amanda",
    "Daniel",
    "David",
    "Robert",
    "John",
    "Joseph",
    "Andrew",
    "Ryan",
    "Brandon",
    "Jason",
    "Justin",
    "Sarah",
    "William",]

    last_name = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
        "Moore",
        "Taylor",
        "Anderson",
        "Thomas",
        "Jackson",
        "White",
        "Harris",
        "Martin",
        "Thompson",
        "Garcia",
        "Martinez",
        "Robinson",
        "Clark",
        "Rodriguez",
        "Lewis",
        "Lee",
        "Walker",
        "Hall",
        "Allen",
        "Young",
        "Hernandez",
    ]
    random1 = ["01", "02", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    random1 = random.choice(random1)
    random2 = random.randint(1, 29)
    random3 = random.randint(1970, 2002)
    first_name1 = random.choice(first_name).lower()
    last_name1 = random.choice(last_name).lower()
    email = first_name1 + last_name1 + random_num(5) + str(email_domain)
    username1 = username + random_num(5)
    password = random_char(7) + random_num(6)
    
    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 500, "height": 400},
        device_scale_factor=2,
    )
    page = context.new_page()
    browser.new_context(ignore_https_errors=True)
    page.set_default_timeout(90000000)
    time.sleep(1)
    page.goto("https://auth.riotgames.com/login#acr_values=urn%3Ariot%3Agold&client_id=accountodactyl-prod&redirect_uri=https%3A%2F%2Faccount.riotgames.com%2Foauth2%2Flog-in&response_type=code&scope=openid%20email%20profile%20riot%3A%2F%2Friot.atlas%2Faccounts.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Fpassword.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Femail.edit%20riot%3A%2F%2Friot.atlas%2Faccounts.auth%20riot%3A%2F%2Fthird_party.revoke%20riot%3A%2F%2Fthird_party.query%20riot%3A%2F%2Fforgetme%2Fnotify.write%20riot%3A%2F%2Friot.authenticator%2Fauth.code%20riot%3A%2F%2Frso%2Fmfa%2Fdevice.write&state=e6335447-8dd3-4112-bc75-ebb33c86ff8b&ui_locales=en")
    time.sleep(1)
    page.locator("//a[normalize-space()='Create Account']").click()
    time.sleep(1)
    page.locator("//input[@name='email']").type(email)
    print(f'Set email to: {email}')
    time.sleep(1)
    page.locator("//button[@title='Next']").click()
    time.sleep(1)
    page.locator("//input[@placeholder='MM']").type(random1)
    time.sleep(1)
    page.locator("//input[@placeholder='DD']").type(str(random2))
    time.sleep(1)
    page.locator("//input[@placeholder='YYYY']").type(str(random3))
    time.sleep(1)
    page.locator("//button[@title='Next']").click()
    time.sleep(1)
    page.locator("//input[@name='username']").type(username1)
    print(f'Set username to: {username1}')
    time.sleep(1)
    page.locator("//button[@title='Next']").click()
    time.sleep(1)
    page.locator("//input[@name='password']").type(password)
    time.sleep(1)
    page.locator("//input[@name='confirm_password']").type(password)
    print(f'Set password to: {password}')
    time.sleep(1)
    page.locator("//button[@title='Next']").click()
    time.sleep(2)
    page.locator("//input[@data-testid='riot-id__riotId']").type(riot_id)
    print(f'Set RIOT ID to: {riot_id}')
    time.sleep(2)
    tag = random_num(4)
    page.locator("//input[@data-testid='riot-id__tagline']").type(tag)
    time.sleep(2)
    page.locator("//div[normalize-space()='Save Changes']").click()
    time.sleep(2)
    time.sleep(1)
    data_list = (f'{email}:{username1}:{password}')
    with open("ValAccounts.txt", "a") as f:
        json.dump(data_list, f, indent=4)
        f.write("\n")
        f.close
    time.sleep(2)
    browser.close()


create_account()