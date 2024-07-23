from django.db import models
from django.contrib.auth.models import User

class Translation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_direction = models.CharField(max_length=7)
    original_text = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Translation by {self.user.username}"
