from rest_framework.response import Response
from rest_framework.views import APIView
from openai import OpenAI
from PyPDF2 import PdfReader 
from .models import PDF

client = OpenAI()

que_prompt = "I want you to return a JSON object by analyzing the CV data provided in the following JSON format."
json_promt = '{"student_name":"", "projects": [{"title": "", "description": "", "tech_stack": [], "time_duration": {"start": "04-2020", "end": "05-2020", "duration_months": 2}, "relevancy": 5}], "experience": [{"role": "", "organization": "", "short_description": "", "tech_stack": [], "time_duration": {"start": "05-2022", "end": "07-2022", "duration_months": 3}, "relevancy": 4}], "college": {"name": "IIT Bombay", "branch": "Electrical Engineering", "degree": "Dual Degree", "cgpa": 8.2, "start": "07-2018", "end": "05-2023"}}'

from rest_framework import serializers

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'

class GetResume(APIView):
    def get(self, request):
        data = PDF.objects.all()
        serializer = PdfSerializer(data, many=True)
        return Response(serializer.data)

class GeminiView(APIView):
    def post(self, request):
        reader = PdfReader(request.FILES['cv']) 
        cv = ""
        for i in range(len(reader.pages)):
            cv += reader.pages[i].extract_text()

        prompt = que_prompt + "\n\n" + json_promt + "\n\n" + cv
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
        )
        response = response.choices[0].message.content
        with open('/media/sahil/New Volume/Learning/cruxbackend/api/a.json', 'w') as f:
            f.write(response)
        response = eval(response)
        PDF.objects.create(name=request.FILES['cv'].name, data=response)
        return Response({"data":response})