from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, View
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
import datetime
from .models import Notification

class NotificationListView(ListView):
	model = Notification
	context_object_name = 'notification_list' 

	def get_context_data(self, **kwargs):
	        context = super(NotificationListView, self).get_context_data(**kwargs)
	        return context

class NotificationUpdate(NotificationListView, UpdateView):
	pass

# class UserUpdate(UpdateView):
# 	model = User
# 	fields = [
# 	'name'
# 	]
# 	template_name = 'settings.html'

# 	def dispatch(self, request, *args, **kwargs):
#         handler = super(UserUpdate, self).dispatch(request, *args, **kwargs)
#         if self.object.submitted_by != self.request.user:
#             return HttpResponseForbidden("You didn't create this item.")
#         return handler

#     def form_valid(self, form):
#        user = form.save()
#        user.date_edited =  datetime.date.today()
#        user.save()
#        return HttpResponseRedirect(reverse_lazy(''))

# # class SettingsView(TemplateView)
# # 	model = User
# # 	template_name = 'settings.html'

# # 	def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['user_info'] = User.objects.all()[:5]
# #         return context
