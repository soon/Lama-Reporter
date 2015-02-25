# coding=utf-8
import logging

import pyowm

from plugins import LamaPlugin
from utils import safe_call_and_log_if_failed


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class WeatherPlugin(LamaPlugin):
    weather_names = ['погода', 'погоду', 'погодой', 'погоды']
    today = pyowm.timeutils.now()
    tomorrow = pyowm.timeutils.tomorrow()
    status_as_vk_smile = {
        "rain": '&#9748;',
        "sun": '&#128262;',
        "clouds": '&#9729;',
        "snow": '&#10052;'
    }

    pretty_status_names = {
        "rain": 'дождик',
        "sun": 'солнышко',
        "clouds": 'облачка',
        "fog": 'обалдеть какой туманище',
        "haze": 'туманчик',
        "mist": 'туманчик',
        "snow": 'снежок',
        "clear": 'без облачков'
    }

    def __init__(self, location):
        super(WeatherPlugin, self).__init__()
        self._location = None

        self.location = location

        self. time_names_and_functions = [
            (['сейчас'], self.post_weather_at_now_to_dialog),
            (['сегодня'], self.post_weather_at_today_to_dialog),
            (['завтра'], self.post_weather_at_tomorrow_to_dialog),
        ]

    @safe_call_and_log_if_failed
    def process_input(self, user_input, words, normalized_words, message):
        if any(weather in normalized_words for weather in self.weather_names):
            function = next((f for times, f in self.time_names_and_functions
                             if any(t in normalized_words for t in times)),
                            lambda x: logging.debug('No appropriate function'))
            function(message)

    def post_weather_at_now_to_dialog(self, message):
        logging.debug('Posting weather at now')
        self.post_weather_to_dialog(self.weather_from_observation, message)

    def post_weather_at_today_to_dialog(self, message):
        logging.debug('Posting weather at today')
        self.post_weather_to_dialog(self.get_weather_from_forecast_at(self.today), message)

    def post_weather_at_tomorrow_to_dialog(self, message):
        logging.debug('Posting weather at tomorrow')
        self.post_weather_to_dialog(self.get_weather_from_forecast_at(self.tomorrow), message)

    def get_weather_from_forecast_at(self, time):
        return self.forecast.get_weather_at(time)

    def post_weather_to_dialog(self, weather, message):
        self.bot.safe_post_message_with_forward_messages(self.format_weather(weather), [message])

    def format_weather(self, weather):
        without_wind = 'Погода: [{status}], температура: [{temperature}] °C, влажность {humidity}%'.format(
            status=self.get_status(weather), 
            temperature=self.get_temperature(weather),
            humidity=self.get_humidity(weather))
        wind_speed = self.get_wind_speed(weather)
        if wind_speed is not None:
            return without_wind + ', скорость ветра: {speed} м/с'.format(speed=wind_speed)
        else:
            return without_wind

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def weather_from_observation(self):
        return self.observation.get_weather()

    @property
    def observation(self):
        return self.owm.weather_at_place(self.location)

    @property
    def forecast(self):
        return self.owm.daily_forecast(self.location)

    @property
    def owm(self):
        return pyowm.OWM()

    @staticmethod
    def get_status(weather):
        status = weather.get_status()
        smile = WeatherPlugin.get_status_as_vk_smile(status)
        return WeatherPlugin.pretty_status_names.get(status, status) + smile

    @staticmethod
    def get_temperature(weather):
        temperature = weather.get_temperature('celsius')
        if 'temp' in temperature:
            return WeatherPlugin.normalize_temperature(temperature['temp'])
        else:
            return 'утречко: {}, денек: {}, ночка: {}'.format(
                *[WeatherPlugin.normalize_temperature(t) for t in (temperature['morn'],
                                                                   temperature['day'],
                                                                   temperature['night'])])

    @staticmethod
    def normalize_temperature(t):
        return int(round(float(t)))

    @staticmethod
    def get_status_as_vk_smile(status):
        return WeatherPlugin.status_as_vk_smile.get(status, '')

    @staticmethod
    def get_humidity(weather):
        return weather.get_humidity()

    @staticmethod
    def get_wind_speed(weather):
        return weather.get_wind().get('speed')
