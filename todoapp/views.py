
from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm

def home(request):
	todo_context = Todo.objects.all()
	print(request.POST.get('add_todo_items'), 'home')
	form = TodoForm()
	if request.POST or None:
		Todo.objects.create(message=request.POST.get('add_todo_items'))
		return redirect('/')

	return render(request, 'todo/home.html', {'todo_context':todo_context, 'form':form})


def delete_todo(request, pk):
	delete_data = Todo.objects.get(id=pk).delete()
	return redirect('/')

def error_404(request, exception):
	data = {'name':'todo.herokuapp.com'}
	return render(request, 'error404/index.html', data)