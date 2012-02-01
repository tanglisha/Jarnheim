from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if "POST" == request.method:
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/character/" % new_user.name)
        else:
            data, errors = {}, {}

        return render_to_response("/character/new", {
            'form': forms.FormWrapper(form, data, errors)})
