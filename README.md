music.py
========

A simple script intended to quickly play internet music streams from the commandline. Focus on being simple and effective, I use this when programming to help me get in the zone, so I wanted something that would turn on some music then get out of my way!

Requirements
------------
VLC needs to be installed. (Tested with version 1.1.11 - 2.0.0)

Tested with Python 2.7.1, probably works on other recent versions too.

I've only used it on OSX, I suspect with tweaks to the paths (mainly the VLC executable path) it should work on other *nix systems. It won't run on Windows since it communicates with VLC via a UNIX socket.

Installation
------------

- Put the music.py file it somewhere in your path, I personally use `~/bin` and just name it `music`
- Give it executable permission `$ chmod +x ~/bin/music`
- Run it: `$ music`

One Liner:

`$ bash < <(curl -s https://raw.github.com/ctcherry/music.py/master/install.sh)`

Configuration
-------------

The script will auto-create its configuration file in `~/.music`. It's a very simple file, and includes a few DI.fm streams by default, feel free to add anything that VLC supports. The format is `name_here: http://url` one entry per line.

But...
------
You don't like Python? How about a version in Ruby: [music.rb](https://github.com/ctcherry/music.rb)