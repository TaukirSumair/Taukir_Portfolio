from django.shortcuts import render

def skill(request):
    context={'skills':'active'}
    return render(request,'edu/skill.html',context)
