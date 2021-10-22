import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
from google.cloud import translate_v2 as translate
#export GOOGLE_APPLICATION_CREDENTIALS="/mnt/f/lyrics_collection/lyrics-collection-key.json"


file = open("artists_genius_b.txt", "a")  # File to write lyrics to
genius = lg.Genius('aTh-Dc2WaOTlLdHP5p7xV_YpLke-MQvY9Ux_nfg68IcGikRld8yJZfIwSv6794L1',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True, timeout=30)


artistsb1 = ["burry soprano","burt bacharach","bury tomorrow","burzum","busdriver","bush","bu$hi","bushido","bushido & shindy","bushido zho","busta rhymes","busted","buster","busy signal","buta","butrint imeri","butrint imeri, kida & ledri vula","батерс (butters)","the buttertones","butthole surfers","the buttress","бутырка (butyrka)","buzzcocks","bvcovia","bvdlvd","bway yungy","b*witched","by индия (by india)","büyük ev ablukada","b young"]

def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in 
    translate_client = translate.Client()
    c = 0  # Counter
    for name in arr:
        try:
            # To fetch by popularity too and then merge the lists
            # songsByTitle = (genius.search_artist(name, max_songs=k, sort='title')).songs
            # songsAll = list(songs)
            # for i in songsByTitle:
            #     if not any(x.id == i.id for x in songs):
            #         songsAll.append(i)
            # s = [song.lyrics for song in songsAll]

            test_songs = (genius.search_artist(name, max_songs=1, sort='popularity')).songs
            test_song_lyric = test_songs[0].lyrics.split("\n")
            result0 = translate_client.detect_language(test_song_lyric[0])
            result1 = translate_client.detect_language(test_song_lyric[1])
            isEnglish = result0["language"] == "en" and result1["language"] == "en"
            print(test_song_lyric[0], test_song_lyric[1], isEnglish)
            if(isEnglish):
                songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
                s = [song.lyrics for song in songs]
                file.write(f"\n \n   <| Song By {name} |>   \n \n".join(s))  # Deliminator
                c += 1
                print(f"Songs grabbed:{len(s)}")
        except Exception as inst:  #  Broad catch which will give us the name of artist and song that threw the exception
            print(type(inst))
            print(inst.args)
            print(inst)
            print(f"some exception at {name}: {c}")


# get_lyrics(artists, 75)
get_lyrics(artistsb1, 100)

#const artistsWithA = Array.from(document.querySelectorAll("#main > ul.artists_index_list > li > a"))
#JSON.stringify(artistsWithA.map(artist => artist.innerText))