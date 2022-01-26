from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'phone', 'body',
                  'read', 'created_at', 'updated_at',)
        model = Appointment
