from datetime import datetime

from django.db import models


# Create your models here.


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=datetime.now)
    reply_to = models.ForeignKey("Post",
                                 related_name="replies",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def __unicode__(self):
        return self.text
