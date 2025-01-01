from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for the Movie model.

    Fields:
        vote_average (DecimalField): The average vote for the movie, represented as a decimal with up to 4 digits and 2 decimal places.
        release_date (DateField): The release date of the movie.

    Meta:
        model (Movie): The model that is being serialized.
        fields (str): Specifies that all fields in the model should be included in the serialization.
    """
    vote_average = serializers.DecimalField(
        max_digits=4, decimal_places=2, coerce_to_string=False
    )
    release_date = serializers.DateField()

    class Meta:
        model = Movie
        fields = "__all__"
