
from django.shortcuts import render, redirect
from .models import Post

# View to create a new Post object
def create_post(request):
    if request.method == "POST":  # If the form is submitted
        title = request.POST.get('title')  # Get the title from the form
        content = request.POST.get('content')  # Get the content from the form

        # Create and save the Post object
        new_post = Post.objects.create(title=title, content=content)

        # Redirect to the post_detail view to display the newly created post
        return redirect('post_detail', pk=new_post.pk)

    # If it's a GET request, render the form for creating a post
    return render(request, 'create_post.html')

# View to display the details of a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch post by primary key, or return 404 if not found
    return render(request, 'post_detail.html', {'post': post})
