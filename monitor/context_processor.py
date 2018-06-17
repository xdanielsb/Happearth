from django.urls import reverse
import time 
def global_monitor(request):
  MODE_UI = "U2"
  day = time.strftime("%d")
  if(day[0]=='0'): day =day[1:] 
  ctx = {
    "MODE": MODE_UI,
    "day": day, 
    "month": time.strftime("%B"),
    "year": time.strftime("%Y"),
  }
  return ctx
