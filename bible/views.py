from django.shortcuts import render
from .models import Bible
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def home(request):
    return render(request,"bible/home.html",{})

def show_bible_content(request,testament,bookno,chapter):
    b=Bible.objects.filter(testament=testament,bookno=bookno,chapter=chapter).order_by('verseno')
    chapters=Bible.objects.filter(testament=testament,bookno=bookno)
    
    for B in b:
        print(B.verseno)
    ch=[]
    for c in chapters:
        if c.chapter not in ch:
            ch.append(c.chapter)
    ch=sorted(ch)
    
    
    books=["ഉല്‍‍പത്തി","പുറപ്പാട്","ലേവ്യര്‍","സംഖ്യ","നിയമാവര്‍ത്തനം","ജോഷ്വാ","ന്യായാധിപ‌ന്‍‍മാര്‍","റൂത്ത്","1 സാമുവല്‍","2 സാമുവല്‍","1 രാജാക്ക‌ന്‍‍മാര്‍","2 രാജാക്ക‌ന്‍‍മാര്‍","1 ദിനവൃത്താന്തം","2 ദിനവൃത്താന്തം","എസ്രാ","നെഹമിയ","തോബിത്","യൂദിത്ത്","എസ്തേര്‍","1 മക്കബായര്‍","2 മക്കബായര്‍","ജോബ്","സങ്കീര്‍ത്തനങ്ങള്‍","സുഭാഷിതങ്ങള്‍","സഭാപ്രസംഗക‌ന്‍","ഉത്തമഗീതം","ജ്ഞാനം","പ്രഭാഷക‌ന്‍","ഏശയ്യാ","ജെറെമിയ","വിലാപങ്ങള്‍","ബാറൂക്ക്","എസെക്കിയേല്‍","ദാനിയേല്‍","ഹോസിയാ","ജോയേല്‍","ആമോസ്","ഒബാദിയ","യോനാ","മിക്കാ","നാഹും","ഹബക്കുക്ക്","സെഫാനിയ","ഹഗ്ഗായി","സഖറിയാ","മലാക്കി","മത്തായി","മര്‍ക്കോസ്","ലൂക്കാ","യോഹന്നാ‌ന്‍","അപ്പ. പ്രവര്‍ത്തനങ്ങള്‍","റോമാ","1 കൊറിന്തോസ്","2 കൊറിന്തോസ്","ഗലാത്തിയാ","എഫേസോസ്","ഫിലിപ്പി","കൊളോസോസ്","1 തെസലോനിക്കാ","2 തെസലോനിക്കാ","1 തിമോത്തേയോസ്","2 തിമോത്തേയോസ്","തീത്തോസ്","ഫിലെമോ‌ന്‍","ഹെബ്രായര്","യാക്കോബ്","1 പത്രോസ്","2 പത്രോസ്","1 യോഹന്നാ‌ന്‍","2 യോഹന്നാ‌ന്‍","3 യോഹന്നാ‌ന്‍","യുദാസ്","വെളിപാട്"]
    
    
    return render(request,"bible/show_content.html",{"bible":b,"bookno":bookno,"books":books[bookno-1],"chapter":chapter,"ch":ch,"testament":testament})

def show_content_ajax_call(request,testament,bookno,chapter):
    b=Bible.objects.filter(testament=testament,bookno=bookno,chapter=chapter).order_by('verseno')
    serialized_data = serializers.serialize('json',b)
    print(serialized_data)
    return JsonResponse(serialized_data,safe=False)

 
    
  


