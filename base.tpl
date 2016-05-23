<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Pages</h1>
<ul>
    % for page in pages:
        name = page['name']
        <li><a href="{{name}}/details/">{{name}}</a></li>
    % end
</ul>
</body>
</html>