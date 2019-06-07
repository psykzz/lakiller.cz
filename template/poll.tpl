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
		% import src.poll
		{{! src.poll.get_valid_polls(cursor, offset)}}
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>