from faker import Faker
from django.shortcuts import render

# Create your views here.
def story():
    fake = Faker()
    my_story = (
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            f"Hello my name is {fake.name()} and I work in {fake.company()}"
            )


    return my_story

def temperature_conversion(temperature, change_to):
    converted_temp = None
    temperature = int(temperature)
    if change_to == 'C':
        converted_temp = (temperature-32) * 0.5556
    else:
        converted_temp = (temperature * 1.8) + 32
    return converted_temp


def index(requests):
    mystory = story()
    converted_temp  = None
    print('this is print', requests.POST.get("input-temp"))
    if requests.method == 'POST':
            converted_temp = temperature_conversion(requests.POST.get('input-temp'), requests.POST.get('change_to'))
    return render(requests, 'temp_stories/index.html', {'story':mystory,'temp': converted_temp})


