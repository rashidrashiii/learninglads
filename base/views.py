from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView

from .models import Room, Topic, Message, User, Report, ReadReport
from .forms import RoomForm, UserForm, MyUserCreationForm, ReportForm

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        use = request.POST.get('username').lower()
        password = request.POST.get('password')

        # try:
        #     user = User.objects.get(username=use)
        # except:
        #     messages.error(request, 'User does not exist')

        user = authenticate(request, username=use, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q))[0:3]

    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)




@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

@login_required(login_url='login')
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

@login_required(login_url='login')
def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})

@login_required(login_url='login')
def privacy(request):
    return render(request, 'base/privacy_policy.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')

@login_required(login_url='login')
def terms(request):
    return render(request, 'base/terms_of_service.html')


@login_required(login_url='login')
def reportPage(request):
    form = ReportForm()
    if request.method == 'POST':
        # if 'screenshot' in request.FILES:
        #     screenshot = request.FILES['screenshot']
        Report.objects.create(
            user=request.user,
            subject=request.POST.get('subject'),
            username=request.POST.get('username'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            screenshot=request.FILES.get('screenshot')

        )
    context = {'form': form, }
    return render(request,'base/admin_report.html',context)

# @login_required(login_url='login')
# def reportform(request):
#     form = ReportForm()
#     if request.method == 'POST':
#
#         Report.objects.create(
#             user=request.user,
#             subject=request.POST.get('subject'),
#             username=request.POST.get('username'),
#             name=request.POST.get('name'),
#             description=request.POST.get('description'),
#             screenshot=request.POST.get('screenshot'),
#         )
#         return redirect('home')
#
#     context = {'form': form,}
#     return render(request,'base/admin_report.html',context)

@staff_member_required(login_url='login')
def adminDashboard(request):
    room_messages = Message.objects.all()
    count = User.objects.all().count()
    room_count = Room.objects.all().count()
    message_count = Message.objects.all().count()
    staff = User.objects.filter(is_staff=True)
    staffcount = User.objects.filter(is_staff=True).count()
    reports = Report.objects.all()
    reportscount = Report.objects.all().count()

    context = {
        'report': reports,
        'messagecount': message_count,
        'staff': staff,
        'staffcount': staffcount,
        'room_messages': room_messages,
        'user_count': count,
        'room_count': room_count,
        'reportscount': reportscount
    }

    return render(request,'base/admin.html', context)


@staff_member_required(login_url='login')
def adminMenu(request):
    reportcount = Report.objects.all().count()
    return render(request, 'base/admin-menu.html',{'reportcount':reportcount})

@staff_member_required(login_url='login')
def usersList(request):
    users = User.objects.all().order_by('-created_on')
    count = User.objects.all().count()
    room_messages = Message.objects.all()
    reportscount = Report.objects.all().count()
    context = {
        'room_messages': room_messages,
        'userprofile':users,
        'usercount':count,
        'reportscount': reportscount
    }
    return render(request, 'base/admin.html',context)




# class SearchResultsView(ListView):
#     model = User
#     template_name = 'base/admin.html'
#     queryset = User.objects.filter(name__icontains='Rashid')

@staff_member_required(login_url='login')
def userSearch(request):
    name = request.GET.get('q')
    users = User.objects.filter(username__icontains=name).order_by('-created_on')
    room_messages = Message.objects.all()
    context = {
        'room_messages': room_messages,
        'userprofile': users
    }
    return render(request, 'base/admin.html', context)

@staff_member_required(login_url='login')
def deleteUser(request, pk):
    try:
        record = User.objects.get(id=pk)
        record.delete()
        print("User deleted successfully!")
    except:
        print("User doesn't exists")
    return redirect('users')

@staff_member_required(login_url='login')
def deleteRooms(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return redirect('home')

@staff_member_required(login_url='login')
def reportsPage(request):
    reports = Report.objects.all().order_by('-created')
    count = Report.objects.all().count()
    room_messages = Message.objects.all()
    reportscount = Report.objects.all().count()
    readreport = ReadReport.objects.all().order_by('-created')
    context = {
        'reports': reports,
        'reportcount': count,
        'room_messages': room_messages,
        'reportscount': reportscount,
        'readreport':readreport,

    }
    return render(request, 'base/admin.html', context)

@staff_member_required(login_url='login')
def reportsView(request,pk):
    reports = Report.objects.get(id=pk)
    room_messages = Message.objects.all()
    reportscount = Report.objects.all().count()
    context = {
        'report': reports,
        'room_messages': room_messages,
        'reportscount':reportscount,
    }
    return render(request, 'base/newreports.html', context)

@staff_member_required(login_url='login')
def readedreportsView(request,pk):
    readedreport = ReadReport.objects.get(id=pk)
    room_messages = Message.objects.all()
    reportscount = Report.objects.all().count()
    context = {
        'room_messages': room_messages,
        'reportscount':reportscount,
        'readedreport':readedreport,
    }
    return render(request, 'base/reports.html', context)

@staff_member_required(login_url='login')
def reportRead(request):
    if request.method == 'POST':
        reportid = request.POST.get('reportid')
        readreport = Report.objects.get(id=reportid)
        ReadReport.objects.create(
            user=readreport.user,
            subject=readreport.subject,
            username=readreport.username,
            name=readreport.name,
            description=readreport.description,
            screenshot=readreport.screenshot,
            created=readreport.created,
        )
        readreport.delete()
        return redirect('reports')
