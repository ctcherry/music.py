#!/usr/bin/python

MUSIC_FILE = "~/.music"

VLC_EXEC = "/Applications/VLC.app/Contents/MacOS/VLC"
VLC_SOCKET = "/tmp/vlc.sock"

import os
import socket
import stat
import sys

from time import sleep

class MusicList(object):
    def __init__(self, file=MUSIC_FILE):
        self.path = os.path.expanduser(file)
        if not self.exists():
            self.write_default()
        self.load()
    
    def write_default(self):
        f = open(self.path, 'w')
        f.write("te: http://www.di.fm/mp3/techno.pls\n")
        f.write("tr: http://www.di.fm/mp3/trance.pls\n")
        f.write("vt: http://www.di.fm/mp3/vocaltrance.pls\n")
        f.close()
    
    def exists(self):
        return os.path.isfile(self.path)

    def load(self):
        if self.exists():
            f = open(self.path, 'r')
            music_lines = f.readlines()
            f.close
            split_lines = [self._striplist(ml.split(':',1)) for ml in music_lines]
            self.data = dict(split_lines)

    def find(self, item):
        if item in self.data:
            return self.data[item]
        else:
            return None

    def _striplist(self, l):
        return([x.strip() for x in l])


class VLCSocket(object):
    def __init__(self, exec_path=VLC_EXEC, socket_path=VLC_SOCKET):
        self.exec_path = exec_path
        self.socket_path = socket_path
        self.socket = None
        
    def connect(self):
        if self.socket is None:
            if not self.socket_exist():
                os.system("%s --daemon -I oldrc --rc-unix=%s --rc-fake-tty" % (self.exec_path, self.socket_path))
                sleep(1)
                
            self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.socket.connect(self.socket_path)
        
    def socket_exist(self):
        if os.path.exists(self.socket_path):
            mode = os.stat(self.socket_path).st_mode
            if stat.S_ISSOCK(mode):
                return True
            else:
                return False
        return False
    
    def send(self, data):
        if self.socket_exist():
            if self.socket is not None:
                self.socket.send(data+"\n")
        
    def close(self):
        self.socket.close()
        
    def quit(self):
        if self.socket_exist():
            self.send('quit')
    
    def play(self, url):
        self.connect()
        self.send('clear')
        self.send('add ' + url)
        
    def stop(self):
        self.send('stop')
            
    def resume(self):
        self.connect()
        self.send('play')


def main():
    cmd_name = os.path.basename(sys.argv[0])
    ml = MusicList()

    if not ml.exists():
        print "No Music file"
        exit()
    
    if len(sys.argv) == 1:
        print "Available streams:"
        for name, url in ml.data.items():
          print "%s (%s)" % (name, url)
        print ""
        print "- To play the first stream: %s %s" % (cmd_name, ml.data.keys()[0])
        print "- To stop: %s stop" % (cmd_name)
        print "- To resume: %s resume" % (cmd_name)
        print "- To quit: %s quit" % (cmd_name)
        print ""
        exit()

    vlc = VLCSocket()

    if sys.argv[1] == 'quit':
        vlc.quit()
        exit()

    if sys.argv[1] == 'stop':
        vlc.stop()
        exit()

    if sys.argv[1] == 'resume':
        vlc.resume()
        exit()

    url = ml.find(sys.argv[1])

    if url is not None:
        vlc.play(url)
        exit()


if __name__ == "__main__":
    main()