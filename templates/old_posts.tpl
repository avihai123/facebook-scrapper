% rebase('templates/base.tpl', title=title)

<h1>{{title}}</h1>


<div class="row">
% for post in post_list:
  <div class="col-sm-6 col-md-4">
    <div class="thumbnail">
      <img src="{{post['picture']}}" alt="...">
      <div class="caption">
        <h3>Thumbnail label</h3>
        <p>{{post['message'] if 'message' in post.keys() else 'empty post'}}</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>
  % end
</div>

