from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'main/index.html')

def education(request):
    education_data = {
        'schools': [
            {
                'name': 'Boston College',
                'degree': "Bachelor's of Science in Computer Science",
                'minor': 'Minor in Finance',
                'years': '2021-2025',
                'logo': 'images/bc-logo.png',
                'website': 'https://www.bc.edu'
            },
            {
                'name': 'Universidad Carlos III de Madrid',
                'degree': 'Concentration in Computer Science',
                'years': '2023-2023',
                'logo': 'images/madrid-logo.png',
                'website': 'https://www.uc3m.es/home'
            },
            {
                'name': 'Marymount High School Los Angeles',
                'degree': 'Summa Cum Laude',
                'years': '2017-2021',
                'logo': 'images/marymount-logo.png',
                'website': 'https://www.mhs-la.org'
            }
        ]
    }
    return render(request, 'main/education.html', education_data)

def projects(request):
    return render(request, 'main/projects.html')

def interests(request):
    coding_languages = [
        {'name': 'Python', 'icon': 'images/python-logo.png'},
        {'name': 'Java', 'icon': 'images/java-logo.png'},
        {'name': 'C++', 'icon': 'images/cpp-logo.png'},
        {'name': 'HTML5', 'icon': 'images/html5-logo.png'},
        {'name': 'CSS3', 'icon': 'images/css3-logo.png'},
        {'name': 'Figma', 'icon': 'images/figma-logo.png'},
        {'name': 'Microsoft Office', 'icon': 'images/microsoft-logo.png'}
    ]
    passions = {
        'martial_arts': {
            'title': 'Z-Ultimate Self Defense',
            'description': 'After practicing for 15 years, I earned my first degree black belt in mixed martial arts from Z-Ultimate Self Defense Studios. In High School, I was also able to teach younger students in their group lessons.',
            'logo': 'images/z-ultimate-logo.png'
        },
        'campus_rec': {
            'title': 'Campus Recreation',
            'description': 'I was a facility supervisor at Boston College\'s recreation center, where I managed all the student employees and served as a resource for all guests and members.',
            'logo': 'images/campus-rec-logo.png'
        }
    }
    context = {
        'coding_languages': coding_languages,
        'passions': passions
    }
    return render(request, 'main/interests.html', context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({'status': 'success', 'message': 'Message received! (Functionality coming soon)'})
        except:
            return JsonResponse({'status': 'error', 'message': 'There was an error. Please try again.'}, status=400)
    return render(request, 'main/contact.html')
