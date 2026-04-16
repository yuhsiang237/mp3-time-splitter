# MP3 Trimmer

Trims an MP3 audio file by specifying a start time and end time. The trimmed file is saved to the `output/` folder.

## Requirements

- Python 3.x
- moviepy v2+

## Installation

```bash
pip install moviepy
```

## Usage

1. Run the script:

```bash
python converter.py
```

2. When prompted, paste the full path to your MP3 file:

```
Enter the path to the MP3 file: C:\Users\you\music\example.mp3
```

3. The script will display the total duration of the audio file.

4. Enter the **start time** in `HH:MM:SS` format (e.g. `00:01:30`)

5. Enter the **end time** in `HH:MM:SS` format (e.g. `00:03:00`)

6. The trimmed file will be saved to the `output/` folder with the naming format:

```
<original_name>_<HH-MM-SS>_<HH-MM-SS>.mp3
```

> Example: `example_00-01-30_00-03-00.mp3`

> The `output/` folder will be created automatically if it does not exist.

## Directory Structure

```
mp3-time-splitter/
├── input/        # Place source MP3 files here
├── output/       # Trimmed MP3 files will be saved here
└── converter.py
```
