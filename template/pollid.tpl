% from datetime import datetime
% pollid = str(pollid)
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
		<p><b>Information about poll ID {{pollid}}:</b></p>
		% cursor.execute('SELECT * FROM poll_question WHERE id = ' + pollid)
		% result = cursor.fetchall()
		% for x in result:
		% if x[5] == 1 or x[9] == 1:
		<p>Access Denied</p>
		% continue
		% else:
		<p>Question: {{x[4]}}</p>
		<p>Type: {{x[1]}}</p>
		<p>Start time: {{x[2].strftime('%d %B %Y - %H:%M:%S')}}</p>
		<p>End time: {{x[3].strftime('%d %B %Y - %H:%M:%S')}}</p>
		% end
		% end
		% if x[1] == 'OPTION':
		<p><b>Options:</b></p>
		% cursor.execute('SELECT text FROM poll_option WHERE pollid = ' + pollid)
		% result = cursor.fetchall()
		% cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 1')
		% result1 = cursor.fetchall()
		% cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND optionid = 2')
		% result2 = cursor.fetchall()
		<p>1. {{result[0][0]}}: {{result1[0][0]}}</p>
		<p>2. {{result[1][0]}}: {{result2[0][0]}}</p>
		% elif x[1] == 'TEXT':
		% cursor.execute('SELECT replytext FROM poll_textreply WHERE pollid = ' + pollid)
		% result = cursor.fetchall()
		<p><b>Replies:</b></p>
		% for z in range(len(result)):
		<p><b>{{z}}:</b> {{result[z][0]}}</p>
		% end
		% elif x[1] == 'NUMVAL':
		% cursor.execute('SELECT * FROM poll_option WHERE pollid = ' + pollid)
		% result = cursor.fetchall()
		<p><b>Options:</b></p>
		<p>Poll description: {{result[0][2]}}</p>
		<p>Minimum rating description: {{result[0][5]}}</p>
		<p>Middle rating description: {{result[0][6]}}</p>
		<p>Maximum rating description: {{result[0][7]}}</p>
		<p>Minimum rating: {{result[0][3]}}</p>
		<p>Maximum rating: {{result[0][4]}}</p>
		<p><b>Votes:</b></p>
		% for a in range(result[0][4] + 1):
		% cursor.execute('SELECT COUNT(*) FROM poll_vote WHERE pollid = ' + pollid + ' AND rating = ' + str(a))
		% result = cursor.fetchall()
		<p>Rating {{a}}: {{result[0][0]}}</p>
		% end
		% elif x[1] == 'MULTICHOICE':
		<p><b>Options:</b></p>
		% cursor.execute('SELECT COUNT(v.id) as VOTES, p.text FROM poll_vote v LEFT JOIN poll_option p ON v.optionid = p.id WHERE v.pollid = ' + pollid + ' GROUP BY v.optionid')
		% result = cursor.fetchall()
		% for y in result:
		<p>{{y[1]}} : {{y[0]}}</p>
		% end
		% end
	</div>
	<div class='footer'><a href='/'>Home</a> | Made by LaKiller8 | <a href='https://github.com/DominikPanic/lakiller.cz'>Source</a></div>
</body>
</html>