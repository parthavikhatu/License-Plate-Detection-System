import cv2
import imutils
import pytesseract
import pymongo
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def process_frame(frame):
    # ... (existing code for processing the frame)
    # You should add the code to process the frame here and return the processed_frame.
    return frame

if __name__ == "__main__":
    # Open webcam for video capture (change the parameter to a specific camera index if needed)
    cap = cv2.VideoCapture(0)

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.o1kdxoq.mongodb.net/")
    db = client['license_plate']
    collection = db['license_plate_no']

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to a manageable size
        frame = imutils.resize(frame, width=500)

        # Process the frame
        processed_frame = process_frame(frame)

        # Display the processed frame
        cv2.imshow('Processed Frame', processed_frame)

        # Perform OCR on the processed image to extract the license plate text
        plate_text = pytesseract.image_to_string(processed_frame, config='--psm 6').strip()
        print("License Plate:", plate_text)

        if plate_text:
            # Save license plate and time to MongoDB
            current_time = time.time()
            data = {'License Plate': plate_text, 'Time': current_time}
            collection.insert_one(data)

        # Press 'q' to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
