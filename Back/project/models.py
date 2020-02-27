from datetime import datetime

from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="项目名称")
    desc = models.CharField(default="", max_length=200, verbose_name="项目描述")
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name="最后修改时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
