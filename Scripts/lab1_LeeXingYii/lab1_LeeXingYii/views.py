from django.shortcuts import render
from django.utils.safestring import mark_safe
import random

def homepage(request):
    return render(request, 'home.html')

def lunch(request):
    lunch_options = {
        1: "Nasi Lemak",
        2: "Nasi Ayam",
        3: "KFC",
        4: "Domino pizza",
        5: "Laksa",
        6: "Sushi"
    }
    dice_roll = random.randint(1, 6)
    lunch = lunch_options[dice_roll]
    return render(request, 'lunch.html',{'lunch': lunch})

def pattern(request):
    patterns = ""
    for i in range(1, 8):
        patterns += "#" * i + "<br>"
    for i in range(2, 1, -1):
        patterns += "#" * i + "<br>"
    for i in range(2, 1, -1):
        patterns += "#" * i + "<br>"
    patterns = mark_safe(patterns)
    return render(request, 'pattern.html', {'patterns': patterns})

def cgp(request):
    subjects = ["Malays", "English", "Chinese", "Mathematics", "Science"]
    # Assume the credit hours for each subject
    credit_hours = [3, 3, 3, 2, 2]

    marks = [random.randint(70, 100) for _ in range(len(subjects))]

    grade_points = [
        4 if mark >= 90 else
        3.7 if mark >= 85 else
        3.3 if mark >= 80 else
        3.0 if mark >= 75 else
        2.7 if mark >= 70 else
        2.3 if mark >= 65 else
        2.0 if mark >= 60 else
        0  # Fail grade (adjust as needed)
        for mark in marks
    ]

    total_credit_hours = sum(credit_hours)

    #Let quality points start from 0
    quality_points = 0
    for i in range(len(subjects)):
         quality_points += grade_points[i] * credit_hours[i]

    cgp = round(quality_points / total_credit_hours, 2)
    
    data = "<br><br>".join([f"Subject: {subjects[i]}<br>Mark: {marks[i]}<br>Grade point: {grade_points[i]}<br>Credit hours: {credit_hours[i]}" for i in range(len(subjects))])

    data = mark_safe(data)
    context = {
         "cgp" : cgp,
         "data" : data,
    }



    return render(request, "cgp.html", context)