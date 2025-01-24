

class Song:
    """Class to represent a song

    Attributs:
    title {str} : The title of the song
    artist {Artist}: An artist object representing the songs creater.
    duration {int}: The duration of the song in seconds. Maybe be zero
    """    
    def __init__(self, title : str, artist : str, duration : float = 0  ):
        """Song init method
        Args:
            title (str): Initializes the 'title' attribute
            artist (str): Name of the song's creator
            duration (float, optional): Initial value of the 'duration' attribute, defaults to zero.
        """        
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)    


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
    album_name (str) : Name of the album
    artist: (str): The artist responsible for the album. If not specified, the artist will defualt to an artist with anem "Various Artists".
    tracks (List[Song]: A list of the songs on the Album)
    """    
    def __init__(self, album_name : str, year : int, artist=None):
        self.name = album_name
        self.year = year

        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = [] 

    def add_song(self, song : Song, position : int = None):
        """Adds a song to the track list

        Args:
            song (Song): The title of a song to add
            position (int, optional): _description_. Defaults to None.
        """  
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)   
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)    


class Artist:
    """Basic class to for the artist details.

    Attributes:
    name (str): The name of the artist.
    albums (List[Album]): A list of the albums by this artist. The list includes only those albums inthis collection, it is
    not an exhaustive list of the aritst's albums.

    Methods:
        add_album: Use to add a new album oto the artist's albums list
    """    
    def __init__(self, name : str):
        self.name = name
        self.albums = []

    def add_album(self, album : Album):
        """Add a new album to the list.

        Args:
        album (Album): Album object to add to the list.
        if the album is already present, it will not be added again.

        Args:
            album (Album): _description_
        """        
        self.albums.append(album)

    def add_song(self, name : str, year : int, title : str):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doens't already exist.

        Args:
            name (str): The name of the album
            year (int): The year  the album was produced
            title (str): The title of the song
        """     
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(f"{name} not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print(f"Found album {name}")
        album_found.add_song(title)       

def find_object(field : str, object_list : list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exitsts, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None    


def load_data():
    artist_list = []

    with open("Section10 - Object Oriented Python/albums.txt", "r") as albums:
        for line in albums:
            #print(line)
            #data row should consist of (artist, album, year, song)
            artist, album, year, song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            print(f"{artist} : {album} : {year} : {song}")
            
            new_artist = find_object(artist, artist_list)
            if new_artist is None:
                new_artist = Artist(artist)
                artist_list.append(new_artist)

            new_artist.add_song(album, year, song)    

        #After reading a last line of the text file, we will have an artist that haven't been stored -> do it now
    return artist_list


def create_checkfile(artist_list):
    """Create a check fiel from the object data for comparison with the original file"""    
    with open("Section10 - Object Oriented Python/checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == '__main__':

    print("LOADING DATA")
    artists = load_data()
    print("There are {} artist".format(len(artists)))
    create_checkfile(artists)