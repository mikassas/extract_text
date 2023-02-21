import moviepy.editor
from pathlib import Path


def get_audio(path):

  video_file = Path("path to video")

  video = moviepy.editor.VideoFileClip(f'{video_file}')
  audio = video.audio()
  audio.write_audiofile(f'{video.file.stem}.mp3')
 

def main():
  path = input("enter path to video: ")
  get_audio(path)


if __name__ == "__main__":
  main()
  
