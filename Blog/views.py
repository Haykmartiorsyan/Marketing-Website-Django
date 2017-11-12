from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPosts, PostCategory, PostComment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
def Blog(request):
    context = {}
    posts = BlogPosts.objects.all().order_by('-created')
    latest_post = BlogPosts.objects.all().order_by('-created')[:2]
    post_category = PostCategory.objects.all().order_by('-id')[:3]

    for post in posts:
        s = post.created
        day = s.date().day
        month = s.date().month
        year = s.date().year

    items_count = 3
    paginator = Paginator(posts, items_count)
    page = request.GET.get('page', 1)

    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)

    query = request.GET.get('q')
    if query:
        post_page = posts.filter(
            Q(title=query) |
            Q(short_description=query) |
            Q(description=query) |
            Q(tag=query) |
            Q(category__name=query)
        ).distinct()

    context['post_page'] = post_page
    context['posts'] = posts
    context['post_category'] = post_category
    context['latest_post'] = latest_post
    context['posts'] = posts
    context['day'] = day
    context['month'] = month
    context['year'] = year

    return render(request, 'blog/index.html', context)


class single_post(generic.DetailView):

    template_name = 'blog/single-post.html'
    posts = BlogPosts.objects.all().order_by('-created')
    model = BlogPosts
    context_object_name = 'post'
    initial = {'key': 'value'}
    form_class = CommentForm

    def post(self, request, pk):
        post = get_object_or_404(BlogPosts, id=pk)

        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        return HttpResponseRedirect('./')

    def get_context_data(self, **kwargs):
        posts = BlogPosts.objects.all().order_by('-created')
        post_category = PostCategory.objects.all()[:3]
        latest_post = BlogPosts.objects.all().order_by('-created')[:2]

        for post in posts:
            s = post.created
            day = s.date().day
            month = s.date().month
            year = s.date().year

        context = super(single_post, self).get_context_data(**kwargs)

        context['posts'] = posts
        context['post_category'] = post_category
        context['latest_post'] = latest_post
        context['day'] = day
        context['month'] = month
        context['year'] = year

        return context