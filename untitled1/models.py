from django.db import models
from django.forms import ModelForm

class List1(models.Model):
    Name = models.CharField(max_length=30)
# new list
# class Add_new_list(ModelForm):
#     class Meta:
#         model = List1
#         fields = '__all__'

class List2(models.Model):
    list_name = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)

# new task
# class Add_new_task(ModelForm):
#     class Meta:
#         model = List2
#         # fields = ['Name']
#         fields = '__all__'

class List3(models.Model):
    Name = models.CharField(max_length=30)
# done tasks
