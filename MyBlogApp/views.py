from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostWelcome, PostCars, CommentCarPosts, PostTech, CommentTechPosts
from .forms import CommentFormCars, CommentFormTech
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Profile
from django.db.models import Q



class SearchCarView(View):
    def get(self, request, *args, **kwargs):
        querysetc = PostCars.objects.all()
        queryc = request.GET.get('qsc')
        if queryc:
            querysetc = querysetc.filter(
                Q(topic__icontains=queryc) |
                Q(name__icontains=queryc)
            ).distinct()
        context = {
            'querysetc': querysetc
        }
        return render(request, 'MyBlogApp:MyBlogApp/CarSearch_results.html', context)


def LikeCarView(request, pk):
    postcars = get_object_or_404(PostCars, id=request.POST.get('postcars_id'))
    likedcars = False
    if postcars.likescars.filter(id=request.user.id).exists():
       postcars.likescars.remove(request.user)
       likedcars = False
    else:
       postcars.likescars.add(request.user)
       likedcars = True
    return HttpResponseRedirect(reverse('MyBlogApp:carpost-postcars_detail', args=[str(pk)]))



def LikeTechView(request, pk):
    posttech = get_object_or_404(PostTech, id=request.POST.get('posttech_id'))
    likedtech = False
    if posttech.likestech.filter(id=request.user.id).exists():
       posttech.likestech.remove(request.user)
       likedtech = False
    else:
       posttech.likestech.add(request.user)
       likedtech = True
    return HttpResponseRedirect(reverse('MyBlogApp:techpost-posttech_detail', args=[str(pk)]))



def UnLikeCarView(request, pk):
    postcars = get_object_or_404(PostCars, id=request.POST.get('postcars_id'))
    unlikedcars = False
    if postcars.unlikescars.filter(id=request.user.id).exists():
       postcars.unlikescars.remove(request.user)
       unlikedcars = False
    else:
       postcars.unlikescars.add(request.user)
       unlikedcars = True
    return HttpResponseRedirect(reverse('MyBlogApp:carpost-postcars_detail', args=[str(pk)]))



def UnLikeTechView(request, pk):
    posttech = get_object_or_404(PostTech, id=request.POST.get('posttech_id'))
    unlikedtech = False
    if posttech.unlikestech.filter(id=request.user.id).exists():
       posttech.unlikestech.remove(request.user)
       unlikedtech = False
    else:
       posttech.unlikestech.add(request.user)
       unlikedtech = True
    return HttpResponseRedirect(reverse('MyBlogApp:techpost-posttech_detail', args=[str(pk)]))




class PostListView(ListView):
    model = PostWelcome
    template_name = 'MyBlogApp/welcome.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostListCarView(ListView):
    model = PostCars
    template_name = 'MyBlogApp/cars.html'
    context_object_name = 'postscars'
    ordering = ['?']
    paginate_by = 5



class PostListTechView(ListView):
    model = PostTech
    template_name = 'MyBlogApp/tech.html'
    context_object_name = 'poststech'
    ordering = ['-date']
    paginate_by = 2



class UserPostListCarView(ListView):
    model = PostCars
    template_name = 'MyBlogApp/user_postscars.html'
    context_object_name = 'postscars'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostCars.objects.filter(by=user).order_by('-date')


class UserPostListTechView(ListView):
    model = PostTech
    template_name = 'MyBlogApp/user_poststech.html'
    context_object_name = 'poststech'
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostTech.objects.filter(author=user).order_by('-date')



class PostDetailCarView(DetailView):
        model = PostCars

        def get_context_data(self, *args, **kwargs):
            context = super(PostDetailCarView, self).get_context_data(*args, **kwargs)

            stuff = get_object_or_404(PostCars, id=self.kwargs['pk'])
            stuffer = get_object_or_404(PostCars, id=self.kwargs['pk'])
            total_likescars = stuff.total_likescars()
            total_unlikescars = stuffer.total_unlikescars()

            likedcars =False
            unlikedcars = False
            if stuff.likescars.filter(id=self.request.user.id).exists() and stuffer.unlikescars.filter(id=self.request.user.id).exists():
                likedcars = True
                unlikedcars = True
            context['total_likescars'] = total_likescars
            context['total_unlikescars'] = total_unlikescars
            context['likedcars'] = likedcars
            context['unlikedcars'] = unlikedcars
            return context




class PostDetailTechView(DetailView):
        model = PostTech

        def get_context_data(self, *args, **kwargs):
            context = super(PostDetailTechView, self).get_context_data(*args, **kwargs)
            stuff = get_object_or_404(PostTech, id=self.kwargs['pk'])
            stuffer = get_object_or_404(PostTech, id=self.kwargs['pk'])
            total_likestech = stuff.total_likestech()
            total_unlikestech = stuffer.total_unlikestech()

            likedtech =False
            unlikedtech = False
            if stuff.likestech.filter(id=self.request.user.id).exists() and stuffer.unlikestech.filter(id=self.request.user.id).exists():
                likedtech = True
                unlikedtech = True
            context['total_likestech'] = total_likestech
            context['total_unlikestech'] = total_unlikestech
            context['likedtech'] = likedtech
            context['unlikedtech'] = unlikedtech
            return context



class AddCommentCarView(CreateView):
        model = CommentCarPosts
        form_class = CommentFormCars
        template_name = 'MyBlogApp/add_commentCars.html'
        ordering = ['-timestampCars']

        def get_success_url(self):
            return reverse('MyBlogApp:carpost-postcars_detail', kwargs={'pk': self.object.postcars.pk})

        def form_valid(self, form):
            form.instance.postcars_id = self.kwargs['pk']
            return super().form_valid(form)


class AddCommentTechView(CreateView):
    model = CommentTechPosts
    form_class = CommentFormTech
    template_name = 'MyBlogApp/add_commentTech.html'
    ordering = ['-timestampTech']

    def get_success_url(self):
        return reverse('MyBlogApp:techpost-posttech_detail', kwargs={'pk': self.object.posttech.pk})

    def form_valid(self, form):
        form.instance.posttech_id = self.kwargs['pk']
        return super().form_valid(form)


class PostCreateCarView(LoginRequiredMixin, CreateView):
    model = PostCars
    fields = ['topic', 'content', 'imge']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)


class PostCreateTechView(LoginRequiredMixin, CreateView):
    model = PostTech
    fields = ['title', 'content', 'img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = PostWelcome
        success_url = '/'

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False


class PostUpdateCarView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostCars
    fields = ['topic', 'content']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.by:
            return True
        return False


class PostDeleteCarView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = PostCars
        success_url = '/'

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.by:
                return True
            return False


class PostUpdateTechView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostTech
    fields = ['title', 'author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteTechView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostTech
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
