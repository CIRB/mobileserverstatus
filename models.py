from django.db import models

class Message(models.Model):
    status  = models.CharField(max_length=25)
    version = models.IntegerField()

    def __unicode__(self):
        return "%s - %s" %(self.version, self.status)
