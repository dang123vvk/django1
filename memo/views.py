from django.views import generic
from .models import Memo

class MemoListView(generic.ListView):
    model = Memo

class MemoDetailView(generic.DetailView):
    model = Memo

class MemoCreateView(generic.CreateView):
    model = Memo
    fields = ['text']
    success_url = "/memo"

class MemoUpdateView(generic.UpdateView):
    model = Memo
    fields = ['text']
    success_url = "/memo"
    template_name_suffix = '_update_form'