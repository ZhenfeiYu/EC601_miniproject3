import audio_visual
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run = audio_visual.AudioVisualize()
        typed = sys.argv[1]
        if typed == '1d':
            run.audio_visualize_1d()
        elif typed == '2d':
            run.audio_visualize_2d()
    else:
        print('run.py [options](1d | 2d)')