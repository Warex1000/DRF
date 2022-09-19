from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from women.models import *
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer


# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all() # Переопределили в методе get_queryset
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=False)
#     def category(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         return Response({'category': category.name})

# Класс Плагинации, Настройки вывода количества данных по API запросу. Указано по 3.
class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination   # Подключили клас плагинации

    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # Если указать параметр, например TokenAuthentication то доступы будут предоставляться только по токенам а по сессии не будет.


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )   # доступ только для авторизированных пользователей.
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsOwnerOrReadOnly, )
    # Если стоит класс IsOwenerOrReadOnly то доступ на редиктирование только пользователю который создал запись


# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):   # Только на удаление
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    ''' 1) Если не авторизирован, то можешь смотреть, если авторизирован или админ то можешь смотреть и удалять
    в http://127.0.0.1:8000/api/v1/womendelete/3/'''
    permission_classes = (IsAdminOrReadOnly, )   # 1)
    ''' 2) Если не авторизирован, то смотреть и удалить не можешь в http://127.0.0.1:8000/api/v1/womendelete/3/.'''
    # permission_classes = (IsAdminUser,)   # 2)


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):   # Чтение, Обновление, Удаление данных
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     def get(self, request):
#         women_list = Women.objects.all()
#         return Response({'posts': WomenSerializer(women_list, many=True).data})
#         # many=True - не одна запись а список записей .data - словарь из переобразованных данных.
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Objects does not exist'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})


    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'error': 'Method DELETE not allowed'})
    #     serializer = WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': 'deleted post' + str(pk)})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer





