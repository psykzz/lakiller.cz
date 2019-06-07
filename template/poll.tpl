<html>
<head>
	<meta charset="utf-8">
	<title>LaKiller's Statbus</title>
	<meta name="description" content="Meanigless statistics for an even more meaningless game.">
	<link rel="stylesheet" href="/static/style.css">
	<link rel="shortcut icon" type="image/x-icon" href="/static/favicon.png"/>
</head>
<body>
	<div class='header'>Select a poll | <a href='/'>Back</a></div>
	<div class='container'>
		<form form action='/poll' method='get'>
			Offset: <input value='{{offset}}' name='offset' type='text'/> <input value='Load' type='submit'/>
		</form>
		<ul class="left">
		% polls = src.poll.get_valid_polls()
		% for x in polls:
		<li>Poll {{x[0]}}: {{x[1]}} | <a href='/poll/{{x[0]}}'>View</a></li>
		% end
		</ul>
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>