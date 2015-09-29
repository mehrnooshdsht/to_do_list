from django import forms


class AddNewListForm(forms.Form):
    List_Name = forms.CharField(max_length=30)


class AddNewTaskForm(forms.Form):
    Task_Name = forms.CharField(max_length=30)


