from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.template.loader import render_to_string
from .models import Shop, Adress, Products
from .forms import ShopCreateForm

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound, JsonResponse



def index(request):
    return render(request, "home.html")


class ShopListView(ListView):
    model = Shop
    template_name = "home.html"
    context_object_name = 'shops'


class ShopDetailView(DetailView):
    model = Shop
    template_name = "detailShop.html"
    # pk_url_kwarg = 'id'
    context_object_name = 'shop'
    # extra_context = {'products': Products.objects.filter(shop == )}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.filter(shop = self.kwargs['pk'])
        return context
    

class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Shop
    template_name = 'createShop.html'
    form_class = ShopCreateForm
    # fields = ['name', 'adress']

    def form_valid(self, form):
        form.instance.ownerProfile = self.request.user
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({'my_form': render_to_string('templateForInlineForm.html', context = {'form': modelform_factory(Adress, fields=('city', 'street', 'house'))})})
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class AdressCreateView(LoginRequiredMixin, CreateView):
    model = Adress
    template_name = 'createAdress.html'
    fields = ['city', 'street', 'house']


