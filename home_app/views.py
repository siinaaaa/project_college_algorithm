from django.shortcuts import render


# Create your views here.
def api_for_dictionary():
    file = "C:/Users/Sina/Downloads/Dictionary.txt"
    list = []
    with open(file, 'r') as file:
        content = file.read()
        list.append(content)
    return list


def api_1(request):
    if request.method == 'POST':
        words = request.POST.get('words')
        split_of_words = words.split()
        lists = api_for_dictionary()
        for item in lists:
            print(type(item))
        return render(request, 'home_app/index.html', {'words': words})
    return render(request, 'home_app/index.html')
