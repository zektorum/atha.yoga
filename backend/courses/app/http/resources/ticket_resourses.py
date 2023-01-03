from rest_framework.serializers import ModelSerializer

from courses.app.http.resources.course_resources import CourseResource
from courses.models import Ticket


class TicketResource(ModelSerializer):
    course = CourseResource()

    class Meta:
        model = Ticket
        fields = [
            "course",
            "user",
            "amount",
        ]
