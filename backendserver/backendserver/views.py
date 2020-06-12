import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class api_news(APIView):

	def get(self,request):
		x=requests.get("https://newsapi.org/v2/everything?q=trump&apiKey=ed670e2fd04f475fa4b296d2085be2e3")		
		# print(x.json())

		return HttpResponse(x)

	def post(self,request):
		pass