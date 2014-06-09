# Create your views here.
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext
from frontapp.models import contacts
from frontapp.forms import contactForm
def home(request):
	return render_to_response('frontapp/index.html')
def contact(request):
        context = RequestContext(request)
        if request.POST:
		contactform= contactForm(data=request.POST)#fetch form with all the data
		if contactform.is_valid():
			contactform.save(commit=True)
			return HttpResponseRedirect('frontapp/contact')
		else:
			print contactform.errors
	else:
		contactform = contactForm()#fetch empty form 
		print contactform
	context_dict = {
		'contactform':contactform,
	}
	
	return render_to_response("frontapp/contact.html",context_dict,context)
