<li class="media">
    <div class="media-left">
      <a href="{{post['full_picture'] if 'full_picture' in post.keys() else '#'}}">
        <img class="media-object" src="{{post['picture'] if 'picture' in post.keys() else '#'}}" alt="{{post['id']}}" width="96" height="96">
      </a>
    </div>
    <div class="media-body">
      <h4 class="media-heading">{{post['name'] if 'name' in post.keys() else 'Unnamed post' }}</h4>
      % if 'message' in post.keys():
      <p>{{post['message']}}</p>
      % end
      <p>{{post['shares']}} shares {{post['likes']}} likes {{post['comments']}} comments</p>
      <p><i class="glyphicon glyphicon-time"></i><span class="badge">{{post['updated_time']}}</span>
    </div>
</li>

<!--
<li class="list-group-item">
    %if 'name' in post.keys():
        <h3><span class="label label-info"><a href="https://www.facebook.com/{{post['id']}}/">{{post['name']}}</a></span></h3>
    % end
    % if 'message' in post.keys():
        <p>{{post['message']}}</p>
    % end
    % if 'shares' in post.keys():
        <p>Total shares <span class="badge">{{post['shares']}}</span></p>
    % end
    % if 'full_picture' in post.keys():
        <a href="{{post['full_picture']}}" target="_blank"><img src="{{post['picture']}}" alt="{{post['id']}}"></a>
    % end
    <p><i class="glyphicon glyphicon-time"></i> Last modified <span class="badge">{{post['updated_time']}}</span>
    </p>
</li>
-->