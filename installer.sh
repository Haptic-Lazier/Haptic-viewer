pip3 install time
pip3 install os
pip3 install praw
pip3 install shutil

mkdir Haptic_viewer/pic_gif_output/Pictures
mkdir Haptic_viewer/pic_gif_output/Gifs
mkdir Haptic_viewer/pic_gif_output/Texts

wget -qO Haptic_viewer/ https://github.com/Haptic-Lazier/Haptic-veiwer/blob/main/haptic_go.py
wget -qO Haptic_viewer/ https://github.com/Haptic-Lazier/Haptic-veiwer/blob/main/cred.py

echo "Install Complete, type 'cd Haptic_viewer/cred.py' to configure the bot to get started!"
