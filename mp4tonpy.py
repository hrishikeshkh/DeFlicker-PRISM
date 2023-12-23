from moviepy.editor import VideoFileClip
import numpy as np

# Replace 'your_video.mp4' with the actual filename
video_path = 'E:\shootout.mp4'
output_npy_path = 'output6.npy'

# Load the video clip
video_clip = VideoFileClip(video_path)

# Convert the video frames to a NumPy array
video_array = np.array([frame for frame in video_clip.iter_frames()])

# Save the NumPy array to a .npy file
np.save(output_npy_path, video_array)