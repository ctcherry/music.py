music.py
========

A simple script intended to quickly play internet music streams from the commandline. Focus on being simple and effective, I use this when programming to help me get in the zone, so I wanted something that would turn on some music then get out of my way!

Requirements
------------
VLC needs to be installed.

I've only used it on OSX, I suspect with tweaks to the paths (namely the VLC executable path) it should work on other *nix systems. It won't run on Windows since it communicates with VLC via a UNIX socket.

Installation
------------

- Put it somewhere in your path, I personally use ~/bin/music
- `$ chmod +x ~/bin/music`
- run it: `$ music`

One Liner:

`$ bash < <(curl -s https://raw.github.com/ctcherry/music.py/master/install.sh)`

Configuration
-------------

The script will auto-create its configuration file in ~/.music. It's a very simple file, and includes a few DI.fm streams by default, feel free to add anything that VLC supports. The format is one `name_here: http://url` entry per line.
