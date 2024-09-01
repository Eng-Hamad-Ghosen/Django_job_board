#get data from model ==> json
from rest_framework import serializers
from .models import Job
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        # fields = '__all__'
        exclude = ('image','slug')
        
    def validate(self, data):#للتاد من صحة البيانات المدخلة
        # التحقق من وجود البريد الإلكتروني بالفعل في قاعدة البيانات
        if Job.objects.filter(title=data['title']).exists():
            raise serializers.ValidationError("The Title is already exists.")
        
        return data