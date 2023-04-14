import os
from moviepy.editor import *
#to run this script you need moviepy library

input_directory = 'your_mp4_file_path'
output_directory = 'your_output_file_path'

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
