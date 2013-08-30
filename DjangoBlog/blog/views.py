# -*- coding: utf-8 -*-
# Create your views here.
from blog.models import Post
from django.views import generic 
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'postList'
    paginate_by = 10  #페이징을 위해서는 이것과 템플릿단에 pagination div만 추가하면 됨 !!

    def get_queryset(self):
        # order_by의 컬럼명 지정할 때 '-'를 추가하면 내림차순, '-' 없이 컬럼만 쓰면 오름차순
        return Post.objects.order_by('-created')
    
class CreateView(generic.CreateView):
    # 템플릿명을 지정하지 않으며, generic.CreateView에서 지정된 템플릿명을 찾아서 호출됨
    template_name = 'post_add.html'
    model = Post
    
class UpdateView(generic.UpdateView):
    template_name = 'post_add.html'
    model = Post
    
class DetailView(generic.DetailView):
    template_name = 'post_detail.html'
    model = Post

class DeleteView(generic.DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('list')
    
    def get_object(self, *args, **kwargs):
        object = super(DeleteView,self).get_object(*args, **kwargs)
        
        return object
