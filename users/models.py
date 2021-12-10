from django.db import models
from django.utils import timezone

# Create your models here.
class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date', null = True)
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)
    
    def __srt__(self):
        return self.name
