<html>
<head>
	<meta charset="utf-8">
	<title>LaKiller's Statbus</title>
	<meta name="description" content="Meanigless statistics for an even more meaningless game.">
	<link rel="stylesheet" href="/static/style.css">
	<link rel="shortcut icon" type="image/x-icon" href="/static/favicon.png"/>
</head>
<body>
	<div class='header'>Select a poll:</div>
	<div class='container'>
		<ul class="list">
		% cursor.execute("SELECT * FROM poll_question LIMIT 50")
		% if not cursor:
			Database query failed. Please tell LaKiller.
		% end
		% for x in cursor:
		% if x[5] == 1 or x[9] == 1:
		% continue
		% else:
		<li>Question: {{x[4]}} <a href='/poll/{{x[0]}}'>View</a></li>
		% end
		% end
		</ul>
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>