# create your SongList class in this file
from song import Song


class SongList:
    #Initialize an empty list for Song object
    def __init__(self, ):
        self.songs = []

    #Method to return a user selected single song object
    def get_song(self, title):
        for song in self.songs:
            if song[0].title == title:
                return song[0]

    #This method adds single song object to songs list
    def add_song(self, title, artist, year):
        self.songs.append([Song(title, artist, year, 'y')])

    def song_left_to_learn(self):
        """
        Loops through songs list and counts all the songs that needs to be learned and returns the count
        """
        required_songs = 0
        for song in self.songs:
            if song[0].status == 'y':
                required_songs += 1
        return required_songs

    def learned_song(self):
        """
        Loops through songs list and counts all the songs that are learned and returns the count
        """
        learned_songs = 0
        for song in self.songs:
            if song[0].status == 'n':
                learned_songs += 1
        return learned_songs

    def sort(self, sort_method):
        """
            Sort the list based on user spinner selection primarily then by the title
        """
        if sort_method == "Artist":
            self.songs.sort(key=lambda i: (i[0].artist, i[0].title))
        elif sort_method == "Title":
            self.songs.sort(key=lambda i: i[0].title)
        elif sort_method == "Year":
            self.songs.sort(key=lambda i: (i[0].year, i[0].title))

    def load_songs(self):
        """
            load songs from songs.csv and create a Song object for each song
        """
        readfile = open('songs', 'r')
        for song in readfile:
            song_string = song.split(",")
            self.songs.append(
                [Song(song_string[0], song_string[1], int(song_string[2]), song_string[3].strip())])
        readfile.close()

    def save_song(self):
        """
            saves all the changes made by the user to songs.csv file
        """
        writefile = open('songs', 'w')
        for song in self.songs:
            writefile.write(
                song[0].title + "," + song[0].artist + "," + str(song[0].year) + "," + song[
                    0].status + "\n")

        writefile.close()

