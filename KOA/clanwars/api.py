import requests
import json
from django.conf import settings

class ClanWars:
    auth_headers = {
        'x-api-user': settings.USER_ID,
        'x-api-key': settings.API_TOKEN
    }

    # Get status of the Habitica server. Does not require authentication
    def get_status(self):
        response = requests.get(settings.BASE_URL + '/status').json()
        return response

    # Get the authenticated user's profile without sensitive information
    def get_user(self):
        response = requests.get(settings.BASE_URL + '/user/anonymized', headers = self.auth_headers).json()
        return response