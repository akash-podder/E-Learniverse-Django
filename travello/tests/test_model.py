import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from travello.models import Player, FootballClub

class MyPlayerModelTestCase(TestCase):
    image_path = '/home/akash/PSL_Projects/Demo/Django_Telusko_Travello_Website/media/pics/players/sergio_ramos.jpg'
    destroy_image_path = ''
    # Set up the test environment
    def setUp(self):
        # Create a test image file
        self.test_image = SimpleUploadedFile(
            name='sergio_ramos.jpg',
            content=open(self.image_path, 'rb').read(),
            content_type='image/jpeg'
        )

    # after all the Testcases are Run this Function will Run
    def tearDown(self):
        # Delete the test image file
        os.remove(self.destroy_image_path)

    def test_create_player(self):
        name = "Sergio Ramos",
        desc = "The Greatest Defender of All... Time",
        country = "Spain",
        price = 211

        player_model = Player.objects.create(
            name=name,
            img=self.test_image,
            desc=desc,
            country=country,
            price=price
        )
        # Perform the test
        self.assertEquals(player_model.name, name)
        self.assertEquals(player_model.desc, desc)
        self.assertEquals(player_model.country, country)
        self.assertEquals(player_model.price, price)

        self.assertTrue(player_model.img)  # Check if the image is saved successfully by assertions to validate the behavior of the model
        # to Destroy Image after all the Tests are Run
        self.destroy_image_path = player_model.img.path

class MyFootballClubModelTestCase(TestCase):
    image_path = '/home/akash/PSL_Projects/Demo/Django_Telusko_Travello_Website/media/pics/clubs/realmadrid.png'
    destroy_image_path = ''
    # Set up the test environment
    def setUp(self):
        # Create a test image file
        self.test_image = SimpleUploadedFile(
            name='realmadrid.png',
            content=open(self.image_path, 'rb').read(),
            content_type='image/jpeg'
        )

    # after all the Testcases are Run this Function will Run
    def tearDown(self):
        # Delete the test image file
        os.remove(self.destroy_image_path)

    def test_create_club(self):
        name = "Real Madrid"
        desc = "The Greatest Club in the World"
        price = 1000
        is_club_in_city = True

        club_model = FootballClub.objects.create(
            name=name,
            img=self.test_image,
            desc=desc,
            price=price,
            is_club_in_city=is_club_in_city
        )
        # Perform the test
        self.assertEquals(club_model.name, name)
        self.assertEquals(club_model.desc, desc)
        self.assertEquals(club_model.price, price)
        self.assertEquals(club_model.is_club_in_city, is_club_in_city)

        self.assertTrue(club_model.img)  # Check if the image is saved successfully by assertions to validate the behavior of the model
        # to Destroy Image after all the Tests are Run
        self.destroy_image_path = club_model.img.path