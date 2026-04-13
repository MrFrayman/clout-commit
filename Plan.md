app.py should read the contents of data.txt and just replace it with a random char from [a-z] (excluding the one currently in data.txt). This way you don't get arbituary big files...

The run.sh basically calls app.py, followed by `git add data.txt`, `git commit -m "I just want recruiterts to think, I work/commit something every day..."`, `git push origin master`

To start every thing, clone the repo using SSH (and make sure to use private/public key auth). Next add a cronjob to run it daily.