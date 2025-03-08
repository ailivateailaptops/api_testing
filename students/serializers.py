from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        """Check for duplicate student details before saving"""
        student_exists = Student.objects.filter(
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade')
        ).exists()

        if student_exists:
            raise serializers.ValidationError("Student with the same details already exists.")

        return data

    def create(self, validated_data):
        """Ensure unique email handling manually"""
        if Student.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"email": "A student with this email already exists."})

        return super().create(validated_data)

    def to_internal_value(self, data):
        """Override this method to catch unknown fields"""
        for field in data.keys():
            if field not in self.fields:
                raise serializers.ValidationError({field: "This field is not valid."})
        return super().to_internal_value(data)
