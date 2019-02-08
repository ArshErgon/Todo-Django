
from django import forms

class TodoForm(forms.Form):
	add_todo_items = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter and hit enter'}))

