from django.db import models


class RequestModel(models.Model):
    full_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=13)
    comment = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'request'
        verbose_name_plural = 'requests'
