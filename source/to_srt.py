import os
import whisper
from whisper.utils import get_writer

input_directory = "your_input_path_here"
output_directory = "your_output_path_here"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

model = whisper.load_model("medium")  # or whatever model you prefer
language = "zh" # or whatever language of your audios

mp3_files = [f for f in os.listdir(input_directory) if f.endswith('.mp3')]
i = 1
# Process each mp3 file and generate an SRT file
for mp3_file in mp3_files:
    input_file = os.path.join(input_directory, mp3_file)
    result = model.transcribe(input_file, fp16=False)

    srt_filename = os.path.splitext(input_file)[0] + ".srt"
    output_file = os.path.join(output_directory, srt_filename)

    srt_writer = get_writer("srt", output_directory)
    srt_writer(result, output_file)
    print("video " + str(i) + " has completed!")
    i += 1
