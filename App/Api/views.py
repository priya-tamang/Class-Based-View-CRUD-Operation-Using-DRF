from App.models import App
from App.Api.serializers import detailSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class details_list(APIView):

    def get(self, request):
        Person_detail = App.objects.all()
        serializer = detailSerializers(Person_detail, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = detailSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

class each_details(APIView): 

    def get(self, request, pk):
        try:
            Person_detail = App.objects.get(pk=pk)
        except:
            return Response({'error':'Details not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = detailSerializers(Person_detail )
        return Response(serializer.data)

    def put(self, request, pk):
         Person_detail = App.objects.get(pk = pk)
         serializer = detailSerializers(Person_detail, data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         else:
            return Response(serializer.error)

    def delete(self, request, pk):
        Person_detail = App.objects.get(pk =pk)
        if Person_detail.delete():
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


       
