import os
from moviepy.editor import *

input_directory = 'E:\\4.3'
output_directory = 'E:\\PersonalUse\\4.3'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for file in os.listdir(input_directory):
    if file.endswith('.mp4'):
        input_file = os.path.join(input_directory, file)
        output_file = os.path.join(output_directory, file.replace('.mp4', '.mp3'))

        video = VideoFileClip(input_file)
        audio = video.audio

        audio.write_audiofile(output_file)
        video.close()
        audio.close()

print("Audio extraction completed!")
