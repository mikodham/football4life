from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# from moviepy.editor
from pathlib import Path
import configparser
import os
import json
# import re
import pickle
import sys

# JSON
# get type/class, Foul, etc
# get start_time, end_time

# Chelsea-Burnley
# 22.25, actual 27.42
# 5:15 KICK-OFF, how to get this data


def conv_min2sec(string):
    """convert minutes to second"""
    minutes, seconds = string.split(":")
    return int(minutes)*60+int(seconds)


def get_kickoff(dir):
    """return seconds of the video (1st half kickoff, 2nd half kickoff)"""
    print(dir)
    os.open(dir, os.O_RDONLY)
    config = configparser.ConfigParser()
    config.read(dir)
    return int(float(config['1_HQ.mkv']['start_time_second'])), (float(config['2_HQ.mkv']['start_time_second']))


# init
root = os.getcwd()
parent = Path(root + "/Dataset/SoccerNet")
# video_dir = Path(root + "/Dataset/Videos")
# labels_dir = Path(root + "/Dataset/Labels")
# trim_dir = Path(root + "/Dataset/Trimmed_Videos")
video_dir, labels_dir, trim_dir = parent, parent, parent

if __name__ == "__main__":
    league = 'england_epl'
    year = '2014-2015'
    match = '2015-05-17 - 18-00 Manchester United 1 - 1 Arsenal'  #'2015-02-21 - 18-00 Chelsea 1 - 1 Burnley'

    if len(sys.argv) == 4:
        league, year, match = sys.argv[1:]
    # leagues_list = os.listdir(labels_dir / 'SoccerNet_V1.1_Labels')
    # years_list = os.listdir(labels_dir / 'SoccerNet_V1.1_Labels' / league)
    # matches_list = os.listdir(labels_dir / 'SoccerNet_V1.1_Labels' / league / year)

    match_dir = video_dir / league / year / match
    class_dir = labels_dir / league / year / match

    # get fouls+yellow_card
    file = open(class_dir / "Labels-v2.json", )
    data = json.load(file)
    annots = data['annotations']
    labels_save = []
    for each in annots:
        temp = each['label']
        if "Foul" in temp or "card" in temp:
            labels_save.append(each)
    file.close()

    temp = trim_dir / league / year / match
    if not os.path.exists(temp):
        os.makedirs(temp)
    # print("hello")
    with open(temp / 'labels.json', "w") as fp:
        json.dump(labels_save, fp, indent=2)

    with open(temp / 'labels.json', "r") as fp:
        labels_load = json.load(fp)

    print(len(labels_load), labels_load)
    # get kick_off time from video.ini!!
    first_half, second_half = get_kickoff(match_dir / 'video.ini')

    for label in labels_load:
        # if label['label'] == 'Foul':
        saved_dir = trim_dir / league / year / match / label['label']
        if not os.path.exists(saved_dir):
            os.makedirs(saved_dir)
        HALF, event_time = label['gameTime'].split(" - ")
        full_match_dir = match_dir / (HALF + '_HQ.mkv')
        event_time = conv_min2sec(event_time)
        if HALF == "1":
            kickoff = first_half
        else:  # HALF == "2"
            kickoff = second_half

        # Modify the tolerance!
        start_time, end_time = event_time - 15 + kickoff, event_time + 15+ kickoff
        filename = label['gameTime'].replace(":", "_")
        print(full_match_dir, start_time, end_time, saved_dir / (filename + '.mp4'))
        ffmpeg_extract_subclip(full_match_dir, start_time, end_time, targetname=saved_dir / (filename + '.mkv') )
# ffmpeg -progress pipe:1 -hide_banner -i /path/to/file.mkv -map 0:v
# -map 0:a -map 0:s -c:a aac -c:v copy -c:s mov_text /path/to/outfile.mp4
