from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from panda.models import Contributer, Reviewer , Subject
from panda.forms import PostForm
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from panda.forms import ContributerForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, mail_admins
from django.contrib.auth.decorators import login_required



def index(request):
	return render_to_response("panda/index.html")
"""
#def bye(request):
	#return HttpResponse("<h2>gooooo gud bye..</h2>")

def blog(request):
	context = RequestContext(request)
	blogs = Blog.objects.all()
	
	context_dict = {
		'blogs': blogs,
	}
	
	return render_to_response("panda/blog.html",context_dict,context)
"""
def submit_post(request):
	""" Create a form to submit post.
	"""
	context = RequestContext(request)

	if request.POST:
		postform = PostForm(data=request.POST)  # creating a new instance for using it
		if postform.is_valid():
			postform.save(commit=True)
			return HttpResponseRedirect('/panda/blog')
		else:
			print postform.errors
	else:
		postform = PostForm()
		print postform
	
	context_dict = {
		'postform': postform,
	}
	return render_to_response("panda/submitpost.html", context_dict , context)

def userlogin(request):
    """Login form.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
		for group in user.groups.all():
			if group.name == 'contributor':
		                login(request, user)
                		return HttpResponseRedirect('/panda/user/upload/')
			if group.name == 'reviewer':
				login(request,user)
				return HttpResponseRedirect('/panda/user/review')
            else:
                # An inactive account was used - no logging in!
                messages.info(request, "Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Bad login!")
            return render_to_response('panda/login.html', context)
    else:
        return render_to_response('panda/login.html', context)


def upload(request):
        context = RequestContext(request)

    # Download APK and increment the count
    #if request.GET:
        #subject = get_object_or_404(Subject, id=request.GET['id'])
        # increment download count
        #project.increment_download_count()
        #return HttpResponseRedirect('/media/%s' % project.apk)
	
    ## **	uploads = Subject.objects.filter(contributor=request.user)
        uploads = Subject.objects.filter(contributor__user__username=request.user)
    	context_dict = {'uploads': uploads}
    	return render_to_response('upload.html', context_dict, context)
	

def review(request):
	return render_to_response("review.html")

def home(request):
	context = RequestContext(request)
	return render_to_response('panda/home.html',context)

def contributer_signup(request):

	"""Request for new contributer to signup"""
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':
	        print "we have a request to register"    
	        contributer_form = ContributerForm(request.POST,request.FILES)
	        if contributer_form.is_valid():
                	print "Forms are valid"

                        if 'picture' in request.FILES:
                		user = Contributer(picture=request.FILES['picture'])
	                user = Contributer(validation_docs=request.FILES['validation_docs'])
                        user = contributer_form.save(commit=False)
                        

                        user.set_password(user.password)
                        user.save()
                        
		
                        email_subject="New Contributer has registered"
	                email_message="""
New Contributer has registered.
	    	
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """ 
# + newContributer.validation_docs +

Waiting for your your approval"""
			send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com', ['pri.chundawat@gmail.com'],fail_silently=False)
			messages.success(request,"form successfully submitted. Waiting for activation  from admin.")
			return HttpResponseRedirect(reverse('panda.views.index'))
	        else:
			if contributer_form.errors:
				print contributer_form.errors
	else:
		contributer_form = ContributerForm()	
           
        context_dict = {'contributer_form': contributer_form, 'registered': registered}
        return render_to_response('panda/signup.html', context_dict, context)


@login_required
def user_logout(request):
    """Logout user.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')    
    
