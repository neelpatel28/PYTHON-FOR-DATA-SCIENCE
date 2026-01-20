class Media:
    def __init__(self):
        self.title = ""

    def get_user_input(self):
        self.title = input("Enter title: ")

    def play(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Music(Media):
    def __init__(self):
        super().__init__()
        self.artist = ""

    def get_user_input(self):
        super().get_user_input()
        while True:
            try:
                artist_input = input("Enter artist: ")
                if artist_input.isalpha():
                    self.artist = artist_input
                    break
                else:
                    print("Invalid artist name. Please enter alphabetic characters only.")
            except TypeError:
                print("Give valid name!")

    def play(self):
        return "Playing '{}' by {}".format(self.title, self.artist)


class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_to_playlist(self, song):
        try:
            if not isinstance(song, Music):
                raise TypeError("Can only add instances of Music to playlist")
            song.get_user_input()
            self.playlist.append(song)
            print("{} added to playlist".format(song.title))
        except TypeError as e:
            print(e)

    def play_songs(self):
        for song in self.playlist:
            print(song.play())

# Usage
b = True
while b:
    try:
        music_player = MusicPlayer()
        a = True
        while a:
            print(" ")
            choice = input("Want to add a song to the playlist? \nEnter y/Y to proceed or else exit: ").lower()
            if choice == "exit":
                a = False
                b = False
                break
            elif choice != 'y':
                print("\nEither y/Y or exit is only valid! Re-try ")
                break

            song = Music()
            music_player.add_to_playlist(song)

        music_player.play_songs()
    except Exception as e:
        print("An error occurred: {}".format(e))
