from django.shortcuts import render, render_to_response
from forms import Add_new_list_form, Add_new_task_form
from models import List1, List2, List3
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect


def open1(request):
    list_all = List1.objects.all()
    context = RequestContext(request, {
        'tasklists': list_all,
    })
    if request.method == 'POST':
        form1 = Add_new_list_form(request.POST)
        if form1.is_valid():
            list_name = form1.cleaned_data['List_Name']
            lists = List1.objects.create(Name=list_name)
    else:
        form1 = Add_new_list_form()

    return render(request, 'index2.html', {'form1': form1}, context)


def open2(request, this_task_id, done, my_id):
    list_all2 = List2.objects.all().filter(list_name=my_id)
    #
    context = RequestContext(request, {
        'tasks_in_list': list_all2,
    })
    if request.method == 'POST':
        form2 = Add_new_task_form(request.POST)
        if form2.is_valid():
            task_name = form2.cleaned_data['Task_Name']
            tasks = List2.objects.create(Name=task_name, list_name=my_id)
    else:
        form2 = Add_new_task_form()
        if done == "0":
            List2.objects.filter(id=this_task_id).delete()
        elif done == "1":
            new_task_add=List2.objects.get(id=this_task_id)
            done_task = List3.objects.create(Name=new_task_add.Name)
            List2.objects.filter(id=this_task_id).delete()
    return render(request, 'index3.html', {'form2': form2,'this_task_id' :this_task_id ,'done':done, 'my_id': my_id }, context)
# 'this_task_name': None


def open3(request):
    list_all3 = List3.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'done_tasklists': list_all3,
    })
    return HttpResponse(template.render(context)
                        )
