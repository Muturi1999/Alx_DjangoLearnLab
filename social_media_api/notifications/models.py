# from django.db import models
# from django.contrib.auth import get_user_model
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType

# User = get_user_model()

# class Notification(models.Model):
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
#     actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor_notifications')
#     verb = models.CharField(max_length=255)  # Example: "liked your post"
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     target = GenericForeignKey('content_type', 'object_id')
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.actor} {self.verb} {self.target}"
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications_sent")
    verb = models.CharField(max_length=255)  # Describes the action (e.g., "liked your post")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("content_type", "object_id")  # Reference to any model
    timestamp = models.DateTimeField(auto_now_add=True)  # Ensure timestamp is included

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} at {self.timestamp}"
