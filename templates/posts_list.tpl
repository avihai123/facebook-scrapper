% if 'message' in post.keys() and 'shares' in post.keys():
    <li class="list-group-item">
        <p><strong>Post id - </strong>{{post['id']}}</p>
        <p><strong>Message</strong></p>
        <p> {{post['message']}}</p>
        <p>Total shares <span class="badge">{{post['shares']}}</span></p>
        % if 'full_picture' in post.keys():
            <a href="{{post['full_picture']}}" target="_blank"><img src="{{post['picture']}}" alt="{{post['id']}}"></a>
        % end
        <p><i class="glyphicon glyphicon-time"></i> Last modified <span class="badge">{{post['updated_time']}}</span>
        </p>
    </li>
% end