"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song
from operator import attrgetter

# test empty SongList
song_list = SongList()
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
assert len(song_list.songs) > 0  # assuming CSV file is not empty
print(song_list)
# test get number of songs to learn
print("Number of songs to learn = ", song_list.get_number_required())


# test sorting songs
#song_list.sort_list(song_list.songs[0].title)
song_list.sort_list("Required")
print('\n\n', song_list)
# test adding a new Song
song_list.add_song("Here and Now","Someone",1981,False)
print(song_list)
# test get_song()

# test getting the number of required and learned songs (separately)
print("Number of songs learnt = ", song_list.get_number_learned())
# test saving songs (check CSV file manually to see results)
song_list.save_songs("songs.csv")
