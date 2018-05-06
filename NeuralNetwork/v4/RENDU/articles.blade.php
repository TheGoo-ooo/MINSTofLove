<!-- Stored in resources/views/child.blade.php -->
@extends('layouts.app')
@section('title', 'Page Title')
@section('sidebar')
    @parent
    <p>This is appended to the master sidebar.</p>
@endsection
@section('content')
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="{{ secure_asset('js/fade.js')}}"></script>
  <div class="container-fluid">
    @if (isset($article_created) && $article_created)
      <div class="alert alert-success slide-up" role="alert">
        <p>Article submitted</p>
      </div>
    @endif
    @if (isset($article_updated) && $article_updated)
      <div class="alert alert-success slide-up" role="alert">
        <p>Article updated</p>
      </div>
    @endif
    @if (isset($review_created) && $review_created)
      <div class="alert alert-success slide-up" role="alert">
        <p>Review submitted</p>
      </div>
    @endif
    @if (isset($review_updated) && $review_updated)
      <div class="alert alert-success slide-up" role="alert">
        <p>Review updated</p>
      </div>
    @endif
      <h2>{{__('articles.header')}}</h2>
      <div class="mb-2">
        <a href="newarticle/">Create new article</a>
      </div>
    @foreach($c_articles as $a)
      @php
        $reviews = $a->reviews;
      @endphp
      <div class="rounded">
        <div class="article-container row">
          <div class="col-xs-12">
            <div class="col-md-9 col-xs-12 bg-dark text-light rounded">
              <h3><a class="text-light" href = "articles/{{$a->id}}">{{$a->title}}</a></h3>
              <div class="author-line">
                <p> {{ __('articles.by') }} <a href="#">{{$a->user()->first()->getName()}}</a></p>
              </div>
            </div>
            <div class="col-md-3 col-xs-12 bg-light">
                <a href={{URL::to('articles/' . $a->id . '/reviews')}}>
                  {{ __('articles.reviews')}} ({{ sizeof($reviews)}})
                </a></br>
                @if (Auth::check())
                  <a href={{URL::to('articles/' . $a->id . '/newreview')}}>
                    {{ __('articles.submit_review')}}
                  </a></br>
                  @if (Auth::id() == $a->user_id)
                    <a href={{URL::to('editArticle/' . $a->id)}}>
                      Edit article
                    </a></br>
                  @endif
                @endif
            </div>
          </div>
        </div>
      </div>
    @endforeach
  </div>
@endsection
