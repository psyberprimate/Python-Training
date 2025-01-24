

class Song:
    """Class to represent a song

    Attributs:
    title {str} : The title of the song
    artist {Artist}: An artist object representing the songs creater.
    duration {int}: The duration of the song in seconds. Maybe be zero
    """    
    def __init__(self, title : str, artist, duration : float = 0  ):
        """Song init method
        Args:
            title (str): Initializes the 'title' attribute
            artist (_type_): Artist object representing the song's creator
            duration (float, optional): Initial value of the 'duration' attribute, defaults to zero.
        """        
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
    album_name (str) : Name of the album
    artist: (Artist): The artist responsible for the album. If not specified, the artist will defualt to an artist with anem "Various Artists".
    tracks (List[Song]: A list of the songs on the Album)
    """    
    def __init__(self, album_name : str, year : int, artist=None):
        self.name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = [] 

    def add_song(self, song : Song, position : int = None):
        """Adds a song to the track list

        Args:
            song (Song): _description_
            position (int, optional): _description_. Defaults to None.
        """        
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)    


class Artist:
    """Basic class to sotre artist detials.

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

def find_object(field : str, object_list : list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exitsts, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None    
    print()


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("Section10 - Object Oriented Python/albums.txt", "r") as albums:
        for line in albums:
            #print(line)
            #data row should consist of (artist, album, year, song)
            artist, album, year, song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            print(f"{artist} : {album} : {year} : {song}")
            
            if new_artist is None:
                new_artist = Artist(artist)
                artist_list.append(new_artist)
            elif new_artist.name != artist:
                #Just reads details for a new artist
                #retrieve the artist object if there is one, otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album, year, new_artist)   
                new_artist.add_album(new_album)
            elif new_album.name != album:
                #Just read a new album for the current artist
                #Retrieve the album object if there is one, otherwise create a new album object and sotre it in the artist's collection.
                new_album = find_object(album, new_artist.albums)
                if new_album is None:
                    new_album = Album(album, year, artist)
                    new_artist.add_album(new_album)

            #create a new song object and add it to the current album's collection
            new_song = Song(song, new_artist)
            new_album.add_song(new_song)

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