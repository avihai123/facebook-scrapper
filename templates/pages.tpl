% rebase('templates/base.tpl', title=title)
<ul class="list-group">
    % for page in page_list:
        <div class="list-group">
            <div class="list-group-item">
                <a href="{{page['id']}}/">
                    <h4 class="list-group-item-heading">{{page['name']}}</h4>
                    <p class="list-group-item-text">{{page['about']}}</p>
                    <p>fans - {{page['fan_count']}}</p>
                </a>
                <!-- List 3 best posts -->
                <button class="btn btn-info" data-toggle="collapse" data-target="#{{page['id']}}">Best Posts</button>
                <ul class="list-group collapse" id="{{page['id']}}">
                    % for post in post_dict[page['id']]:
                        % include('templates/posts_list.tpl')
                    % end
                </ul>
            </div>
        </div>
    % end
</ul>
