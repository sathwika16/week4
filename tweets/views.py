from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_form.html', {'form': form})

@login_required
def tweet_list(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

@login_required
def tweet_edit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweets/tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweets/tweet_confirm_delete.html', {'tweet': tweet})

def tweet_search(request):
    query = request.GET.get('q')
    tweets = Tweet.objects.filter(content__icontains=query)
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})
