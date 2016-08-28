import argparse
import ipaddress
import requests
import time



class Userinterface():

    on = True
    logged_in_user = None

    def __init__(self, name, server):
        self.logged_in = True
        self.user = name
        self.server = server

    @classmethod
    def login(cls):
        action = input("Mi a neved?")
        if action == "X":
            cls.on = False
        else:
            cls.logged_in_user = action

    def run_app(self):
        while self.logged_in:
            print("Welcome at Tweetcool")
            print("Press 1 to check conenction")
            print("press 2 to post")
            print("press 3 to read tweets")
            print("Press X to exit")
            action = input("Choose an option: ")
            if action == 'x':
                self.logged_in = False
            if action == 'X':
                self.__class__.on = False
                self.logged_in = False
            if action == '1':
                response=requests.get(self.server+'/p')
                print(response)
            if action == '2':

                tweet = input("Say something!")
                content_to_send = {'poster': self.user, 'content': tweet}
                response = requests.post(self.server+'/tweet', json = content_to_send)
                if response.status_code == 200:
                    print("it works")
                else:
                    print("something wrong")
            if action == '3':
                response = requests.get(self.server+'/tweet')
                for tweet in response.json():
                    print(tweet['poster'] + ' > > > ' + tweet['content'] + '    ' + str(time.ctime(tweet['timestamp'])))
