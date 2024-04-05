from moviepy.editor import *

name = 'D:\VScode\home\Movie 01_ori.mp4'
name2 = 'D:\VScode\home\Movie 01.mp4'
au = VideoFileClip(name)
new_au = au.fl_time(lambda t:  0.2*t, apply_to=['mask', 'audio'])
new_au = new_au.set_duration(au.duration/0.2)
new_au.write_videofile(name2)