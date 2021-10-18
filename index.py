import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
from google.cloud import translate_v2 as translate
#export GOOGLE_APPLICATION_CREDENTIALS="/mnt/f/lyrics_collection/lyrics-collection-key.json"


file = open("artists_genius_a.txt", "a")  # File to write lyrics to
genius = lg.Genius('aTh-Dc2WaOTlLdHP5p7xV_YpLke-MQvY9Ux_nfg68IcGikRld8yJZfIwSv6794L1',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True, timeout=30)


artists3 = ["arash","嵐 (arashi) & r3hab","arca","arca & sia","arch enemy","architects","archive","archspire","arcángel","arcángel & bad bunny","ard adz","ardhito pramono","ardn","area21","a-reece","a-reece & jay jody and blue tape","ares","ariana grande & doja cat","ariana grande & justin bieber","ariana grande & nathan sykes","ariana grande & social house","ariana grande & the weeknd","ariana grande & victoria monét","arianne schreiber","ariel camacho y los plebes del rancho","ariel pink","ariel pink's haunted graffiti","ariel rivera","ariel winter","aries","ariete","arijit singh","arijit singh & mithoon","arik ancelin","ari lennox","ari lennox & j. cole","ария (ariya)","arizona zervas","arkells","ark patrol","arlo guthrie","arlo parks","armaan malik","armand hammer","armand hammer & the alchemist","the armed","armin van buuren","armin van buuren & davina michelle","ar'mon & trey","army of lovers","army of the pharaohs","aronchupa","a.r. rahman","arrdee","arrested development","arrested youth","arrogant worms","arsenal fc","arsenik","çağrı sinci","arz (uk)","art","артур эскейп (arthur escape)","arthur miller","arthur nery","arthur russell","articolo 31","artigeardit","artik & asti","art school girlfriend","arttu wiskari","arya lee","asaad (saudi money)","asaf avidan - אסף אבידן","asal kolaar x ofro","asammuell","asan","asanrap","a$ap ant","a$ap mob","asap science","a$ap twelvyy","asche","asche & kollegah","asha bhosle","ashafar","ashanti","ash b","ashcoolbro","ashe","ashe 22","ashe & finneas","asher roth","asheru","ash island","ashkidd","ashland craft","ashley cooke","ashton irwin","asia","asiah","asian doll","as i lay dying","asil slang","asin","as it is","асия (asiya)","asking alexandria","asme","aspova","assassin's creed sea shanties","astrid s","astro","astrud gilberto","the ataris","ateez","ateyaba","тяжёлая атлетика (athletic music)","ati242","atif aslam","atlantic starr","​atlas","atlas genius","atmosphere","ato","șatra b.e.n.z","atreyu","atsuover","atta boy","attack attack!","at the drive-in","attic abasement","attila","the aubreys","audio88 & yassin","audrey assad","audrey hepburn","audrey mika","audrey nuna","audrey nuna & niki","august","august alsina","august burns red","augustine","аукцыон (auktyon)","auli'i cravalho","au/ra","aurelio voltaire","auri","aurora","austin george","austin mahone","autem, bushido zho & 163onmyneck","autoheart","autumn!","av","the avalanches","avant","avantasia","avatar","avatar: the last airbender","avega","avelino","aventura & bad bunny","avery lynch","the avett brothers","aviators","avi(pl) x louis villain","aviva","a-wall","​awfultune","awkwafina","awolnation","axcx","axos","axwell λ ingrosso","aya nakamura","ayax","ayax y prok","ayo & teo","​ayokay","ayra starr","ayreon","ayushmann khurrana","ayzha nyree","az","azaan sami khan","azad","azahriah","azchike","azealia banks","azer bülbül","azet","azet & albi","azet & jugglerz","azizi gibson","azteca","azzi memo"]

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
            test_song_lyric = test_songs[0].lyrics.split("\n")[0]
            result = translate_client.detect_language(test_song_lyric)
            print(test_song_lyric)
            print(result)
            if(result["language"] == "en"):
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
get_lyrics(artists3, 100)

#const artistsWithA = Array.from(document.querySelectorAll("#main > ul.artists_index_list > li > a"))
#JSON.stringify(artistsWithA.map(artist => artist.innerText))