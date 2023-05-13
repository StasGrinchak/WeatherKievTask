from celery import shared_task
from celery.utils.log import get_task_logger
from bs4 import BeautifulSoup
import requests
import lxml

from Weather.models import WeatherKiev, ParserSetting


logger = get_task_logger(__name__)


@shared_task
def parser():
    #change parser status in database
    status = ParserSetting.objects.first()
    status.status = 'in_progress'
    status.save()
    #headers and making a request to the site to get the markup
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    request = requests.get('https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/', headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    #search for elements on the markup
    block = soup.find('div', {'class': 'city__week-inner fl-c'}).find_all('div', {'class': 'city__day'})
    for info in block:
        date = info.find('span', {'class': 'date'}).text.replace('\n', '')
        temperature = info.find('div', {'class': 'city__day-temperature'}).find_all('span')
        try:
            #check for the existence of a record in the database and update
            instance = WeatherKiev.objects.get(date=date)
            instance.temperature_day = temperature[0].text
            instance.temperature_night = temperature[1].text
            instance.save()
        except WeatherKiev.DoesNotExist:
            #creating a new record in the database
            WeatherKiev.objects.create(date=date, temperature_day=temperature[0].text, temperature_night=temperature[1].text)
    status.status = 'done'
    status.save()
