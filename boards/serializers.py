from rest_framework import serializers

from boards.models import Dashboard, DashboardArchive, Column, Marks, Card, Task, SubTasks
from users.models import CustomUser


class DashboardSerializer(serializers.ModelSerializer):
    owner_id = serializers.UUIDField(source='owner.id', read_only=True)

    class Meta:
        model = Dashboard
        fields = '__all__'
        # model = Dashboard
        # fields = ['id', 'owner', 'title', 'description', 'is_private', 'is_favourite', 'users_can_edit',
        #           'users_can_view', 'users_can_comment']

    def create(self, validated_data):
        owner_id = validated_data.pop('owner')
        participants_data = validated_data.pop('participants', [])

        try:
            owner = CustomUser.objects.get(id=owner_id.id)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Owner with the provided ID does not exist.")

        dashboard = Dashboard.objects.create(owner=owner, **validated_data)

        # dashboard.participants.add(owner)

        # for participant_data in participants_data:
        #     participant = CustomUser.objects.create(**participant_data)
        #     dashboard.participants.add(participant)

        dashboard.save()
        return dashboard


class DashboardArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardArchive
        fields = ['id', 'cards_archived_id']


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'dashboard', 'title', 'position']


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['id', 'font_color', 'color', 'mark_text']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'column', 'position', 'info', 'description', 'status', 'priority', 'card_marks', 'deadline',
                  'is_notifications', 'is_archived', 'color']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'success_amount', 'total_amount']


class SubTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTasks
        fields = ['id', 'status', 'deadline']
