# Download yolo repo
echo "Downloading YOLO repo"
git clone https://github.com/qqwweee/keras-yolo3.git
mv keras-yolo3 keras_yolo3

# Copy replacement files
echo "Replacing files"
mv src/yolo_replacement.py keras_yolo3/yolo.py
sed -i 's/yolo3.utils/keras_yolo3.yolo3.utils/g' keras_yolo3/yolo3/model.py

# Download pre-trained weights
echo "Downloading pre-trained weights"
cd keras_yolo3
wget https://pjreddie.com/media/files/yolov3-tiny.weights

# Convert model to keras
echo "Converting model to Keras"
python convert.py yolov3-tiny.cfg yolov3-tiny.weights model_data/tiny_yolo.h5
