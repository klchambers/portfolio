from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission, e.g., save to database, send email, etc.
            form.save()  # or whatever you want to do with the data
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


def projects(request):
    return render(request, 'home/projects.html')
