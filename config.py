
import os


class Config:
    def __init__(self):
        self.API_KEY = os.environ.get('API_KEY')
        self.URL_SEARCH_RECIPE = 'https://api.spoonacular.com/recipes/complexSearch'
        self.URL_DETAIL_RECIPE = 'https://api.spoonacular.com/recipes/{id}/information'
        self.URL_GENERATE_MEAL_PLAN = 'https://api.spoonacular.com/mealplanner/generate'

        self.DB_PLATFORM = 'mysql+pymysql'
        self.DB_SERVER = 'localhost'
        self.DB_PORT = ''
        self.DB_USERNAME = 'root'
        self.DB_PASSWORD = ''
        self.DB_NAME = ''
        self.DB_URL = f'{self.DB_PLATFORM}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}'
