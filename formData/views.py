from django.shortcuts import render
from .models import FormData
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .email_validator import is_email_valid


@csrf_exempt
def form_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST['email']
        if is_email_valid(email):
            # saving data to the database model
            obj = FormData(
                email=email,
                name=name
            )
            obj.save()
            context = {
                'color': 'text-green-500 bg-green-100 border-green-400',
            }
            messages.success(request, 'Form Submitted successfully!')
            return render(request, 'form.html', context)
        else:
            context = {
                'color': 'text-red-500 bg-red-100 border-red-400',
            }
            messages.error(request, "Invalid Email! Enter a valid email address.")
            return render(request, 'form.html', context)
    return render(request, 'form.html')

