from twilio.rest import Client
from darksky import forecast
from django_CloudWatch.local_settings import account_sid, auth_token, Dark_Sky_Key
from datetime import date, timedelta
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")

def weather():
    latitude, longitude = get_lat_long('231 Gennessee St. San Francisco') 
    message = get_forecast((latitude, longitude))
    send_sms(message)


def get_lat_long(address):
    location = geolocator.geocode(address)
    print(location.address)
    print((location.latitude, location.longitude))
    return location.latitude, location.longitude

def get_forecast(location):
    weather = forecast(Dark_Sky_Key, location[0], location[1])
    return "Weekly Summary: {} \n Today's Wind Speed: {}".format(weather.daily.summary, weather.windSpeed)
    # print(weather.temperatureMax)
    # with forecast(Dark_Sky_Key, *PLACE) as place:
    #     weekly_summary = place.daily.summary
    #     print(weekly_summary)
    #     print(place.)
        # print("temp max: {}".format(place.daily.temperatureMax))

        # message = "Weekly Summary: {} \n Today's Summary: {} \n Temp Range: {} - {}".format(weekly_summary, day.summary, day.temperatureMin, day.temperatureMax)
    # return message

def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body = message,
                     from_='+12405585791',
                     to='+12403288453'
                 )
    print(message.sid)