% rebase('templates/base.tpl', title=title)

<h1>{{title}}</h1>
<ul class="media-list">
    % for post in post_list:
        % include('templates/posts_list.tpl')
    % end
</ul>