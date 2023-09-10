from django.shortcuts import render

# Create your views here.
def contact(request):
    # return render(request, './first_app/index.html', context= {'author': 'Phitron', 'age': 19, 'marks': 33, 'courses': [
    #     {
    #         'id': 1,
    #         'course': 'C++',
    #         'teacher': 'Rahim'
    #     },
    #     {
    #         'id': 2,
    #         'course': 'Java',
    #         'teacher': 'kahim'
    #     },
    #     {
    #         'id': 3,
    #         'course': 'Python',
    #         'teacher': 'Fahim'
    #     }
    # ] })
    
    return render(request, './first_app/index.html', {"name": "I am Rahim", "marks": 86, "list": [24,3,10,5], "blog": "loram ipsum dolor, sit amet consecteru elit. Harum wquae pempore fugit laboum voluptas mollitia. Ecplicabo earum assumenda abcaecati et."})