import urllib.request as request
import urllib.error
from datetime import datetime
import weather.types as types
from weather.errors import NotFoundCityError
import json

class Connect:
    def __init__(self, appid: str = "5b149de8224b060a770d374ea44e7d63") -> None:
        self.appid = appid
        self.url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.func = []
    
    def on_weather(self, *args, **kwargs):
        
        def wrap(func):
            self.func.append(func)
        
        return wrap
    
    def get(self, city: str, country: str =None, lang: str=None):
        params = {
            'appid':self.appid,
            'q'    : city.replace(' ', '+'),
        }
        
        url = self.url
        
        if(country):
            params['q'] = params['q'] + ',' + country
        
        if(lang):
            params['lang'] = lang
        
        for k, v in params.items():
            url += "{}={}&".format(k, v)
        
        REQ = request.Request(url, method="GET")
        try: r = request.urlopen(REQ).read().decode()
        except urllib.error.HTTPError: raise NotFoundCityError("Not founded city") from None
        
        r = json.loads(r)
        
        
        r['weather'] = r['weather'][0]
        try:
            del r['cod']
            del r['weather']['id']
            del r['weather']['icon']
            del r['sys']['id']
            del r['sys']['type']
        except: pass
        
        sunrise, sunset = r['sys']['sunrise'], r['sys']['sunset']
        r['sys']['sunrise']= datetime.utcfromtimestamp(sunrise).strftime('%H:%M:%S (%Y-%m-%d)')
        r['sys']['sunset'] = datetime.utcfromtimestamp(sunset).strftime('%H:%M:%S (%Y-%m-%d)')
        result = types.Result(r)
        
        if(self.func != []):
            for func in self.func:
                func(result)
    
        else: return result
