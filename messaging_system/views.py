from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Message, User
from .forms import UserForm, MessageForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def add_new_user(request):
    if request.method == "POST":
        print("post request")
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print("form is valid")
            data = user_form.cleaned_data
            User.objects.create_user(
                username=data['username'], password=data['password'],
                email=data['email'])
            new_user = User.objects.get(email=data['email'])
            new_user = authenticate(username=new_user.username,
                                    password=data['password'])
            data['password'] = '0000000000'  # clear the password field
            if new_user.is_authenticated:
                print("redirect to home page")
                login(request, new_user)
                return redirect('/')
            else:
                return redirect('login')
        else:
            print("form is not valid")
            return render(request, 'messaging_system/add_new_user.html', {'form': user_form})

    else:
        print("Get request")
        user_form = UserForm()
        return render(request, 'messaging_system/add_new_user.html', {'form': user_form})


@login_required
def home_page(request):
    messages = request.user.message_set.all()
    print("MESSAGES:")
    print(messages)
    return render(request, 'messaging_system/home_page.html', {'messages': messages})


@login_required
def get_messages(request):
    messages = request.user.message_set.all()
    return render(request, 'messaging_system/show_messages.html', {'messages': messages})


@login_required
def get_unread_messages(request):
    messages = request.user.message_set.filter(read_message=False)
    return render(request, 'messaging_system/show_messages.html',
                  {'messages': messages, 'show_unread_messages': True})


@login_required
def read_message(request, pk=None):
    message = get_object_or_404(Message, pk=pk)
    message.read_message = True
    message.save()
    return render(request, 'messaging_system/show_message.html', {'message': message})


@login_required
def create_new_message(request):
    user = request.user
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            print(message_form.cleaned_data)
            if User.objects.filter(email=message.receiver).exists():
                receiver_user = User.objects.get(email=message.receiver)
                message.sender = user.email
                message.user = user
                message.save()
                if message.receiver != message.sender:
                    # Create a new message object related to the receiver user
                    message.pk = None
                    message.user = receiver_user
                    message.save()

                return redirect('show_messages')
            else:
                error = "User '{}' is not exist".format(message.receiver)
                message_form = MessageForm()
                return render(request, 'messaging_system/write_message.html',
                              {'form': message_form, 'error': error})
    else:
        message_form = MessageForm()
        return render(request, 'messaging_system/write_message.html',
                      {'form': message_form})


@login_required
def delete_message(request, pk=None):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect('show_messages')

