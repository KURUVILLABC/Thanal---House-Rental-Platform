from django.contrib import admin

# Register your models here.
# user_login ,house_type ,house_manager ,house_details ,house_pics ,user_details ,house_request,user_docs
# house_messages ,house_agreement ,house_pool_advertisement ,house_pooling_request ,house_pool_details
# transaction_details ,house_rent_payment_log ,feedback



from .models import transaction_details ,house_rent_payment_log ,feedback

from.models import user_login,house_type ,house_manager ,house_details ,house_pics ,user_details ,house_request,user_docs
from.models import house_messages ,house_agreement ,house_pool_advertisement ,house_pooling_request ,house_pool_details


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(house_type)
admin.site.register(house_manager)
admin.site.register(house_details)
admin.site.register(house_pics)

admin.site.register(house_request)
admin.site.register(user_docs)

admin.site.register(house_messages)
admin.site.register(house_agreement)
admin.site.register(house_pool_advertisement)
admin.site.register(house_pooling_request)
admin.site.register(house_pool_details)

admin.site.register(transaction_details)
admin.site.register(house_rent_payment_log)
admin.site.register(feedback)
