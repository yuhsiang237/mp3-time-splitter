import os
from moviepy import AudioFileClip

OUTPUT_DIR = 'output'

os.makedirs(OUTPUT_DIR, exist_ok=True)


def parse_time(time_str):
    """Convert HH:MM:SS format to total seconds."""
    parts = time_str.strip().split(':')
    if len(parts) != 3:
        raise ValueError("Invalid format. Please enter time as HH:MM:SS (e.g. 00:01:30)")
    hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
    return hours * 3600 + minutes * 60 + seconds


while True:
    input_path = input('Enter the path to the MP3 file: ').strip().strip('"')

    if not os.path.isfile(input_path):
        print('File not found. Please check the path and try again.')
        continue

    if not input_path.lower().endswith('.mp3'):
        print('Not an MP3 file. Please provide a valid .mp3 file path.')
        continue

    break

audio = AudioFileClip(input_path)
total_seconds = int(audio.duration)
total_h = total_seconds // 3600
total_m = (total_seconds % 3600) // 60
total_s = total_seconds % 60
print(f'File: {os.path.basename(input_path)}')
print(f'Total duration: {total_h:02d}:{total_m:02d}:{total_s:02d} ({total_seconds} seconds)')

while True:
    start_input = input('Enter start time (HH:MM:SS, e.g. 00:00:00): ')
    try:
        start_sec = parse_time(start_input)
        if start_sec < 0 or start_sec >= total_seconds:
            print(f'Start time out of range. Please enter a value between 00:00:00 and {total_h:02d}:{total_m:02d}:{total_s:02d}.')
            continue
        break
    except ValueError as e:
        print(f'Error: {e}')

while True:
    end_input = input(f'Enter end time (HH:MM:SS, e.g. {total_h:02d}:{total_m:02d}:{total_s:02d}): ')
    try:
        end_sec = parse_time(end_input)
        if end_sec <= start_sec:
            print(f'End time must be greater than start time. Please try again.')
            continue
        if end_sec > total_seconds:
            print(f'End time exceeds audio length (max {total_h:02d}:{total_m:02d}:{total_s:02d}). Please try again.')
            continue
        break
    except ValueError as e:
        print(f'Error: {e}')

base_name = os.path.splitext(os.path.basename(input_path))[0]
start_label = start_input.strip().replace(':', '-')
end_label = end_input.strip().replace(':', '-')
output_filename = f'{base_name}_{start_label}_{end_label}.mp3'
output_path = os.path.join(OUTPUT_DIR, output_filename)

print(f'Trimming: {start_input.strip()} ~ {end_input.strip()} ...')
clipped = audio.subclipped(start_sec, end_sec)
clipped.write_audiofile(output_path)
audio.close()
print(f'Saved: {output_path}')
