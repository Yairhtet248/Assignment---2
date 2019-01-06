"""
Name: YairHtet
Date:27/1/2018
Brief Project Description:
A program that keeps a record of songs the user has learnt
and a record of songs to learn
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from songlist import SongList

background_color = [0, 69, 0, 0.3]
Background_Color = [0, 78, 80, 0.3]
class SongsList(App):
    def build(self):
        """
            Building kivy app and setting up Song objects
        """
        self.title = "Songs To Learn 2.0 by Oakgar Ziwa"
        self.root = Builder.load_file('app.kv')
        self.song_list.load_songs()
        self.song_list.sort('Artist')
        self.build_left_layout()
        self.build_right_layout()
        return self.root

    def __init__(self, **kwargs):
        """
            Initializing all the required widgets for left layout for kivy app.
        """
        super().__init__(**kwargs)
        self.song_list = SongList()

        # Top count label and bottom status label
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")

        # Left layout widgets
        self.sort_label = Label(text="Sort By:")
        # Setting Artist as default sort method
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year'))
        self.add_song_label = Label(text="Add New Song!", )
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)

        # Button widgets to handle add and clear
        self.add_song_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

    #Creating left layout based on widgets created in a particular order
    def build_left_layout(self):
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_song_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.add_song_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)

        # Setting on click for sorting spinner, add button and clear button
        self.spinner.bind(text=self.sort_songs)
        self.add_song_button.bind(on_release=self.add_song_handler)
        self.clear_button.bind(on_release=self.clear_add_song_fields)

    def sort_songs(self, *args):
        """
        This method handles on click on spinner and sorts based on that and rebuilds right layout
        """
        self.song_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_layout()

    def build_right_layout(self):
        """
            Building right layout with widgets based on the list we created.
        """
        # Sets the count label
        self.top_label.text = "To Learn: {}. Already Learned: {}".format(str(self.song_list.song_left_to_learn()),str(
            self.song_list.learned_song()))

        # Goes through each song in the list and check if it learned or required and setts color based on that
        for song in self.song_list.songs:
            # n = Learned
            if song[0].status == 'n':
                song_button = Button(text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(
                    song[0].year) + ") " "(Learned)", id=song[0].title)

                song_button.background_color = background_color
            # y = required to learn
            else:
                song_button = Button(
                    text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(song[0].year) + ")",
                    id=song[0].title)

                song_button.background_color = Background_Color

            # Setting on click for the buttons created
            song_button.bind(on_release=self.song_learn_handler)
            self.root.ids.rightLayout.add_widget(song_button)

    def song_learn_handler(self, button):
        """
            Handles on click for each song button created
        """

        # if button user clicked is learned change it to required to learn and update the status bar
        if self.song_list.get_song(button.id).status == 'n':
            self.song_list.get_song(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "Click The Button To Learn The Songs"

        # if button user clicked is Required to learn change it to learned and update the status bar
        else:
            self.song_list.get_song(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have learned {}".format(str(self.song_list.get_song(button.id).title))

        # Update the sorting and reloads the right layout
        self.sort_songs()
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_layout()

    def clear_add_song_fields(self, *args):
        """
            Handles clearing up all the text fields and status bar
        """
        self.title_text_input.text = ""
        self.artist_text_input.text = ""
        self.year_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def add_song_handler(self, *args):
        """
            This method handles all the error checking for user input on text field and creates a Song object
        """
        # Checks if all the input fields are complete if not error text will be displayed
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:
                # If year is negative
                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Year must be >= 0"
                # If all the criteria matches it creates a Song object in song_list class
                else:
                    self.song_list.add_song(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sort(self.spinner.text)
                    self.clear_add_song_fields()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_layout()
            # String Error checking for year input
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def on_stop(self):
        # on close all the data form the list will be saved to to songs.csv file
        self.song_list.save_song()


if __name__ == '__main__':
    app = SongsList()
    app.run()
