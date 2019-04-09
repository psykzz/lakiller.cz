% from datetime import datetime
<html>
<head>
	<meta charset="utf-8">
	<title>LaKiller's Statbus</title>
	<meta name="description" content="Meanigless statistics for an even more meaningless game.">
	<link rel="stylesheet" href="/static/style.css">
	<link rel="shortcut icon" type="image/x-icon" href="/static/favicon.png"/>
</head>
<body>
	<div class='header'>Poll Information | <a href='/poll'>Back</a></div>
	<div class='container left'>
		% cursor.execute('SELECT * FROM poll_question WHERE id = ' + pollid)
		<p><b>Information about poll ID {{pollid}}:</b></p>
		% if not cursor:
		<p>Database error occured.</p>
		% else:
		% result = cursor.fetchall()
		% for x in result:
		% if x[5] == 1 or x[9] == 1:
		<p>Access Denied</p>
		<p>Adminonly: {{bool(x[5])}} | Hide from view: {{bool(x[9])}}</p>
		% else:
		<p>Question: {{x[4]}}</p>
		<p>Type: {{x[1]}}</p>
		<p>Start time: {{x[2].strftime('%d %B, %Y - %H:%M:%S')}}</p>
		<p>End time: {{x[3].strftime('%d %B, %Y - %H:%M:%S')}}</p>
		% end
		% end
		% end
		% if x[1] == 'OPTION':
		<p><b>Options:</b></p>
		% cursor.execute('SELECT text FROM poll_option WHERE pollid = ' + pollid)
		% if not cursor:
		<p>Database error occured.</p>
		% else:
		% result = cursor.fetchall()
		% for y in range(len(result)):
		<p>{{y+1}}. {{result[y][0]}}</p>
		% end
		% end
		<p><b>Votes:</b></p>
		% cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 1')
		% if not cursor:
		<p>Database error occured.</p>
		% else:
		% count = cursor.fetchall()
		<p>Option 1: {{count[0][0]}}</p>
		% end
		% cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 2')
		% if not cursor:
		<p>Database error occured.</p>
		% else:
		% count = cursor.fetchall()
		<p>Option 2: {{count[0][0]}}</p>
		% end
		% elif x[1] == 'TEXT':
		% cursor.execute('SELECT replytext FROM poll_textreply WHERE pollid = ' + pollid)
		% if not cursor:
		<p>Database error occured.</p>
		% else:
		% result = cursor.fetchall()
		% for z in range(len(result)):
		<p><u>Reply {{z}}:</u> {{result[z][0]}}</p>
		% end
		% end



		% end
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>