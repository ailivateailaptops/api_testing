from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Includes all fields in the API response

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        if value > 120:  # Setting a reasonable max age limit
            raise serializers.ValidationError("Age cannot be more than 120.")
        return value