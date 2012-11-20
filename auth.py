#not use built-in view function
from django.contrib import auth
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    username=request.POST.get("username",'')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("pro")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/"+str(user))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
