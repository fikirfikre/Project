from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from back_end.models import News, Achievements, About, Officials, Service, Institution
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import NewsSerializer, AchievementSerializer, OfficialSerializer, ContactUsSerializer, ServiceSerializer, InstitutionSerializer


class Home(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'index.html'

    def get(self, request):
        news = News.objects.all().order_by('date')[0:2]
        news_serializer = NewsSerializer(news, many=True)

        achievements = Achievements.objects.all()
        achievements_serializer = AchievementSerializer(
            achievements, many=True)

        officials = Officials.objects.all()
        officials_serializer = OfficialSerializer(officials, many=True)

        return Response(data=(news_serializer.data, achievements_serializer.data, officials_serializer.data))

    def post(self, request):
        contacts = ContactUsSerializer(data=request.data)
        contacts.is_valid(raise_exception=True)
        contacts.validated_data
        contacts.save()
        return Response('ok')


class NewsList(APIView):
    def get(self, request):
        queryset = News.objects.all()
        serializers = NewsSerializer(queryset, many=True)

        return Response(serializers.data)

    def post(self, request):
        news = NewsSerializer(data=request.data)
        news.is_valid(raise_exception=True)
        news.validated_data
        news.save()

        return Response(news, status=HTTP_201_CREATED)


class NewsDetail(APIView):
    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceList(APIView):
    def get(self, request):
        queryset = Service.objects.all()
        serializers = ServiceSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)


class ServiceDetail(APIView):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def institution_list(request):
    queryset = Institution.objects.all()
    serializers = InstitutionSerializer(queryset, many=True)
    return Response(serializers.data)

class InstitutionList(APIView):

    def get(self,request) :
        queryset = Institution.objects.all()
        serializer = InstitutionSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = InstitutionSerializer(data = request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)
    
class InstitutionDetail(APIView):

    def put(self,request,pk):
        institute = get_object_or_404(Institution,pk=pk)
        serializer = InstitutionSerializer(institute,request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        institute = get_object_or_404(Institution,pk=pk)
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OfficalsList(APIView):

    def get(self,request) :
        queryset = Officials.objects.all()
        serializer = OfficialSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = OfficialSerializer(data = request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)
    
class OfficalsDetail(APIView):

    def put(self,request,pk):
        offical = get_object_or_404(Officials,pk=pk)
        serializer = OfficialSerializer(offical,request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        offical = get_object_or_404(Institution,pk=pk)
        offical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AchievemntsList(APIView):

    def get(self,request) :
        queryset = Achievements.objects.all()
        serializer = AchievementSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AchievementSerializer(data = request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)
    
class AchievementsDetail(APIView):

    def put(self,request,pk):
        achievement = get_object_or_404(Achievements,pk=pk)
        serializer = AchievementSerializer(achievement,request.data)
        serializer.is_valid(rasie_exception = True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        achievement = get_object_or_404(Achievements,pk=pk)
        achievement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def resource_list(request):  # Resource page
    pass


def resource_detail(request, id):  # Resource Detail Page
    pass


def job_list(request):  # Job Page
    pass


def job_detail(request, id):  # Job detail Page
    pass


def job_form(request):  # Job form page
    pass
