from django.http.response import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.

@csrf_exempt
def CustomerList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def CustomerDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse({'status': 'false', 'message': 'User not found'})

    if request.method == 'GET':
        serializer = CustomerSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)