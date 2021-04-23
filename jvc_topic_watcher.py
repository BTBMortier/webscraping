#!/usr/bin/env python3

import os
import sys
import time
import argparse
import requests
from pynput import keyboard
from pynput.keyboard import KeyCode
from bs4 import BeautifulSoup as bs


def get_page():
    url = "https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm"
    page = requests.get(url)
    soup = bs(page.content , 'html.parser')
    body = soup.body
    return body

def get_topics(body):
    div = body.contents[5]
    a   = div.contents[5]
    b   = a.ul
    topics = b.find_all("li",class_="")
    return topics

def get_topic_info(topics_obj):
    display = [] 
    for topic in topics_obj:
        if topic.img['src'] == "/img/forums/topic-marque-off.png":
            pass
        else:
            tinfos  = []
            topax   = topic.a['title']
            auteur  = topic.span.find_next("span",target="_blank").text.strip()
            nposts  = topic.span.find_next("span",class_="topic-count").text.strip()
            timest  = topic.span.find_next("span",class_="topic-date").text.strip()
            tinfos  = [topax,auteur,nposts,timest]
            display.append(tinfos)
    return display

def show_topics(display_arr):
    for i in  range(len(display_arr)):
        op      = display_arr[i][1]
        topic   = display_arr[i][0]
        nposts  = display_arr[i][2]
        t_time  = display_arr[i][3]
        print(f' "{topic}" par {op} à {t_time} : {nposts} post(s)')


def on_press(key):
    if key == KeyCode.from_char('q'):
        print("\n" * 100)
        print("\nBoucled")
        os._exit(1)
        

if __name__ == '__main__': 

    if len(sys.argv) > 1:
        r = int(sys.argv[1])
    else:
        r = 5
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        body    = get_page()
        topics  = get_topics(body)
        display = get_topic_info(topics)
        show_topics(display)
        time.sleep(r)
        print("\n" * 100)




 
