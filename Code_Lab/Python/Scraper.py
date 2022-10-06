#!/usr/bin/python3

import re
import sys
import pprint
import requests
import argparse

class Scraper:
    def __init__(self) -> None:
        self.ArgParser = argparse.ArgumentParser(description="A Darwinbox Org Structure scraper")
        self.ArgParser.add_argument('-u','--username',help="pass username")
        self.ArgParser.add_argument('-p','--username',help="pass password")
        self.Baseurl = "https://moschip.darwinbox.in"
        self.Loginurl = self.Baseurl+"/user/login"
        self.isdebug = False
        self.Args = self.ArgParser.parse_args(args=None if sys.argv[1:] else ['--help'])

    def login(self) -> None:
        self.usrn = self.Args.username 
        self.upas = self.Args.password
        self.session = requests.Session()
        self.start_resp = self.session.get(self.Loginurl)
        self.Match = re.search(r'<input type="hidden" value="(\w+)" name="pbqBeYWPUn" />', self.start_resp.text)
        if self.Match:
            self.Pbq = self.Match.group(1)
        self.payload = {"UserLogin[username]" : self.usrn,"UserLogin[password]" : self.upas, "pbqBeYWPUn" : self.Pbq, "UserLogin[redirectpage]" : "dashboard" }
        self.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" ,"accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "pragma": "no-cache", 
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1"}
        self.session.headers.update(self.headers)
        self.login_resp = self.session.post(self.Loginurl, data=self.payload)
        if self.isdebug:
            print("Login")        
            print(self.login_resp.status_code)
            print(self.login_resp.text)

    def Get_Data(self):
        self.org_data_resp = self.session.get(self.Baseurl+"/OrganisationalApi/getOrgStructure")
        if self.isdebug:
            print("Orgdata")
            print(self.org_data_resp.status_code)
            print(self.org_data_resp.text)

        self.Out = self.org_data_resp.json()

        self.Root_Dict = self.Out['data'][0]

        self.Post_Process(self.Root_Dict)
        self.Scraper_Bot(self.Root_Dict["id"])

    def Post_Process(self,Dict):
        self.Temp_Dict = Dict
        try:
            self.Temp_Dict['email'] = self.Temp_Dict['bottom_tabs']['email']
        except:
            pass
        try:
            self.Temp_Dict['designation_name'] = self.Temp_Dict['standard_fields']['designation_name']['value']
        except:
            pass
        try:
            self.Temp_Dict['department_name'] = self.Temp_Dict['standard_fields']['department_name']['value']
        except:
            pass
        try:
            self.Temp_Dict.pop('bottom_tabs')
        except:
            pass
        try:
            self.Temp_Dict.pop('standard_fields')
        except:
            pass
        try:
            self.Temp_Dict.pop('filter_data')
        except:
            pass
        try:
            self.Temp_Dict.pop('is_dotted_line')
        except:
            pass
        try:
            self.Temp_Dict.pop('parent_company_id')
        except:
            pass

        pprint.pprint(self.Temp_Dict)
        print('---------------------')

    def Scraper_Bot(self,Id):
        self.Scrape_Url = self.Baseurl+"/OrganisationalApi/getSubOrgStructure?employee_id=" + Id

        Scrape_Out = self.session.get(self.Scrape_Url)
        Items = Scrape_Out.json()

        for one in Items:
            self.Post_Process(one)
            if one["has_children"] == True:
                self.Scraper_Bot(one["id"])

    def logout(self):
        self.logout_resp = self.session.get(self.Baseurl+'/user/logout')
        if self.isdebug:
            print("Logout")        
            print(self.logout_resp.status_code)
            print(self.logout_resp.text)

Giri = Scraper()
Giri.login()
Giri.Get_Data()
Giri.logout()