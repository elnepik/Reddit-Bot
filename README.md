<h1>Reddit-Bot</h1>
A simple reddit reply bot, this is the full code of pythonforengineers.com/build-a-reddit-bot-part-1/ reddit tutorial. 

<h3>main.py instructions:</h3>
<h4>Customize re.search to customize what the bot replies to.</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.55.54%20AM.png'>
<h4>Change the subreddit variable to decide what the subreddit the bot is active on</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.56.06%20AM.png'>
<h4>Change submission.reply to change what the bot says as a response</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.56.16%20AM.png'>
<h3>Instructions for praw.ini:</h3>
<h4>First go to reddit.com/prefs/apps</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.40.44%20AM.png'>
 <h4>Click the create app, or create another app button</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.41.10%20AM.png'>
 <h4>Fill out the form with whatever you want, and then you should see the below.</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%208.44.49%20AM.png'>
<h4>Now put the string of characters at the top of your app next to the client id part of the file. Put the string of characters next to your client secret into the client secret part, put your reddit password into password, and your reddit username into username.</h4>
<img src='https://raw.githubusercontent.com/elnepik/Reddit-Bot/master/Screen%20Shot%202020-07-13%20at%209.27.35%20AM.png'>
<h4>Now we need to move the praw.ini file to the right place, on mac move it to the $HOME/.config folder. First, cd into the directory of the bot, for example, 'cd downloads/Reddit-Bot' Then type 'mv praw.ini $HOME/.config' for more options go to https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#praw-ini-files. After this, you may now run main.py</h4>



