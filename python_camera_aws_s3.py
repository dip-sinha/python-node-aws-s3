
# using conda yolov3 environment(conda activate yolov3)
# 1.install awscli (pip install awscli)
# 2. open cmd and give command aws configure --> give credentials for aws access ,save t in environment variable
# 3. install boto3
# run node.js server and change URL as per requirement
#  s3 bucket name
import boto3  # install : pip install boto3
import json
import cv2

key = cv2.waitKey(1)
from time import sleep
webcam = cv2.VideoCapture(1)  # change this number according to webcam connected in to the system
#r = requests.get('http://localhost:8081/flash').json()
#response = (r.get('res'))
#print(response)
sleep(3)
while True:
    try:
        check, frame = webcam.read()
        # print(check) #prints true as long as the webcam is running
        # print(frame) #prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        if check == True:
            sleep(3)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Image saved!")
            S3 = boto3.client('s3')
            SOURCE_FILENAME = 'saved_img.jpg'
            BUCKET_NAME = 'santa-claus'
            print('sending file to aws s3 bucket')
            # Uploads the given file using a managed uploader, which will split up large
            # files automatically and upload parts in parallel.
            S3.upload_file(SOURCE_FILENAME, BUCKET_NAME, SOURCE_FILENAME)
            print('sent!!')
            break
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
