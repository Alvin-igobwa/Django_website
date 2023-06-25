from django.shortcuts import render
# The views here being created is manually created and not using the clas based views
# Create your views here.
def homescreenview(request):
    context = {}
    # context['some_string'] = "this is some string that I'm passing to the view"
    # context['some_number'] = 9090

    list_of_values = []
    list_of_values.append('first entry')
    list_of_values.append('second entry')
    list_of_values.append('third entry')
    list_of_values.append('fourth entry')
    context['list_of_values'] = list_of_values

    return render(request,"personal/home.html",context) # adding the context to the end means I can add more stuff above