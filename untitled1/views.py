from django.shortcuts import render
from forms import AddNewListForm, AddNewTaskForm
from models import ListNames, AllTasks, DoneTasks
from django.template import loader, RequestContext
from django.http import HttpResponse


def open1(request):
    list_all = ListNames.objects.all()
    context = RequestContext(request, {
        'task_lists': list_all,
    })
    if request.method == 'POST':
        form1 = AddNewListForm(request.POST)
        if form1.is_valid():
            list_name = form1.cleaned_data['List_Name']
            lists = ListNames.objects.create(Name=list_name)
    else:
        form1 = AddNewListForm()

    return render(request, 'index2.html', {'form1': form1}, context)


def open2(request, this_task_id, done, my_id):
    list_all2 = AllTasks.objects.all().filter(list_name=my_id)
    list_all = ListNames.objects.all().filter(id=my_id)
    context = RequestContext(request, {
        'tasks_in_list': list_all2,
        'this_list': list_all,
    })
    if request.method == 'POST':
        form2 = AddNewTaskForm(request.POST)
        if form2.is_valid():
            task_name = form2.cleaned_data['Task_Name']
            tasks = AllTasks.objects.create(Name=task_name, list_name=my_id)
    else:
        form2 = AddNewTaskForm()
        if done == "0":
            AllTasks.objects.filter(id=this_task_id).delete()
        elif done == "1":
            new_task_add = AllTasks.objects.get(id=this_task_id)
            done_task = DoneTasks.objects.create(Name=new_task_add.Name)
            AllTasks.objects.filter(id=this_task_id).delete()
    return render(request, 'index3.html', {'form2': form2, 'this_task_id': this_task_id, 'done': done, 'my_id': my_id},
                  context)


def open3(request):
    list_all3 = DoneTasks.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'done_task_lists': list_all3,
    })
    return HttpResponse(template.render(context)
                        )
