from click import password_option
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from markupsafe import re
from website.models import Room,Message,UserId
from django.http import HttpResponse
from django.contrib import messages
import random
import time

def index(request):
   return render(request, 'index.html')

def room(request,room):
   username = request.GET.get('username')
   password = request.GET.get('password')
   userids = request.GET.get('username')
   rooms = request.GET.get('room_name')
   room_details = Room.objects.get(name=room)
   user_id = UserId.objects.filter(username=userids)
   from_password = Room.objects.filter(password=password)


   return render(request, 'room.html', {
      'username': username,
      'room': room,
      'room_details': room_details,
      'user_id': user_id,
   })

def checkview(request):
   room = request.POST['room_name']
   username = request.POST['username']
   user_details = request.POST['username']
   password = request.POST['password']
   user_id = random.randrange(1,10**8)
   error_message = 'Message 3 char long!'

   banned_words = [
      'nigga',
      'fuck',
      'bitch',
      'dick'
   ]

   if request.method == 'POST':
          
                   
      if len(username) < 3:
         messages.error(request,'Username too short.')
         return redirect('/')
   
      elif Room.objects.filter(name=room).exists():
         return redirect('/'+room+'/?username='+username)

      elif username == banned_words[0] or username == banned_words[1]:
         messages.error(request,'This username is banned.')
         return redirect('/')

      elif username == banned_words[2] or username == banned_words[3]:
         messages.error(request,'This username is banned.')
         return redirect('/')
            
      else:
         new_room = Room.objects.create(name=room,password=password)
         new_user_id = UserId.objects.create(userId=user_id,username=username,rooms=room)
         new_user_id.save()
         new_room.save()
         return redirect('/'+room+'/?username='+username)



def send(request):
   message = request.POST['message']
   username = request.POST['username']
   room_id = request.POST['room_id']

   banned_words = [
      'nigga',
      'fuck',
      'bitch',
      'dick',
   ]

   if request.method == 'POST':

      if len(message) < 1:
            pass

      elif message == banned_words[0]:
            changed_text = ['Black Lives Matter!','Slnko je moja spriazniva vasen!', 'Som debilko X:D.']
            changed_message = random.choice(changed_text)
            new_changed_message = Message.objects.create(value=changed_message,user=username,room=room_id)
            new_changed_message.save()

      elif message == banned_words[1]:
            changed_text = ['I am gay','som deges more','Vcera som pojebal macku do riti']
            changed_message = random.choice(changed_text)
            new_changed_message = Message.objects.create(value=changed_message,user=username,room=room_id)
            new_changed_message.save()

      elif message == banned_words[2] or message == banned_words[3]:
            changed_text = ['Fuck me in the ass.','Im a bitch. :-)','SOM KOKOT XD!']
            changed_message = random.choice(changed_text)
            new_changed_message = Message.objects.create(value=changed_message,user=username,room=room_id)
            new_changed_message.save()

      else:
         new_message = Message.objects.create(value=message,user=username,room=room_id)
         new_message.save()
         #return HttpResponse('Message sent successfully.')

def getMessages(request,room):
   room_details = Room.objects.get(name=room)
   messages = Message.objects.filter(room=room_details.id)
   return JsonResponse({"messages":list(messages.values())})

def getUserId(request,user_id):
      userid = UserId.objects.get(userId=user_id)

