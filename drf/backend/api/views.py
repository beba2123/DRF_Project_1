from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request, *args, **kwargs):
    # body = request.body #it will print the Json data in a string byte
    # data={}

    # try:
    #     data = json.loads(body) # inorder to parse the request body...
    # except:
    #     pass

    # print(data)
    # print(request.GET)
    # # print(request.POST)
    # data['params']  = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price {from line 24 to 25 we are doing serializatio
        #  means that changing the instance(model) in to python dictionary return JSON to my client}
        # but it is more manual method so inorder to make it automatic
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    #     json_data_form = json.dumps(data)
    # return HttpResponse(json_data_form, headers={'content-type': 'application/json'}) #we use all of this becouse of the httpResponse only pass string data so inorder to change into python dictionary format we use json.dump()
    return JsonResponse(data)
