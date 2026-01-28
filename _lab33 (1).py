import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Read all frames first (store in list)
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Total frames
total = len(frames)

# Play forward and reverse
index_forward = 0
index_reverse = total - 1

while True:
    # Forward frame
    if index_forward < total:
        cv2.imshow("Original Video (Forward)", frames[index_forward])
        index_forward += 1

    # Reverse frame
    if index_reverse >= 0:
        cv2.imshow("Reverse Video", frames[index_reverse])
        index_reverse -= 1

    # Quit on 'q'
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

