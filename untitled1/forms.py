from django import forms
class Add_new_list_form(forms.Form):
    List_Name = forms.CharField(max_length=30)

class Add_new_task_form(forms.Form):
    Task_Name = forms.CharField(max_length=30)


