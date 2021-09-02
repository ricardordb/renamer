import argparse
import glob
import sys
import os

movietypes = ("*.mkv", "*.mp4", "*.avi")

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, default="./", help="Path of movies/subtitles. Default current path")
parser.add_argument("-s", '--subtitle', default=False, action='store_true',
                    help="Subtitles names to Movie names. The default option is Movies to Subtitles")

args = parser.parse_args()

path = args.path

if __name__ == '__main__':
    if not path:
        path = ""
    subs = glob.glob(f'{path}/*.srt')
    movies = []
    for extension in movietypes:
        movies.extend(glob.glob(f'{path}/{extension}'))
    subs.sort()
    movies.sort()

if len(subs) != len(movies):
    print("Subtitle count different from movie count! Aborting...")
    sys.exit()

if args.subtitle:
    for i, name in enumerate(subs):
        newname = name[:-4] + movies[i][-4:]
        os.rename(movies[i], newname)
        print(f"{movies[i]} renamed to {newname}")
else:
    for i, name in enumerate(movies):
        newname = name[:-4] + subs[i][-4:]
        os.rename(subs[i], newname)
        print(f"{subs[i]} renamed to {newname}")

print(f"Successifully renamed {len(subs)} movies/subtitles!")




