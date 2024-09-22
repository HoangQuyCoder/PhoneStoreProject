from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .models import *

from io import BytesIO
import pandas as pd


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "provider")

    def generate_excel_file(self, data, file_name):
        excel_file = BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        df = pd.DataFrame.from_dict(data=data)
        df.to_excel(writer, sheet_name='Sheet 1', index=False)
        writer.close()
        excel_file.seek(0)
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment; filename={file_name}"
        return response

    def get_urls(self):
        urls = super().get_urls()
        product_url = [path('product-report/', self.download_product_data), ]
        return product_url + urls

    def download_product_data(self, request):
        all_product_values = Product.objects.all()
        product_data = {"Id": [], "Name": [],
                        "Price": [], "Quantity": [], "Provider": []}
        for product in all_product_values:
            product_data['Id'].append(product.id)
            product_data['Name'].append(product.name)
            product_data['Price'].append(product.price)
            product_data['Quantity'].append(product.quantity)
            product_data['Provider'].append(product.provider)

        return self.generate_excel_file(data=product_data, file_name="Product.xlsx")


class OderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date',)


class OderDeatailAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'order_add')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Order, OderAdmin)
admin.site.register(OrderDetail, OderDeatailAdmin)
admin.site.register(ShippingAddress)
admin.site.register(CustomerUser)
