# -*- coding: utf-8 -*-
import sys
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
import commands

from webmanager.models import BeepSound
from webmanager.models import SayText
from dogwarning import settings

reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def index(request):
    sounds = BeepSound.objects.all()
    says = SayText.objects.all()

    return render_to_response('webmanager/index.html', 
        {'sounds': sounds, 'says': says}
    )


def play(url):
    try:
        command = u"source /etc/profile ; mpg123 '%s'" % url
        status, output = commands.getstatusoutput(command)
    except Exception as e:
        return HttpResponse(u"Play failure, E: %s" % str(e))

    if 'finished.' in output and 0 == status:
        return HttpResponseRedirect('/')
    else:
        return render_to_response('webmanager/error.html',
            { 'message': output.encode('utf-8') }
        )


def play_sound(request, pk):
    redirect_url = '/'
    try:
        sound = get_object_or_404(BeepSound, id=int(pk))
        return play(sound.path)
    except ValueError as e:
        return HttpResponse(u"Play failure, The id(%s) not a int" % pk)


def play_text(request):
    text = request.GET["text"]
    param = u"?tex=%s&lan=zh&tok=%s&ctp=1&cuid=x&per=1" % (text, 
            settings.baidu_tsn_token)

    url = settings.baidu_tsn + param
    return play(url)
