#like views.py exactly but it is used for APIs only
from rest_framework.response import Response
from .serializers import JobSerializer
from rest_framework import status 
from .models import Job
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET','POST'])
def fbv_list(request):
    if request.method=='GET':
        joblist = Job.objects.all()
        serializer = JobSerializer(joblist , many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer = JobSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def fbv_pk(request,pk):
    joblist = Job.objects.get(id=pk)
    if request.method == 'GET':
        
        serializer=JobSerializer(joblist)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer=JobSerializer(joblist , request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'data':serializer.data},status=status.HTTP_202_ACCEPTED)
    
    if request.method=='DELETE':
        joblist.delete()
        return Response({'data':serializer.data},status=status.HTTP_100_CONTINUE)
    
class generic_list(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
