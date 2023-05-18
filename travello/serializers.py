from rest_framework import serializers
from .models import FootballClub, Player

class DestinationSerializer(serializers.Serializer):

    # Id Required False karon API_response theke Data Create er somoy amra jokon is_validate call dibo jano tokon id Auto_generate hobe  .save() call dile
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    # img = serializers.ImageField(upload_to='pics')
    desc = serializers.CharField()
    price = serializers.IntegerField(default=0)
    is_club_in_city = serializers.BooleanField(default=False)


    # This Function is used for "De-Serialization"
    def create(self, validated_data):
        return FootballClub.objects.create(**validated_data)




class PlayerSerializer(serializers.Serializer):

    # Id Required False karon API_response theke Data Create er somoy amra jokon is_validate call dibo jano tokon id Auto_generate hobe  .save() call dile
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField()
    country = serializers.CharField()
    price = serializers.IntegerField(default=0)


    # This Function is used for "De-Serialization"
    def create(self, validated_data):
        return Player.objects.create(**validated_data)