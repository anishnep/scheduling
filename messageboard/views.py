from django.shortcuts import render
from django.http import HttpResponse
from messageboard.models import Post, Comment
# Create your views here.


def message_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    return render(request, "messageboard/message_board.html", {'post_list':post_list})

def create_post(request):
    if request.method == "POST":
        post_message=request.POST.get("msg_text")
        post = Post(posted_by=request.user, message=post_message)
        post.save()
        
        #return render(request,"messageboard/post.html",{'post':post})
        return render(request,"messageboard/post.html",{'post':post})
    else:
        return HttpResponse("what!!!")
    
def add_comment(request):
    
    if request.method=="POST":
        post_id=request.POST.get("post_id")
        comment_text=request.POST.get("comment_text")
        if comment_text:
            post=Post.objects.get(pk=post_id)
            comment = Comment(comment_by=request.user, post=post, comment_text=comment_text)
       
            comment.save()
            return render(request, "messageboard/comments.html", {'post':post, 'comment':comment})
        #return render(request, "messageboard/_comment.html", {'post':post, 'comment':comment})
    else:
        return HttpResponse("NOT A POST REQUEST")