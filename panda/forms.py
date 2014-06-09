from django import forms
from models import Contributer , Reviewer
from django.contrib.auth.models import User
from panda.models import Contributer

class PostForm(forms.ModelForm):#form for login
	username = forms.CharField()
	password = forms.CharField()

	class Meta:
		model = Contributer
		fields = ['username','password']

class ContributerForm(forms.ModelForm):#form for contributor signup
	username = forms.CharField(label='Username',
       		widget = forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Username  to login*.'}), 
				help_text="", required =True,
					error_messages={'required':'Username is required.'})
	first_name = forms.CharField(
        	widget= forms.TextInput(
           		 attrs={'class': 'form-control',
                   		'placeholder': 'Contributer first name*.'}),
           				 help_text="", required=True,
       						 error_messages={'required':'First name is required.'})
	last_name = forms.CharField(
        	widget= forms.TextInput(
            		attrs={'class': 'form-control',
                   		'placeholder': 'Contributer last name*.'}),
       					 help_text="", required=True,
        					error_messages={'required':'Last name is required.'})

	email = forms.CharField(
        	widget= forms.TextInput(
            		attrs={'class': 'form-control',
                   		'placeholder': 'Contributer valid email*.'}),
           				 help_text="", required=True,
        					error_messages={'required':'Valid Email address is required.'})
	password = forms.CharField(
        	widget=forms.PasswordInput(
            		attrs={'class': 'form-control',
                   		'placeholder': 'Contributer password*.'}),
       					 help_text="", required=True,
       						 error_messages={'required':'Password is missing.'})
	picture = forms.ImageField(
        	label = 'Profile Picture',
        		help_text = 'Upload profile picture.',
        			required=False)
	contact  = forms.CharField(
        	widget= forms.TextInput(
            		attrs={'class': 'form-control',
                   		'placeholder': 'Contribter contact number.'}),
        				help_text="", required=True,
       						 error_messages={'required':'Last name is required.'})

	validation_docs = forms.FileField(
        	label = 'Validation file.',
        		widget = forms.FileInput(),
        			help_text = 'Upload validation file.',
        				required=True)
	class Meta:
        		model =  User
        		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'picture', 'contact', 'validation_docs')
	def clean_validtion_docs_file(self):
        		"""Limit doc_file upload size."""
        		if self.cleaned_data['validation_docs']:
            			validation_docs= self.cleaned_data['validation_docs']
                      		return validation_docs
			else:
				raise forms.ValidationError("Not a valid file!")
	def clean_picture_file(self):
        		"""Limit picture_file upload size."""
        		if self.cleaned_data['picture']:
            			picture= self.cleaned_data['picture']
                      		return picture
			else:
				raise forms.ValidationError("Not a valid profile picture!")		
            	
