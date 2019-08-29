from twilio.rest import Client
from darksky import forecast
from geopy.geocoders import Nominatim
from users.models import CustomUser
from twilio.rest import Client
from django_CloudWatch import settings

geolocator = Nominatim(user_agent="CloudWatch")
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_notification(notification):
    weather = get_weather(notification.user.address)
    body = 'Hi {0}. This is your CloudWatch notification.\n {1}'.format(
        notification.user.first_name,
        weather
    )

    client.messages.create(
        body=body,
        to=str(notification.user.phone_number),
        from_='+12405585791',
    )

def get_weather(address):
    location = geolocator.geocode(address)
    coordinates = (location.latitude, location.longitude)
    weather = forecast(settings.Dark_Sky_Key, coordinates[0], coordinates[1])
    return "Weekly Summary: {} \n Today's Wind Speed: {}".format(weather.daily.summary, weather.windSpeed) 

# def get_forecast(location):
    # print(weather.temperatureMax)
    # with forecast(Dark_Sky_Key, *PLACE) as place:
    #     weekly_summary = place.daily.summary
    #     print(weekly_summary)
    #     print(place.)
        # print("temp max: {}".format(place.daily.temperatureMax))

        # message = "Weekly Summary: {} \n Today's Summary: {} \n Temp Range: {} - {}".format(weekly_summary, day.summary, day.temperatureMin, day.temperatureMax)
    # return message


