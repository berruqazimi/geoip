from django.db import models

class SearchResult(models.Model):
    query = models.CharField(max_length=255)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
