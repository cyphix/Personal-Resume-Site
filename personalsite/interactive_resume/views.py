from django.shortcuts import render

from . import models



def interactive_resume_view(request):
    template_name = 'index.html'
    context = {}

    context['contacts'] = models.Contact.objects.all()
    context['education'] = models.Education.objects.order_by('-end_date', '-start_date')
    context['job_history'] = models.JobHistory.objects.order_by('-end_date', '-start_date')
    context['job_history_info'] = models.JobHistoryInfo.objects.all()
    context['profile'] = models.Profile.objects.all().first()
    context['projects'] = models.Project.objects.all()
    context['skills'] = models.Skill.objects.order_by('-rating', 'skill_name')
    context['tools'] = models.Tool.objects.order_by('-rating', 'tool_name')

    return render(request, template_name, context)
