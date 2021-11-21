# Football Team Foul Detection
Intro to Deep Learning Project CS492, Fall 2021, KAIST.

## Game Dataset 
In each game folder, / Dataset/SoccerNet / trim_dir / league / year / match
- '1_field_calib_ccbv.json', 
- '1_HQ.mkv', => First Half, Full Match
- '1_player_boundingbox_maskrcnn.json', 
- '1_ResNET_TF2.npy',
- '1_ResNET_TF2_PCA512.npy',
- '2_field_calib_ccbv.json',
- '2_HQ.mkv', => Second Half, Full Match
- '2_player_boundingbox_maskrcnn.json',
- '2_ResNET_TF2.npy',
- '2_ResNET_TF2_PCA512.npy',
- 'annotator.txt',
- 'Foul', => Trimmed Videos of Foul
- 'Labels-cameras.json',
- 'Labels-captioning.json',
- 'Labels-v2.json',  => Containing all events(kick-off) and which team commiting the events
- 'Labels.json',
- 'labels_event.json',  => Containing Foul, Yellow and Red card and Which team commits the foul
- 'Red card', => Trimmed Videos for Red Card
- 'video.ini', => Details about 1_HQ.mkv and 2_HQ.mkv
- 'video_with_duration.ini', => Details about 1_HQ.mkv and 2_HQ.mkv
- 'Yellow card' => Trimmed Videos of Yellow Card
 
