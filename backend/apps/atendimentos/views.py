from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.atendimentos.serializers import AreaSerializer, AtendimentoSerializer, SalaSerializer, ProcedimentoSerializer, ConvenioSerializer
from apps.atendimentos.models import Atendimentos, Area, Sala, Procedimento, Convenio

class AtendimentoView(APIView):
    serializer_class = AtendimentoSerializer
    Model = Atendimentos
    def get(self, request, id=None):
        if id:
            try:
                search_query = self.Model.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except search_query.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = self.Model.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_item = self.serializer_class(data=request.data)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(self.Model.objects.all(), pk=id)
        serializer_item = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_200_OK)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(self.Model.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Product with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

class AreaView(APIView):
    serializer_class = AreaSerializer
    Model = Area
    def get(self, request, id=None):
        if id:
            try:
                search_query = self.Model.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except search_query.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = self.Model.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_item = self.serializer_class(data=request.data)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(self.Model.objects.all(), pk=id)
        serializer_item = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_200_OK)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(self.Model.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Item with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

class SalaView(APIView): 
    serializer_class = SalaSerializer
    Model = Sala
    def get(self, request, id=None):
        if id:
            try:
                search_query = self.Model.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except search_query.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = self.Model.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_item = self.serializer_class(data=request.data)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(self.Model.objects.all(), pk=id)
        serializer_item = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_200_OK)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(self.Model.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Item with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)
    
class ProcedimentoView(APIView):
    serializer_class = ProcedimentoSerializer
    Model = Procedimento
    def get(self, request, id=None):
        if id:
            try:
                search_query = self.Model.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except search_query.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = self.Model.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_item = self.serializer_class(data=request.data)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(self.Model.objects.all(), pk=id)
        serializer_item = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_200_OK)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(self.Model.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Item with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)
    
class ConvenioView(APIView):
    serializer_class = ConvenioSerializer
    Model = Convenio
    def get(self, request, id=None):
        if id:
            try:
                search_query = self.Model.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except search_query.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = self.Model.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_item = self.serializer_class(data=request.data)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_201_CREATED)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(self.Model.objects.all(), pk=id)
        serializer_item = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data, status=status.HTTP_200_OK)
        return Response(serializer_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(self.Model.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Item with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)