"""
Module to extract data from Spotify API. Given a category id, this module will extract
the data and put it into a csv file, ordered in albums' year released, artist name
and album name.
"""
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config

client_id = config('CLIENT')
secret = config('SECRET')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=secret))


def get_playlist_id_and_name_dictionary(category_id: str):
    """
    Function to return a dictionary of playlist ids and names for a given keyword (category_id)
    :param category_id: The Spotify category ID for the category. Example value "dinner"
    :return: A dictionary of (playlist id : playlist name) for a given category
    """
    results = spotify.category_playlists(category_id=category_id, limit=12)
    if not results:
        raise Exception('No values returned from Spotify API')
    else:
        playlists = results['playlists']['items']
        playlist_id_name_dict = {}
        for playlist in playlists:
            playlist_id_name_dict[playlist['id']] = playlist['name']
        return playlist_id_name_dict


def get_albums_release_year_and_name(category_id: str):
    """
    Function to a file of albums released from the playlist dictionary passed into the function.
    :param playlist_id_and_name_dict: A dictionary containing a pair of playlist id: playlist name
    :return: A csv file filled with data according to the albums dictionary
    """
    final_albums_dictionary = {
        'Year Released': [],
        'Album Name': [],
        'Artist Name': []
    }

    playlist_id_and_name_dict = get_playlist_id_and_name_dictionary(category_id)
    print(len(list(playlist_id_and_name_dict.keys())))
    with open('csv/'+category_id+'_albums_data.csv', 'w', encoding='UTF-8') as file:
        header = list(final_albums_dictionary.keys())
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        data_written = []
        for playlist_id in list(playlist_id_and_name_dict.keys()):
            playlist = spotify.playlist(playlist_id=playlist_id)
            if not playlist:
                raise Exception('No values returned from Spotify API')
            else:
                playlist_items = playlist['tracks']['items']
                for item in playlist_items:
                    key = item['track']['album']['release_date'][:4] + \
                          item['track']['album']['name'] + \
                          item['track']['artists'][0]['name']
                    if key not in data_written:
                        data_written.append(key)
                        writer.writerow({
                            'Year Released': item['track']['album']['release_date'][:4],
                            'Album Name': item['track']['album']['name'],
                            'Artist Name': item['track']['artists'][0]['name']

                        })


if __name__ == '__main__':
    get_albums_release_year_and_name('rock')
    get_albums_release_year_and_name('hiphop')
