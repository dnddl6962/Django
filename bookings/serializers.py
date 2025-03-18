from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if value < now:
            raise serializers.ValidationError(
                "Check-in cannot be made on a date earlier than today."
            )
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if value < now:
            raise serializers.ValidationError(
                "Check-out cannot be made on a date earlier than today."
            )
        return value

    def validate(self, data):
        if data["check_out"] < data["check_in"]:
            raise serializers.ValidationError(
                "Check-out must be made on a date after the check-in date!"
            )
        if Booking.objects.filter(
            check_in__lte=data["check_out"], check_out__gte=data["check_in"]
        ).exists():
            raise serializers.ValidationError("we already have a reservation")

        return data


class PublicBookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
