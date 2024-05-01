import subprocess
import sys
import os

def check_file_exists(file_path):
    """Check if the file exists to avoid errors during processing."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified file does not exist: {file_path}")

def get_video_duration(input_video_path):
    """Retrieve the duration of the video using ffprobe."""
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video_path]
    process = subprocess.run(cmd, text=True, capture_output=True, check=True)
    if process.returncode != 0:
        raise Exception("Failed to obtain the video duration using ffprobe.")
    return float(process.stdout.strip())

def extend_video_ffmpeg(input_video_path, output_video_path, target_duration_hours):
    check_file_exists(input_video_path)
    original_duration = get_video_duration(input_video_path)
    
    target_duration_seconds = target_duration_hours * 3600
    repeat_count = target_duration_seconds // original_duration
    total_duration = repeat_count * original_duration
    
    if total_duration < target_duration_seconds:
        repeat_count += 1
    
    with open("filelist.txt", "w") as file:
        for _ in range(int(repeat_count)):
            file.write(f"file '{input_video_path}'\n")
    
    concat_cmd = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', 
        '-t', str(target_duration_seconds), '-y', output_video_path
    ]
    subprocess.run(concat_cmd, check=True)
    
    os.remove("filelist.txt")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py original_video.mp4 extended_video.mp4 10")
        sys.exit(1)

    input_video = sys.argv[1]
    output_video = sys.argv[2]
    hours = int(sys.argv[3])

    try:
        extend_video_ffmpeg(input_video, output_video, hours)
        print("Video successfully extended.")
    except Exception as e:
        print(f"Error extending the video: {e}")
