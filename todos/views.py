from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django_htmx.http import retarget


from todos.models import Todo
from todos.froms import TodoForm
# Create your views here
@login_required(login_url="/users/login/")
def todos(request):
  context = {'todos': Todo.objects.filter(user=request.user),'user':request.user}
  if request.htmx:
    # print("htmx??? ",request.htmx)
    return render(request,'todos/partials/todos-container.html',context)
   
  return render(request, 'todos/todos.html', context)

@login_required(login_url='/users/login')
@require_POST
def submit_todo(request):
  form = TodoForm(request.POST)
  print("Todo from form.is_valid::",form.is_valid())
  if form.is_valid():
    todo=form.save(commit=False)
    print("Todo from the form::",todo)
    todo.user= request.user
    print('usser',request.user)
    todo.save()
    # return html
    context={'todo': todo}
    return render(request, 'todos/todos.html#todoitem-partial',context)
    
@login_required(login_url='/users/login')
@require_POST
def completed_todo(request, pk):
  todo = get_object_or_404(Todo,pk=pk, user=request.user)
  todo.is_completed = True
  todo.save()
  context={'todo':todo}
  return render(request, 'todos/todos.html#todoitem-partial',context)
    

@login_required(login_url='/users/login')
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
  todo = get_object_or_404(Todo,pk=pk, user=request.user)
  todo.delete()
  
  response = HttpResponse(status=204)
  response['HX-Trigger'] = 'delete-trigger'
  return response   

@login_required(login_url='/users/login')
def update_todo(request, pk):
  todo = get_object_or_404(Todo, pk=pk, user=request.user)
  context= {
    'form': TodoForm(instance=todo),
    'todo': todo
  }
  return render(request, 'todos/partials/update-todo.html', context)

  
@login_required(login_url='/users/login')
def create_todo(request):
  if request.method=='POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      todo=form.save(commit=False)
      todo.user= request.user
      todo.save()
      context= {'message': "Todo was added successfully"}
      return render(request, 'todos/partials/todo-success.html',context)
    else:
      context ={'form': form}
      response = render(request, 'todos/partials/create-todo.html',context)
      return retarget(response, '#todos-block')
  context = {'form': TodoForm()}  
  return render(request, 'todos/partials/create-todo.html', context) 