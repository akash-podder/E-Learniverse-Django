from rest_framework.test import APITestCase
from travello.serializers import PlayerSerializer, FootballClubSerializer

class PlayerSerializerTestCase(APITestCase):
    def test_player_serializer_valid_data(self):
        data = {
            "name": "Sergio Ramos",
            "desc": "Real Madrid's one of the Finnest Footballer... And One of the Most Underrated Footballer in History",
            "country": "Spain",
            "price": 100
        }
        serializer = PlayerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_player_serializer_error_data(self):
        data = {
            "name": "Sergio Ramos",
            "desc": "Real Madrid's one of the Finnest Footballer... And One of the Most Underrated Footballer in History",
            "country": "Spain",
            "price": 6
        }
        serializer = PlayerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEquals(serializer.errors['non_field_errors'][0], "Too low price for a World Class Player")

class ClubSerializerTestCase(APITestCase):
    def test_player_serializer_valid_data(self):
        data = {
            "name": "Real Madrid",
            "desc": "Real Madrid's one of the Greatest Club in the World in History",
            "is_club_in_city": True,
            "price": 1000
        }
        serializer = FootballClubSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_club_serializer_error_data(self):
        data = {
            "name": "Real Madrid",
            "desc": "Real Madrid's one of the Greatest Club in the World in History",
            "is_club_in_city": True,
            "price": 212
        }
        serializer = FootballClubSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEquals(serializer.errors['non_field_errors'][0], "Football Club's Price is too low")