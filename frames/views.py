from django.shortcuts import render
from .models import Frame
import random
from django.shortcuts import redirect
from .models import Frame, URL

def frame_view(request):
    frames = Frame.objects.all()
    return render(request, 'frames/frame_view.html', {'frames': frames})





def display_urls(request, frame_id):
    urls = URL.objects.filter(frame_id=frame_id)
    if urls:
        url = random.choice(urls)
        return redirect(url.url)
    return redirect('frames:frame_view')

