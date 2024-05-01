# VideoExtender

## Overview

VideoExtender is a Python script that extends the duration of a video file to a specified number of hours by repeating its content. It is ideal for creating extended loops of short videos.

## Requirements

- Python 3.x
- `ffmpeg` and `ffprobe` installed on your system. You can install these with a package manager like `apt` for Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/annaelmoussa/VideoExtender.git
cd VideoExtender
```

## Usage

Run the script from the command line by specifying the input video file, the output video file, and the desired duration in hours:

```bash
python3 VideoExtender.py <input_video.mp4> <output_video.mp4> <hours>
```

Example:

```bash
python3 VideoExtender.py video_original.mp4 video_extended.mp4 10
```

## How It Works

The script calculates how many times the original video needs to be repeated to reach approximately the specified duration. It then creates a video that loops the original content until the target duration is met.

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This work is [licensed](LICENSE) under the Creative Commons Attribution-NonCommercial 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
