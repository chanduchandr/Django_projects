from django.db import models

class Common(models.Model):
    ActiveFlag = models.BooleanField(default=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=50, null=True, blank=True)
    UpdatedDate = models.DateTimeField(auto_now=True)
    UpdatedBy = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
