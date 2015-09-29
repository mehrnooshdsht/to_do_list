from django.db import models


class ListNames(models.Model):
    Name = models.CharField(max_length=30)
# list names

class AllTasks(models.Model):
    list_name = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
# all tasks for all lists

class DoneTasks(models.Model):
    Name = models.CharField(max_length=30)
# done tasks
