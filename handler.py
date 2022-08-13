from crawler import *


def run():
    home_page = get_page('https://musictarin.com/')
    singers = get_all_singers(home_page)

    # STORE AND FORMAT SINGERS IN A LIST WITH (ID, NAME, LINK)
    for singer in singers:
        singer_id = singers.index(singer)
        singer_name = str(singer).split(sep='">')[1].split(sep='</a>')[0]
        singer_link = singer.get('href')
        singers_list.append((singer_id, singer_name, singer_link))

    # SHOW ALL SINGERS TO USER AND WAIT FOR USER CHOICE
    for item in singers_list:
        print(f'{item[0]}:{item[1]}')

    user_input = int(input("Please enter singer ID: "))
    chosen_singer = get_page(singers_list[user_input][2])
    all_musics = get_singer_musics(chosen_singer)

    # PASS EACH SONG FROM SINGER TO (def fetch_data) FOR GET AND SAVE INFO
    for music in all_musics:
        song_page = get_page(music)
        fetch_data(song_page)

    # SHOW ALL DOWNLOAD LINKS AND TITLES
    for f in scraped_data:
        print(f)
