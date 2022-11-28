import cv2
import os
import random
import shutil


def mkbatch_folders(filepaths, in_dir, out_dir, batch_size=12):
    num_filepaths = len(filepaths)
    batch_idx = 0
    for init_idx in range(0, num_filepaths, batch_size):
        batch_idx+=1
        mkdir = "{out_dir}{batch_idx}/".format(out_dir=out_dir, batch_idx=batch_idx)
        print("creating: "+ mkdir)
        os.mkdir(mkdir)

        end_idx = min(init_idx + batch_size, num_filepaths)
        for filepath in filepaths[init_idx:end_idx]:
            shutil.copy(in_dir+filepath, mkdir+filepath)
    print("batch_folders have been created.")
    return

def shuffle_listdir(dir):
    filepaths = os.listdir(dir)
    random.shuffle(filepaths)
    return filepaths

def _func(filepath, frame):
    print("Generating "+filepath)
    cv2.imwrite(filepath, frame)
    return True

def videos2imgs(path_to_video, images_dir, sample_freq=30):
    
    filename = os.path.splitext(os.path.split(path_to_video)[1])[0]
    out_dir = os.path.join(images_dir, filename)
    if (os.path.isdir(out_dir)):
        try:
            os.rmdir(out_dir)
        except OSError as e:
            print("Error: %s : %s" % (out_dir, e.strerror))
    else:
        os.makedirs(out_dir)

    stream = cv2.VideoCapture(path_to_video)
    frame_counter = 0
    while True:
        out_filepath = os.path.join(out_dir, "{frame_counter:05d}.jpg".format(frame_counter=frame_counter))
        ret, frame = stream.read()
        key = cv2.waitKey(1)
        if ret is False or key is ord("q"): 
            break
        if frame_counter % sample_freq == 0: 
            _func(out_filepath, frame)
        frame_counter+=1
    
    print("video2img has been performed successfully.")


if __name__ == "__main__":
    
    images_dir = "images/"
    path_to_video = "raw_data/9B10_remote.mp4"
    videos2imgs(path_to_video, images_dir, 1)

    # img_filepaths = shuffle_listdir(images_dir)