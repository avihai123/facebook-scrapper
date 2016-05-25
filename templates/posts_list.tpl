<li class="list-group-item">
    %if 'name' in post.keys():
        <h3><span class="label label-success">{{post['name']}}</span></h3>
    % end
    <p><strong>Post id - </strong>{{post['id']}}</p>
    % if 'message' in post.keys():
        <p><strong>Message:</strong> {{post['message']}}</p>
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