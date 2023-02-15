import webvtt
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def get_wpm(vtt):
    words = 0
    time = timedelta(0)
    for caption in vtt:
        words += len(caption.text.split())
        end = datetime.strptime(caption.end, "%H:%M:%S.%f")
        start = datetime.strptime(caption.start, "%H:%M:%S.%f")
        time += end - start
    return words / (time.total_seconds() / 60)


def plot_wpm(vtt):
    wpm = []
    for caption in vtt:
        words = len(caption.text.split())
        end = datetime.strptime(caption.end, "%H:%M:%S.%f")
        start = datetime.strptime(caption.start, "%H:%M:%S.%f")
        time = end - start
        wpm.append(words / (time.total_seconds() / 60))
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.ylabel("Words per minute")
    plt.xlabel("Caption")
    plt.show()


def main():
    vtt = webvtt.read("../transcriptions/transcription-english.vtt")
    print(get_wpm(vtt))
    plot_wpm(vtt)


if __name__ == "__main__":
    main()
