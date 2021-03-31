#!/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import argparse
import time
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='192.168.1.17', help='switch IP')
parser.add_argument('--port', default='2', help='port number')
parser.add_argument('--action', default='on', help='action on port, default on')

args = parser.parse_args()
url = 'http://' + args.host + '/login.cgi'

#Start Chrome
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#login
driver.find_element_by_xpath('//*[@id="password"]').send_keys("PASSWORD")

#login_btn
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
time.sleep(3)

#port_status
driver.find_element_by_xpath('//*[@id="blueLinkBold11"]/div[2]/a/span').click()

#switch to maincontent frame
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="maincontent"]'))

#port2
driver.find_element_by_xpath('//*[@id="tbl2"]/tbody/tr[4]/td[1]/input').click()
select = Select(driver.find_element_by_xpath('//*[@id="g_1_1"]/td[4]/select'))

if args.action == 'on':
  select.select_by_visible_text('Auto')
if args.action == 'off':
  select.select_by_visible_text('Disable')

#Apply
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="btn_Apply"]').click()
time.sleep(3)

#logout
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="logout"]').click()

#Close Chrome
driver.close()

#Kill chromedriver
subprocess.run(["pkill", "chromedriver"])

