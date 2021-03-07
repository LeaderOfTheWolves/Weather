## Weather

You Can Get Weather Reports For Any Location With This Package.
This Package Work With openweathermap.org API.

## Instaliation

```python
git clone https://github.com/LeaderOfTheWolves/Weather
cd Weather
pip install -e .
```

## Usage

Import:
```python
import weather
```
Or
```python
from weather import Connect
```

Example:
```python
import weather

Connection = weather.Connect() 
# If You Have appid From openweathermap.com: 
# Connecton = weather.Connect(appid=YOUR_APPID)

Result = Connection.get(city='New York') # Get About New York Weather

print(Result) # Print Result
```

```python
main = Result.main
print(main)
print("temp:", main.temp)
```

Can Use Decorators:
```python
@Connection.on_weather()
def WeatherHandle(Result):
    print(Result)

Connection.get(city="New York")
```

syntax:
```python
Connect.get(city:str, country:str=None, lang:str=None)
```

If City Not Founded, You get weather.errors.NotFoundCityError error
