from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

class IndiaTrackerView(TemplateView):
    templatename="tracker.html"

    def get(self,request):
        r1= requests.get('https://api.covid19india.org/data.json')
        all_state=r1.json()['statewise']
        total_state=all_state[0]
        statewise=all_state[1:]
        
        return render(request,self.templatename,{'statewise':statewise,'total_state':total_state})

    def post(self,request):
        r1= requests.get('https://api.covid19india.org/data.json')
        all_state=r1.json()['statewise']
        total_state=all_state[0]
        statewise=all_state[1:]

        state=request.POST['state']
        r2= requests.get('	https://api.covid19india.org/state_district_wise.json')
        try:
            all_city=r2.json()[state]['districtData']
        except:
            all_city=[]
        
        citywise=[]
        total_city=0
        for city in all_city:
            dict_=dict()
            dict_['city']=city
            dict_['confirmed']=all_city[city]['confirmed']
            total_city+=dict_['confirmed']
            citywise.append(dict_)
          
        return render(request,self.templatename,{'statewise':statewise,'citywise':citywise,'total_city':total_city,'total_state':total_state,'State':state})

class DonateView(TemplateView):
    templatename='donate.html'

    def get(self,request):
        return render(request,self.templatename)

class LatestCaseView(TemplateView):
    templatename='latestcase.html'

    def get(self,request):
        r1= requests.get('https://api.covid19india.org/raw_data.json')
        all_cases=r1.json()['raw_data'][::-1][1:]
                       
        return render(request,self.templatename,{'all_cases':all_cases})

class Essentials_ResourcesView(TemplateView):
    templatename='essentialsresources.html'

    def get(self,request):
        r1= requests.get('https://api.covid19india.org/resources/resources.json')
        all_cases=r1.json()['resources']
               
        return render(request,self.templatename,{'all_cases':all_cases})

class DeathView(TemplateView):
    templatename='deaths.html'

    def get(self,request):
        r1= requests.get('https://api.covid19india.org/deaths_recoveries.json')
        all_cases=r1.json()['deaths_recoveries']
              
        return render(request,self.templatename,{'all_cases':all_cases})

class HelpView(TemplateView):
    templatename='help.html'

    def get(self,request):
        return render(request,self.templatename,)


