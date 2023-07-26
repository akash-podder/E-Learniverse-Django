import json

from rest_framework.test import APITestCase
from django.test import TestCase, Client
from travello.models import Player, FootballClub
from travello.serializers import PlayerSerializer, FootballClubSerializer
from django.urls import reverse
from django.test import TestCase, Client, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework import status
from django.contrib.auth import get_user_model
import pdb


class PlayerViewTestCase(TestCase):
    def setUp(self):
        # Create some Player objects for testing
        Player.objects.create(name='Player 1', desc='Description 1', country='Country 1', price=100)
        Player.objects.create(name='Player 2', desc='Description 2', country='Country 2', price=200)

    def test_get_all_players(self):
        # Create a test client
        client = Client()

        # Get the URL of the view using reverse
        url = reverse('api/players')

        # Send a GET request to the view
        response = client.get(url)

        response = client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Get the expected serialized data
        players = Player.objects.all()
        player_serialized = PlayerSerializer(players, many=True)
        expected_data = player_serialized.data

        # Check that the response data matches the expected data
        self.assertEqual(json.loads(response.content), expected_data)
        # TODO:for Unittest Debugging it will Print the LOGS we use "pdb" module
        # pdb.set_trace()

    @override_settings(MEDIA_ROOT='/tmp/')  # Set temporary media root for testing
    def test_upload_player_image(self):
        # Create a test client
        client = Client()

        # Create a player object with an uploaded image
        image_file = SimpleUploadedFile("Messi.jpeg", b"file_content", content_type="image/jpeg")
        player = Player.objects.create(name='Player with Image', desc='Description with Image', country='Country with Image', price=300, img=image_file)

        # Get the URL of the view using reverse
        url = reverse('api/players')

        # Send a GET request to the view
        response = client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the player name and image URL
        # self.assertContains(response, 'Player with Image')
        # self.assertContains(response, player.img.url)