<html>
<head>
	<meta charset="utf-8">
	<title>LaKiller's Statbus</title>
	<meta name="description" content="Meanigless statistics for an even more meaningless game.">
	<link rel="stylesheet" href="/static/style.css">
	<link rel="shortcut icon" type="image/x-icon" href="/static/favicon.png"/>
</head>
<body>
	<div class='header'>Poll Information!</div>
	<div class='container'>
		% cursor.execute('SELECT * FROM poll_question WHERE id = ' + pollid)
		<p>Information about poll ID {{pollid}}:</p>
		% if cursor:
		% for x in cursor:
		% if x[5] == 1 or x[9] == 1:
		<p>Access Denied</p>
		<p>Adminonly: {{x[5]}} Hide from view: {{x[9]}}</p>
		% else:
		<p>Question: {{x[4]}}</p>
		<p>Type: {{x[1]}}</p>
		<p>Start time: </p>
		<p>End time: </p>
		% end
		% end
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>