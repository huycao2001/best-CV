from django.shortcuts import render

from .models import CV
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

def subfunc(request, cv):
    templateNumber = request.POST.get('templateNumber')
    title = request.POST.get('title')
    cv_current_job = request.POST.get('cv_current_job')
    cv_avatar = request.POST.get('cv_avatar')
    cv_contact_info = request.POST.get('cv_contact_info')
    cv_contact_info_phone = request.POST.get('cv_contact_info_phone')
    cv_contact_info_gender = request.POST.get('cv_contact_info_gender')
    cv_contact_info_gmail = request.POST.get('cv_contact_info_gmail')
    cv_contact_info_website = request.POST.get('cv_contact_info_website')
    cv_contact_info_facebook = request.POST.get('cv_contact_info_facebook')
    cv_contact_info_home = request.POST.get('cv_contact_info_home')
    description = request.POST.get('description')
    is_published = request.POST.get('is_published', False)

    cv_education = request.POST.get('cv_education')
    cv_count_education = request.POST.get('cv_count_education')
    cv_degree1 = request.POST.get('cv_degree1')
    cv_graduation_time1 = request.POST.get('cv_graduation_time1')
    cv_graduation_school1 = request.POST.get('cv_graduation_school1')
    cv_degree2 = request.POST.get('cv_degree2')
    cv_graduation_time2 = request.POST.get('cv_graduation_time2')
    cv_graduation_school2 = request.POST.get('cv_graduation_school2')
    cv_degree3 = request.POST.get('cv_degree3')
    cv_graduation_time3 = request.POST.get('cv_graduation_time3')
    cv_graduation_school3 = request.POST.get('cv_graduation_school3')

    cv_lang = request.POST.get('cv_lang')
    cv_count_lang = request.POST.get('cv_count_lang')
    
    cv_lang1 = request.POST.get('cv_lang1')
    cv_lang1_expert = request.POST.get('cv_lang1_expert')
    cv_lang2 = request.POST.get('cv_lang2')
    cv_lang2_expert = request.POST.get('cv_lang2_expert')
    cv_lang3 = request.POST.get('cv_lang3')
    cv_lang3_expert = request.POST.get('cv_lang3_expert')
    cv_lang4 = request.POST.get('cv_lang4')
    cv_lang4_expert = request.POST.get('cv_lang4_expert')
    cv_lang5 = request.POST.get('cv_lang5')
    cv_lang5_expert = request.POST.get('cv_lang5_expert')

    cv_profile = request.POST.get('cv_profile')
    
    cv_experience = request.POST.get('cv_experience')
    cv_count_experience = request.POST.get('cv_count_experience')

    cv_company_role1 = request.POST.get('cv_company_role1')
    cv_job_description1 = request.POST.get('cv_job_description1')
    cv_company_name1 = request.POST.get('cv_company_name1')
    cv_working_time1 = request.POST.get('cv_working_time1')
    cv_company_role2 = request.POST.get('cv_company_role2')
    cv_job_description2 = request.POST.get('cv_job_description2')
    cv_company_name2 = request.POST.get('cv_company_name2')
    cv_working_time2 = request.POST.get('cv_working_time2')
    cv_company_role3 = request.POST.get('cv_company_role3')
    cv_job_description3 = request.POST.get('cv_job_description3')
    cv_company_name3 = request.POST.get('cv_company_name3')
    cv_working_time3 = request.POST.get('cv_working_time3')
    cv_company_role4 = request.POST.get('cv_company_role4')
    cv_job_description4 = request.POST.get('cv_job_description4')
    cv_company_name4 = request.POST.get('cv_company_name4')
    cv_working_time4 = request.POST.get('cv_working_time4')
    cv_company_role5 = request.POST.get('cv_company_role5')
    cv_job_description5 = request.POST.get('cv_job_description5')
    cv_company_name5 = request.POST.get('cv_company_name5')
    cv_working_time5 = request.POST.get('cv_working_time5')
    
    cv_skill = request.POST.get('cv_skill')
    cv_count_skill = request.POST.get('cv_count_skill')
    cv_skill1 = request.POST.get('cv_skill1')
    cv_skill1_expert = request.POST.get('cv_skill1_expert')
    cv_skill2 = request.POST.get('cv_skill2')
    cv_skill2_expert = request.POST.get('cv_skill2_expert')
    cv_skill3 = request.POST.get('cv_skill3')
    cv_skill3_expert = request.POST.get('cv_skill3_expert')
    cv_skill4 = request.POST.get('cv_skill4')
    cv_skill4_expert = request.POST.get('cv_skill4_expert')
    cv_skill5 = request.POST.get('cv_skill5')
    cv_skill5_expert = request.POST.get('cv_skill5_expert')
    cv_skill6 = request.POST.get('cv_skill6')
    cv_skill6_expert = request.POST.get('cv_skill6_expert')
    cv_skill7 = request.POST.get('cv_skill7')
    cv_skill7_expert = request.POST.get('cv_skill7_expert')
    cv_skill8 = request.POST.get('cv_skill8')
    cv_skill8_expert = request.POST.get('cv_skill8_expert')
    cv_skill9 = request.POST.get('cv_skill9')
    cv_skill9_expert = request.POST.get('cv_skill9_expert')
    cv_skill10 = request.POST.get('cv_skill10')
    cv_skill10_expert = request.POST.get('cv_skill10_expert')
    
    cv_interest = request.POST.get('cv_interest')
    cv_count_interest = request.POST.get('cv_count_interest')
    cv_interest1 = request.POST.get('cv_interest1')
    cv_interest2 = request.POST.get('cv_interest2')
    cv_interest3 = request.POST.get('cv_interest3')
    cv_interest4 = request.POST.get('cv_interest4')
    cv_interest5 = request.POST.get('cv_interest5')
    cv_interest6 = request.POST.get('cv_interest6')
    cv_interest7 = request.POST.get('cv_interest7')
    cv_interest8 = request.POST.get('cv_interest8')
    cv_interest9 = request.POST.get('cv_interest9')
    cv_interest10 = request.POST.get('cv_interest10')
    
    cv_cer = request.POST.get('cv_cer')
    cv_count_cer = request.POST.get('cv_count_cer')
    
    cv_cer_year1 = request.POST.get('cv_cer_year1')
    cv_cer_name1 = request.POST.get('cv_cer_name1')
    cv_cer_year2 = request.POST.get('cv_cer_year2')
    cv_cer_name2 = request.POST.get('cv_cer_name2')
    cv_cer_year3 = request.POST.get('cv_cer_year3')
    cv_cer_name3 = request.POST.get('cv_cer_name3')
    cv_cer_year4 = request.POST.get('cv_cer_year4')
    cv_cer_name4 = request.POST.get('cv_cer_name4')
    cv_cer_year5 = request.POST.get('cv_cer_year5')
    cv_cer_name5 = request.POST.get('cv_cer_name5')
    
    cv_activity = request.POST.get('cv_activity')
    cv_count_activity = request.POST.get('cv_count_activity')

    cv_activity_company_role1 = request.POST.get('cv_activity_company_role1')
    cv_activity_job_description1 = request.POST.get('cv_activity_job_description1')
    cv_activity_company_name1 = request.POST.get('cv_activity_company_name1')
    cv_activity_working_time1 = request.POST.get('cv_activity_working_time1')
    cv_activity_company_role2 = request.POST.get('cv_activity_company_role2')
    cv_activity_job_description2 = request.POST.get('cv_activity_job_description2')
    cv_activity_company_name2 = request.POST.get('cv_activity_company_name2')
    cv_activity_working_time2 = request.POST.get('cv_activity_working_time2')
    cv_activity_company_role3 = request.POST.get('cv_activity_company_role3')
    cv_activity_job_description3 = request.POST.get('cv_activity_job_description3')
    cv_activity_company_name3 = request.POST.get('cv_activity_company_name3')
    cv_activity_working_time3 = request.POST.get('cv_activity_working_time3')
    cv_activity_company_role4 = request.POST.get('cv_activity_company_role4')
    cv_activity_job_description4 = request.POST.get('cv_activity_job_description4')
    cv_activity_company_name4 = request.POST.get('cv_activity_company_name4')
    cv_activity_working_time4 = request.POST.get('cv_activity_working_time4')
    cv_activity_company_role5 = request.POST.get('cv_activity_company_role5')
    cv_activity_job_description5 = request.POST.get('cv_activity_job_description5')
    cv_activity_company_name5 = request.POST.get('cv_activity_company_name5')
    cv_activity_working_time5 = request.POST.get('cv_activity_working_time5')
    

    cv.templateNumber = templateNumber
    cv.title = title
    cv.cv_current_job = cv_current_job
    cv.cv_avatar = cv_avatar
    cv.description = description
    cv.cv_contact_info = cv_contact_info
    cv.cv_contact_info_phone = cv_contact_info_phone
    cv.cv_contact_info_gender = cv_contact_info_gender
    cv.cv_contact_info_gmail = cv_contact_info_gmail
    cv.cv_contact_info_website = cv_contact_info_website
    cv.cv_contact_info_facebook = cv_contact_info_facebook
    cv.cv_contact_info_home = cv_contact_info_home
    cv.is_published = True if is_published == "on" else False

    cv.cv_education = cv_education
    cv.cv_count_education = cv_count_education
    cv.cv_degree1 = cv_degree1
    cv.cv_graduation_time1 = cv_graduation_time1
    cv.cv_graduation_school1 = cv_graduation_school1
    cv.cv_degree2 = cv_degree2
    cv.cv_graduation_time2 = cv_graduation_time2
    cv.cv_graduation_school2 = cv_graduation_school2
    cv.cv_degree3 = cv_degree3
    cv.cv_graduation_time3 = cv_graduation_time3
    cv.cv_graduation_school3 = cv_graduation_school3

    cv.cv_lang = cv_lang
    cv.cv_count_lang = cv_count_lang
    
    cv.cv_lang1 = cv_lang1
    cv.cv_lang1_expert = cv_lang1_expert
    cv.cv_lang2 = cv_lang2
    cv.cv_lang2_expert = cv_lang2_expert
    cv.cv_lang3 = cv_lang3
    cv.cv_lang3_expert = cv_lang3_expert
    cv.cv_lang4 = cv_lang4
    cv.cv_lang4_expert = cv_lang4_expert
    cv.cv_lang5 = cv_lang5
    cv.cv_lang5_expert = cv_lang5_expert
    
    cv.cv_profile = cv_profile
    
    cv.cv_experience = cv_experience
    cv.cv_count_experience = cv_count_experience
    cv.cv_company_role1 = cv_company_role1
    cv.cv_job_description1 = cv_job_description1
    cv.cv_company_name1 = cv_company_name1
    cv.cv_working_time1 = cv_working_time1
    cv.cv_company_role2 = cv_company_role2
    cv.cv_job_description2 = cv_job_description2
    cv.cv_company_name2 = cv_company_name2
    cv.cv_working_time2 = cv_working_time2
    cv.cv_company_role3 = cv_company_role3
    cv.cv_job_description3 = cv_job_description3
    cv.cv_company_name3 = cv_company_name3
    cv.cv_working_time3 = cv_working_time3
    cv.cv_company_role4 = cv_company_role4
    cv.cv_job_description4 = cv_job_description4
    cv.cv_company_name4 = cv_company_name4
    cv.cv_working_time4 = cv_working_time4
    cv.cv_company_role5 = cv_company_role5
    cv.cv_job_description5 = cv_job_description5
    cv.cv_company_name5 = cv_company_name5
    cv.cv_working_time5 = cv_working_time5

    cv.cv_skill = cv_skill
    cv.cv_count_skill = cv_count_skill
    cv.cv_skill1 = cv_skill1
    cv.cv_skill1_expert = cv_skill1_expert
    cv.cv_skill2 = cv_skill2
    cv.cv_skill2_expert = cv_skill2_expert
    cv.cv_skill3 = cv_skill3
    cv.cv_skill3_expert = cv_skill3_expert
    cv.cv_skill4 = cv_skill4
    cv.cv_skill4_expert = cv_skill4_expert
    cv.cv_skill5 = cv_skill5
    cv.cv_skill5_expert = cv_skill5_expert
    cv.cv_skill6 = cv_skill6
    cv.cv_skill6_expert = cv_skill6_expert
    cv.cv_skill7 = cv_skill7
    cv.cv_skill7_expert = cv_skill7_expert
    cv.cv_skill8 = cv_skill8
    cv.cv_skill8_expert = cv_skill8_expert
    cv.cv_skill9 = cv_skill9
    cv.cv_skill9_expert = cv_skill9_expert
    cv.cv_skill10 = cv_skill10
    cv.cv_skill10_expert = cv_skill10_expert

    cv.cv_interest = cv_interest
    cv.cv_count_interest = cv_count_interest
    cv.cv_interest1 = cv_interest1
    cv.cv_interest2 = cv_interest2
    cv.cv_interest3 = cv_interest3
    cv.cv_interest4 = cv_interest4
    cv.cv_interest5 = cv_interest5
    cv.cv_interest6 = cv_interest6
    cv.cv_interest7 = cv_interest7
    cv.cv_interest8 = cv_interest8
    cv.cv_interest9 = cv_interest9
    cv.cv_interest10 = cv_interest10

    cv.cv_cer = cv_cer
    cv.cv_count_cer = cv_count_cer
    cv.cv_cer_year1 = cv_cer_year1
    cv.cv_cer_name1 = cv_cer_name1
    cv.cv_cer_year2 = cv_cer_year2
    cv.cv_cer_name2 = cv_cer_name2
    cv.cv_cer_year3 = cv_cer_year3
    cv.cv_cer_name3 = cv_cer_name3
    cv.cv_cer_year4 = cv_cer_year4
    cv.cv_cer_name4 = cv_cer_name4
    cv.cv_cer_year5 = cv_cer_year5
    cv.cv_cer_name5 = cv_cer_name5

    cv.cv_activity = cv_activity
    cv.cv_count_activity = cv_count_activity
    cv.cv_activity_company_role1 = cv_activity_company_role1
    cv.cv_activity_job_description1 = cv_activity_job_description1
    cv.cv_activity_company_name1 = cv_activity_company_name1
    cv.cv_activity_working_time1 = cv_activity_working_time1
    cv.cv_activity_company_role2 = cv_activity_company_role2
    cv.cv_activity_job_description2 = cv_activity_job_description2
    cv.cv_activity_company_name2 = cv_activity_company_name2
    cv.cv_activity_working_time2 = cv_activity_working_time2
    cv.cv_activity_company_role3 = cv_activity_company_role3
    cv.cv_activity_job_description3 = cv_activity_job_description3
    cv.cv_activity_company_name3 = cv_activity_company_name3
    cv.cv_activity_working_time3 = cv_activity_working_time3
    cv.cv_activity_company_role4 = cv_activity_company_role4
    cv.cv_activity_job_description4 = cv_activity_job_description4
    cv.cv_activity_company_name4 = cv_activity_company_name4
    cv.cv_activity_working_time4 = cv_activity_working_time4
    cv.cv_activity_company_role5 = cv_activity_company_role5
    cv.cv_activity_job_description5 = cv_activity_job_description5
    cv.cv_activity_company_name5 = cv_activity_company_name5
    cv.cv_activity_working_time5 = cv_activity_working_time5


def search_expenses(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        expenses = CV.objects.filter((Q(title__icontains=search_str) | Q(cv_current_job__icontains=search_str)) & Q(is_published=True))
        data = expenses.values()
        return JsonResponse(list(data), safe=False)


def get_showing_cvs(request, cvs):

    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter') == 'publishe':
            return cvs.filter(is_published=True)
        if request.GET.get('filter') == 'inpublishe':
            return cvs.filter(is_published=False)
    return cvs


@login_required
def index(request):
    cvs = CV.objects.filter(Q(owner=request.user))
    cv_search = CV.objects.filter(Q(is_published=True))
    
    context = {
        'cvs': get_showing_cvs(request, cvs),
        'cv_search': get_showing_cvs(request, cv_search)
    }
    return render(request, 'cv/index.html', context)


@login_required
def create_cv(request, idTemplate):
    cv = CV()
    context = {'cv': cv}

    if request.method == 'POST':
        context = {
            'data':request.POST,
        }

        subfunc(request, cv)

        cv.owner = request.user
        cv.save()

        messages.add_message(request, messages.SUCCESS, "cv created successfully")

        return HttpResponseRedirect(reverse('home'))

    url = 'cv/create-cv'+ str(idTemplate) +'.html'
    return render(request, url, context)


@login_required
def choose_template(request):
    return render(request, 'cv/choose-template.html')

@login_required
def cv_detail(request, id):
    cv = get_object_or_404(CV, pk=id)
    context = {
        'cv': cv,
        'title': cv.title,
        'cv_avatar': cv.cv_avatar,
        'cv_current_job': cv.cv_current_job,
        'cv_contact_info': cv.cv_contact_info,
        'cv_contact_info_phone': cv.cv_contact_info_phone,
        'cv_contact_info_gender': cv.cv_contact_info_gender,
        'cv_contact_info_gmail': cv.cv_contact_info_gmail,
        'cv_contact_info_website': cv.cv_contact_info_website,
        'cv_contact_info_facebook': cv.cv_contact_info_facebook,
        'cv_contact_info_home': cv.cv_contact_info_home,
        'cv_education': cv.cv_education,
        'cv_degree1': cv.cv_degree1,
        'cv_graduation_time1': cv.cv_graduation_time1,
        'cv_graduation_school1': cv.cv_graduation_school1,
        'cv_degree2': cv.cv_degree2,
        'cv_graduation_time2': cv.cv_graduation_time2,
        'cv_graduation_school2': cv.cv_graduation_school2,
        'cv_degree3': cv.cv_degree3,
        'cv_graduation_time3': cv.cv_graduation_time3,
        'cv_graduation_school3': cv.cv_graduation_school3,
        'cv_lang': cv.cv_lang,
        'cv_lang1': cv.cv_lang1,
        'cv_lang1_expert': cv.cv_lang1_expert,
        'cv_lang2': cv.cv_lang2,
        'cv_lang2_expert': cv.cv_lang2_expert,
        'cv_lang3': cv.cv_lang3,
        'cv_lang3_expert': cv.cv_lang3_expert,
        'cv_lang4': cv.cv_lang4,
        'cv_lang4_expert': cv.cv_lang4_expert,
        'cv_lang5': cv.cv_lang5,
        'cv_lang5_expert': cv.cv_lang5_expert,
        'cv_profile': cv.cv_profile,
        'description': cv.description,
        'cv_company_role1': cv.cv_company_role1,
        'cv_job_description1': cv.cv_job_description1,
        'cv_company_name1': cv.cv_company_name1,
        'cv_working_time1': cv.cv_working_time1,
        'cv_company_role2': cv.cv_company_role2,
        'cv_job_description2': cv.cv_job_description2,
        'cv_company_name2': cv.cv_company_name2,
        'cv_working_time2': cv.cv_working_time2,
        'cv_company_role3': cv.cv_company_role3,
        'cv_job_description3': cv.cv_job_description3,
        'cv_company_name3': cv.cv_company_name3,
        'cv_working_time3': cv.cv_working_time3,
        'cv_company_role4': cv.cv_company_role4,
        'cv_job_description4': cv.cv_job_description4,
        'cv_company_name4': cv.cv_company_name4,
        'cv_working_time4': cv.cv_working_time4,
        'cv_company_role5': cv.cv_company_role5,
        'cv_job_description5': cv.cv_job_description5,
        'cv_company_name5': cv.cv_company_name5,
        'cv_working_time5': cv.cv_working_time5,
        'cv_skill': cv.cv_skill,
        'cv_skill1': cv.cv_skill1,
        'cv_skill1_expert': cv.cv_skill1_expert,
        'cv_skill2': cv.cv_skill2,
        'cv_skill2_expert': cv.cv_skill2_expert,
        'cv_skill3': cv.cv_skill3,
        'cv_skill3_expert': cv.cv_skill3_expert,
        'cv_skill4': cv.cv_skill4,
        'cv_skill4_expert': cv.cv_skill4_expert,
        'cv_skill5': cv.cv_skill5,
        'cv_skill5_expert': cv.cv_skill5_expert,
        'cv_skill6': cv.cv_skill6,
        'cv_skill6_expert': cv.cv_skill6_expert,
        'cv_skill7': cv.cv_skill7,
        'cv_skill7_expert': cv.cv_skill7_expert,
        'cv_skill8': cv.cv_skill8,
        'cv_skill8_expert': cv.cv_skill8_expert,
        'cv_skill9': cv.cv_skill9,
        'cv_skill9_expert': cv.cv_skill9_expert,
        'cv_skill10': cv.cv_skill10,
        'cv_skill10_expert': cv.cv_skill10_expert,
        'cv_interest': cv.cv_interest,
        'cv_interest1': cv.cv_interest1,
        'cv_interest2': cv.cv_interest2,
        'cv_interest3': cv.cv_interest3,
        'cv_interest4': cv.cv_interest4,
        'cv_interest5': cv.cv_interest5,
        'cv_interest6': cv.cv_interest6,
        'cv_interest7': cv.cv_interest7,
        'cv_interest8': cv.cv_interest8,
        'cv_interest9': cv.cv_interest9,
        'cv_interest10': cv.cv_interest10,
        'cv_cer': cv.cv_cer,
        'cv_cer_year1': cv.cv_cer_year1,
        'cv_cer_name1': cv.cv_cer_name1,
        'cv_cer_year2': cv.cv_cer_year2,
        'cv_cer_name2': cv.cv_cer_name2,
        'cv_cer_year3': cv.cv_cer_year3,
        'cv_cer_name3': cv.cv_cer_name3,
        'cv_cer_year4': cv.cv_cer_year4,
        'cv_cer_name4': cv.cv_cer_name4,
        'cv_cer_year5': cv.cv_cer_year5,
        'cv_cer_name5': cv.cv_cer_name5,
        'cv_activity': cv.cv_activity,
        'cv_activity_company_role1': cv.cv_activity_company_role1,
        'cv_activity_job_description1': cv.cv_activity_job_description1,
        'cv_activity_company_name1': cv.cv_activity_company_name1,
        'cv_activity_working_time1': cv.cv_activity_working_time1,
        'cv_activity_company_role2': cv.cv_activity_company_role2,
        'cv_activity_job_description2': cv.cv_activity_job_description2,
        'cv_activity_company_name2': cv.cv_activity_company_name2,
        'cv_activity_working_time2': cv.cv_activity_working_time2,
        'cv_activity_company_role3': cv.cv_activity_company_role3,
        'cv_activity_job_description3': cv.cv_activity_job_description3,
        'cv_activity_company_name3': cv.cv_activity_company_name3,
        'cv_activity_working_time3': cv.cv_activity_working_time3,
        'cv_activity_company_role4': cv.cv_activity_company_role4,
        'cv_activity_job_description4': cv.cv_activity_job_description4,
        'cv_activity_company_name4': cv.cv_activity_company_name4,
        'cv_activity_working_time4': cv.cv_activity_working_time4,
        'cv_activity_company_role5': cv.cv_activity_company_role5,
        'cv_activity_job_description5': cv.cv_activity_job_description5,
        'cv_activity_company_name5': cv.cv_activity_company_name5,
        'cv_activity_working_time5': cv.cv_activity_working_time5,

        'count': int(cv.cv_count_education), 
        'cv_count_experience': int(cv.cv_count_experience),
        'cv_count_interest': int(cv.cv_count_interest),
        'cv_count_lang': int(cv.cv_count_lang),
        'cv_count_skill': int(cv.cv_count_skill),
        'cv_count_cer': int(cv.cv_count_cer),
        'cv_count_activity': int(cv.cv_count_activity),
    }
    if cv.is_published == True or cv.owner==request.user:
        cv_url = 'cv/cv-detail' + cv.templateNumber + '.html'
        return render(request, cv_url, context)
    else:
        return index(request)

@login_required
def cv_delete(request, id):
    cv = get_object_or_404(CV, pk=id)
    context = {'cv': cv}

    if request.method == 'POST':
        if cv.owner == request.user:
            cv.delete()
            messages.add_message(request, messages.SUCCESS, "CV deleted successfully"
                                 )
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR, "You cannot delete the CV of the other person"
                                 )
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'cv/cv-delete.html', context)


@login_required
def cv_edit(request, id):
    cv = get_object_or_404(CV, pk=id)
    #form = CVForm(instance=cv)
    context = {
        'cv': cv, 
        'count': int(cv.cv_count_education), 
        'cv_count_experience': int(cv.cv_count_experience),
        'cv_count_interest': int(cv.cv_count_interest),
        'cv_count_lang': int(cv.cv_count_lang),
        'cv_count_skill': int(cv.cv_count_skill),
        'cv_count_cer': int(cv.cv_count_cer),
        'cv_count_activity': int(cv.cv_count_activity),
    }
    if cv.owner != request.user:
        return index(request)


    if request.method == 'POST':
        subfunc(request, cv)

        if cv.owner == request.user:
            cv.save()

        messages.add_message(request, messages.SUCCESS, "CV update success"

                             )

        return HttpResponseRedirect(reverse('home'))


    cv_url = 'cv/cv-edit' + cv.templateNumber + '.html'
    print(context)
    return render(request, cv_url, context)
