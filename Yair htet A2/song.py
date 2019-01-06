# create your Song class in this file
class Song:
    def __init__(self, title, artist, year, status):
        """
            Initialize required attributes for a Song
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status

    def mark_song(self, status):
        """
            Mark a song as required/learned
        """
        self.status = status

    def __str__(self):
        return "\'{}\' by {} ({:4}) {}".format(self.title, self.artist, self.year, (('(learned)', '')[self.status==False]))
