from flask import Flask, render_template
import os

app = Flask(__name__,template_folder='../templates',static_folder='../static')


def readfile1(music_dir, image_dir, txt_dir, music, image, txt_title, txt_lyrics):
    i = 1
    num = len(os.listdir(music_dir))
    print(music_dir)

    music_dir = "." + music_dir
    image_dir = "." + image_dir
    while i<num+1:
        music_dir = music_dir+('%d'% (i + 200)).zfill(3) + ".mp3"
        music.append(music_dir)
        #print(music_dir)
        music_dir = music_dir[:-7]

        image_dir = image_dir + ('%d' % (i + 200)).zfill(3) + ".png"
        image.append(image_dir)
        image_dir = image_dir[:-7]

        txt_dir = txt_dir + ('%d' % (i + 200)).zfill(3) + ".txt"
        f = open(txt_dir, encoding='gb18030', errors='ignore')
        txt_title.append(f.readline())
        txt_lyrics.append(f.readline()+f.readline())
        txt_dir = txt_dir[:-7]

        i = i+1

    return num


def readfile2(music_dir, image_dir, txt_dir, music, image, txt_title, txt_lyrics):
    i = 1
    num = len(os.listdir(music_dir))
    #    print('music_dir:%d' % num)

    music_dir = "." + music_dir
    image_dir = "." + image_dir
    while i<num+1:
        if i<10:
           i=i+1
        elif i<100:
            i=i+1
        elif i>99:
            music_dir = music_dir + ('%d' % i) + ".mp3"
            music.append(music_dir)
            print(music_dir)
            music_dir = music_dir[:-7]

            image_dir = image_dir + ('%d' % i) + ".png"
            image.append(image_dir)
            image_dir = image_dir[:-7]

            txt_dir = txt_dir + ('%d' % i) + ".txt"
            f = open(txt_dir, encoding='gb18030', errors='ignore')
            txt_title.append(f.readline())
            txt_lyrics.append(f.readline() + f.readline())
            txt_dir = txt_dir[:-7]

        i = i+1

    return num


def get_soundtrack():
    music1_dir = "./static/resource/songs/soundtrack/"
    image1_dir = "./static/resource/images/soundtrack/"
    txt1_dir = "./static/resource/txt/soundtrack/"

    music1 = []
    image1 = []
    txt1_title = []
    txt1_lyrics = []

    num_soundtrack = readfile1(music1_dir, image1_dir, txt1_dir, music1, image1, txt1_title, txt1_lyrics)
    dictionary = {
        "num1": num_soundtrack,
        "music1": music1,
        "image1": image1,
        "txt1_title": txt1_title,
        "txt1_lyrics": txt1_lyrics
    }

    return dictionary


def get_others():
    music1_dir = "./static/resource/songs/others/"
    image1_dir = "./static/resource/images/others/"
    txt1_dir = "./static/resource/txt/others/"

    music1 = []
    image1 = []
    txt1_title = []
    txt1_lyrics = []

    num_soundtrack = readfile2(music1_dir, image1_dir, txt1_dir, music1, image1, txt1_title, txt1_lyrics)
    dictionary = {
        "num1": num_soundtrack,
        "music1": music1,
        "image1": image1,
        "txt1_title": txt1_title,
        "txt1_lyrics": txt1_lyrics
    }

    return dictionary

def return_dictionary(d):
    #    d = get_soundtrack()

    musiclist = d['music1']
    imagelist = d['image1']
    txtitlelist = d['txt1_title']
    txlyricslist = d['txt1_lyrics']
    num = len(txtitlelist)
    print('num:%d' % num)

    cd = []
    i = 0
    onesong = {}
    while i<num:

        onesong = {'id': i, 'musicscr': musiclist[i], 'image': imagelist[i], 'title': txtitlelist[i], 'lyrics': txlyricslist[i]}
        cd.append(onesong)
        print(onesong['image'])
        i = i + 1

    print('CD size:%d' % len(cd))
    return cd


@app.route('/')
def index():
    general_data = {'title': 'Music Player'}
    stream_entries1 = return_dictionary(get_soundtrack())
    stream_entries2 = return_dictionary(get_others())
#    for e in stream_entries1:
#       print(e)

    return render_template('index.html', entries1=stream_entries1, entries2=stream_entries2, **general_data)


if __name__ == '__main__':
    app.run()
