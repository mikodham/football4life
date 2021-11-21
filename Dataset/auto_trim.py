# import subprocess as sp
import os
from pathlib import Path

# Caution: Use Virtual Environment!
# command = "python test.py a b c"
# cmd = 'cmd /c ' + command
# os.system(cmd)

root = os.getcwd()
labels_dir = Path(root + "/SoccerNet")

leagues_list = os.listdir(labels_dir)
Override = False  # Override: whether the new trim replaces the old trimmed videos
for league in leagues_list:
    years_list = os.listdir(labels_dir / league)
    for year in years_list:
        matches_list = os.listdir(labels_dir / league / year)
        for match in matches_list:
            match_dir = labels_dir / league / year / match
            # If match is already trimmed, skip match
            # If video 1HQ.mkv doesn't exist, or skip match
            files = os.listdir(match_dir)
            # print(match_dir)
            if (Override is False and "Foul" in files) or "1_HQ.mkv" not in files or "2_HQ.mkv" not in files:
                # not override, full match are in the match_dir
                continue
            # Trim
            # print(match_dir, "Trim")
            command = "python trimmer.py %s %s %s" % (league, year, match)
            cmd = 'cmd /c ' + command
            print(cmd)
            os.system(cmd)
