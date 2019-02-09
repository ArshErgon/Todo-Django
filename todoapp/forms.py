
from django import forms

from django.contrib.auth import get_user_model

class TodoForm(forms.Form):
	add_todo_items = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter and hit enter'}))

User = get_user_model()
class UserSignForm(forms.Form):
	name = forms.CharField(
							widget=forms.TextInput(
													attrs={
															'class':'form-control',
															 'placeholder':'UserName'
															 }
													)
							)

	email = forms.CharField(
							widget=forms.EmailInput(
													attrs={
															'class':'form-control', 
															'placeholder':'example@gmail.com'
															}
													)
							)

	password = forms.CharField(
							widget=forms.PasswordInput(
													attrs={
															'class':'form-control'
															}
													)
							)
	password2 = forms.CharField(
							label="Confirm Password",
							 widget=forms.PasswordInput(attrs={"class":'form-control'
							 									}
							 							)
							   )

	def clean_name(self):
		username = self.cleaned_data.get('name')
		qs = User.objects.filter(username=username)
		if qs.exists():	
			raise forms.ValidationError('Name taken')
		return username


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password :
			raise forms.ValidationError('Password does not match')
		return data

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "gmail.com" in email:
			raise forms.ValidationError('Email must have gmail.com not %s'%(str(email[-9:])))
		return email