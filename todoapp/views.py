
from django.shortcuts import render, redirect
from .models import Todo, User, UserRegister
from .forms import TodoForm, UserSignForm
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User as users


def try_page(request):
	user_context = User.objects.all()
	todo = request.POST.get('todo')
	name = UserRegister.objects.filter(name=request.user.pk)
	print(name)
	print(dir(request.user))
	print(request.user.pk)
	print(request.user.username)
	print(dir(User))
	if request.method == "POST":
		User.objects.create(user_todo=todo)
		return redirect('/try/')
	return render(request, 'todo/try.html')

def home(request):
	#print(dir(request.user))
	todo_context = ""
	if request.user.is_superuser:
		print(request.user, 'Super user')
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

Users = get_user_model()
def sign_page(request):
	form = UserSignForm(request.POST or None)
	username = request.POST.get('name')
	email = request.POST.get('email')
	password = request.POST.get('password')

	if form.is_valid():
		context = {
					'form':form
					}
		UserRegister.objects.create(name=username, email=email, password=password)
		new_user = users.objects.create_user(username, email, password, is_staff=True)
		login(request, new_user)
		return redirect('/')

	return render(request, 'registration/sign.html', {'form':form})


def thank_you_page(request):
	return render(request, 'registration/thank.html')


def error_404(request, exception):
	data = {'name':'todo.herokuapp.com'}
	return render(request, 'error404/index.html', data)
