from django.shortcuts import render
from django.views.generic import View
from django.views.generic import CreateView

from blog.models import Post, Contact
from django.shortcuts import redirect


class HomePageView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        posts = Post.objects.all()
        self.context.update({'posts': posts})
        return render(request, template_name=self.template_name, context=self.context)


class AboutPageView(View):
    template_name = 'about.html'
    context = {}

    def get(self, request):
        posts = Post.objects.all()
        self.context.update({'posts': posts})
        return render(request, template_name=self.template_name, context=self.context)


class ContactPageView(View):
    template_name = 'contact.html'
    context = {}

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        return redirect('/')


class BlogPageView(View):
    template_name = 'full-width.html'
    context = {}

    def get(self, request):
        return render(request, template_name=self.template_name)


class AddBlog(View):
    pass


class SinglePageView(View):
    template_name = 'single.html'
    context = {}

    def get(self, request):
        return render(request, template_name=self.template_name)


class AddPostView(View):
    template_name = 'add-post.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        author = request.user

        post = Post.objects.create(
            title=title,
            image=image,
            description=description,
            author=author
        )
        post.save()
        return redirect('/')
