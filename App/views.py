# import imp
# from django.shortcuts import render
# from .models import App
# from django.http import JsonResponse

# # Create your views here.
# def details(request):
#     details = App.objects.all()
#     data = {
#         'details': list(details.values())
#         }
#     return JsonResponse(data)

# def per_details(request, pk):
#     per_det = App.objects.get(pk=pk)
#     data = {
#         'name' : per_det.name,
#         'address' : per_det.address,
#         'num' : per_det.num   
#     }

       
#     return JsonResponse(data)


