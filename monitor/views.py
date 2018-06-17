from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from house.services import consumptionCommunity
from house.services import consumptionHouse
from house.models import House
from calendar import monthrange
import time
import json
import random

class HomePage(TemplateView):
  template_name="monitor/homepage.html"

def getRandInt(to):
  return random.randint(0,to)

def createRandomArray(numHouses):
  data = []
  for  i in range(1,numHouses+1):
    data.append({"name":"House{}".format(i), "y": random.randint(0,1500)})
  return data

class VCommunity(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/community.html"
  def get_username(self):
    return self.request.user.username
  def get_context_data(self,*args, **kwargs):
    year = int(time.strftime("%Y"))
    month = time.strftime("%m")
    day = time.strftime("%d")
    #Get last months data
    past_month = {}
    reference_date = "{}-{}-{}"
    for m in range(1, int(month)):
      ma = m
      if m <= 9: ma = "0{}".format(m)
      fdate = reference_date.format(year, ma, 1 )
      numdays_monthi = monthrange(year, m)[1]
      tdate = reference_date.format(year, ma, numdays_monthi)
      _, consume_monthi = consumptionCommunity(fdate, tdate)
      past_month[m] = consume_monthi
    #Get current month data
    fdate = reference_date.format(year, month, 1)
    tdate = reference_date.format(year, month, day)
    _, consumption_houses = consumptionCommunity(fdate, tdate) #Production
    #_, consumption_houses = consumptionCommunity() #debug
    username = self.get_username()
    houses = House.objects.filter(user__username=username)
    code_house = ""
    if len(houses)  != 0: code_house = houses[0].label
    consumption_houses = json.dumps(consumption_houses)
    past_month = json.dumps(past_month)
    ctx = {
      "consumption_houses": consumption_houses,
      "code_house": code_house,
      "past_month": past_month,
    }
    return ctx

class VWallet(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/wallet.html"

class VAssistant(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/assistant.html"

class VActions(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/actions.html"
  def percentage_a(self, value, greater_value ):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_b(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_c(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_d(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)
  def get_username(self):
    return self.request.user.username

  def get_context_data(self,*args, **kwargs):
    username = self.get_username()
    houses = House.objects.filter(user__username=username)
    code_house = ""
    if len(houses)  != 0: code_house = houses[0].label
    
    data = consumptionHouse(code_house)
    consumption_a = data["heating_cooling"]        #getRandInt(20000)#18800
    consumption_b = data["kitchen"] + data["plug"] #getRandInt(11500)#11500
    consumption_c = data["lighting"]               #getRandInt(4200)#4200
    consumption_d = data["water_boiler"]           #getRandInt(3000)#3000

    consumption_current_month = consumption_a + \
        consumption_b + +consumption_c + consumption_d
    bigConsume = 700 + 600 + 300 + 400

    p =  int ( consumption_current_month *100/ bigConsume )
    pa = self.percentage_a(consumption_a, 700)
    pb = self.percentage_b(consumption_b, 600)
    pc = self.percentage_c(consumption_c, 300)
    pd = self.percentage_d(consumption_d, 400)

    ctx = {
      "consumption": consumption_current_month,
      "consumption_a": consumption_a,
      "consumption_b": consumption_b,
      "consumption_c": consumption_c,
      "consumption_d": consumption_d,
      "p": p, 
      "pm": 100-p,
      "pa": pa,
      "pb": pb,
      "pc": pc,
      "pd": pd,
      "pam": 100 - pa,
      "pbm": 100 - pb,
      "pcm": 100 - pc,
      "pdm" : 100 - pd,
    }
    return ctx

class VMeter(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/meter_history.html"

class VLanding(TemplateView):
  template_name="monitor/landing.html"

class VCalendar(LoginRequiredMixin, TemplateView):
  login_url = 'account:login'
  template_name="monitor/calendar.html"

class VStatus(LoginRequiredMixin, TemplateView):
  template_name = "monitor/home.html"
  login_url = 'account:login'

  def percentage_a(self, value, greater_value ):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_b(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_c(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)
  def percentage_d(self, value, greater_value):
    stm = value * 100 / greater_value
    return int(stm)

  def get_username(self):
    return self.request.user.username

  def get_context_data(self,*args, **kwargs):
    year = int(time.strftime("%Y"))
    month = time.strftime("%m")
    day = time.strftime("%d")
    reference_date="{}-{}-{}"
    fdate = reference_date.format(year, month, 1)
    tdate = reference_date.format(year, month, day)
    data, _ = consumptionCommunity(fdate, tdate) #Production
    #data, _ = consumptionCommunity() #Debug
    consumption_a = data["heating_cooling"]        #getRandInt(20000)#18800
    consumption_b = data["kitchen"] + data["plug"] #getRandInt(11500)#11500
    consumption_c = data["lighting"]               #getRandInt(4200)#4200
    consumption_d = data["water_boiler"]           #getRandInt(3000)#3000
    consumption_current_month = consumption_a + \
        consumption_b + +consumption_c + consumption_d
    bigConsume = 35000

    p =  int ( consumption_current_month *100/ bigConsume )
    pa = self.percentage_a(consumption_a, 20000)
    pb = self.percentage_b(consumption_b, 10000)
    pc = self.percentage_c(consumption_c, 3000)
    pd = self.percentage_d(consumption_d, 7000)
    
    ctx = {
      "consumption": consumption_current_month,
      "consumption_a": consumption_a,
      "consumption_b": consumption_b,
      "consumption_c": consumption_c,
      "consumption_d": consumption_d,
      "p": p, 
      "pm": 100-p,
      "pa": pa,
      "pb": pb,
      "pc": pc,
      "pd": pd,
      "pam": 100 - pa,
      "pbm": 100 - pb,
      "pcm": 100 - pc,
      "pdm" : 100 - pd,
    }
    return ctx
