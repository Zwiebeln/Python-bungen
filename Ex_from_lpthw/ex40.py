#this goes in mystuff.py
def apple():
    print "I am apples!"

tangerine ="Living reflection of a dream"

class Song(object):
    def __init__(self, lyrics):
        self.lyrics= lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday= Song(["Happy birtyday to you","I don't wan to get sued", "So I'll stop right here"])

bulls_on_parad = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parad.sing_me_a_song()
