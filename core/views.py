from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .forms import UploadForm
from .models import Product

import csv
import re


def decode_utf8(line_iterator):
    for line in line_iterator:
        _decoded_line = line.decode('utf-8').lstrip('"')
        decoded_line = re.sub(r';",+', ';', _decoded_line)
        yield decoded_line


def create_upload(request):
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})

    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():

        products_file = csv.reader(decode_utf8(request.FILES['sent_file']), delimiter=';')
        next(products_file)  # Скипнуть хэдер

        for counter, line in enumerate(products_file):
            code = line[0]
            name = line[1]
            level_one = line[2]
            level_two = line[3]
            level_three = line[4]
            price = line[5]
            alt_price = line[6]
            quantity = line[7]
            property_fields = line[8]
            joint_purchases = line[9]
            measure_unit = line[10]
            image = line[11]
            display_on_index = line[12]
            description = line[13]

            p = Product()
            p.code = code
            p.name = name
            p.level_one = level_one
            p.level_two = level_two
            p.level_three = level_three
            p.price = price
            p.alt_price = alt_price
            p.quantity = quantity
            p.property_fields = property_fields
            p.joint_purchases = joint_purchases
            p.measure_unit = measure_unit
            p.image = image
            p.display_on_index = display_on_index
            p.description = description
            p.save()

        return redirect('/product_list')


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
