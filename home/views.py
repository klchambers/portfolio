from django.shortcuts import render, redirect
from .forms import ContactForm
from honeypot.decorators import check_honeypot
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
import logging


@check_honeypot(field_name=settings.HONEYPOT_FIELD_NAME)
def portfolio(request):
    # Handling contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)

            new_message.save()  # Save the message after assigning all the data

            # Set up email notification
            subject = f'Hi Kieran, {new_message.name} just sent you a message'
            message = (f'The following message has been received:\n'
                       f'\nName: {new_message.name}'
                       f'\nEmail: {new_message.email}'
                       f'\nDate: {new_message.date}'
                       f'\nMessage: "{new_message.message}"')

            try:
                send_mail(subject,
                          message,
                          settings.DEFAULT_FROM_EMAIL,
                          [settings.DEFAULT_TO_EMAIL])
            except Exception as e:
                logging.error(f'Error sending your message: {e}')
                raise

            messages.success(
                request,
                f"Thank you for your message! I'll email you back at {new_message.email}." # noqa
            )
            return redirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'home/home.html', {'form': form})
