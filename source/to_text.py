import os
import whisper

input_directory = "your_input_file_here"
output_directory = "your_output_path_here"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

model = whisper.load_model("medium")
language = "en"

mp3_files = [f for f in os.listdir(input_directory) if f.endswith('.mp3')]
i = 1

# Process each mp3 file and generate an text file
for mp3_file in mp3_files:
    input_file = os.path.join(input_directory, mp3_file)
    result = model.transcribe(input_file)
    output_file_name = os.path.splitext(mp3_file)[0] + ".txt"
    output_file_path = os.path.join(output_directory, output_file_name)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(result["text"])
    print(result["text"])
    print(f"Transcription saved for: {mp3_file}")
    print(f"video {i} has completed!")
    i += 1
