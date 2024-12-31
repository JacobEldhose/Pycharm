import cv2

video_path = cv2.VideoCapture("D:\\Luminar\\DL\\Open-cv\\mh.mp4")

cv2.rectangle(video_path,pt1=(400,300),pt2=(100,200),color=(255,255,0),thickness=cv2.FILLED)
cv2.circle(video_path,center=(350,250),radius=50,color=(255,51,255),thickness=cv2.FILLED)
cv2.putText(
    video_path,
    text="luminar",
    org=(250,300),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(0,0,0),
    thickness= 2)
while True:
    success , frame = video_path.read()
    print(success)
    cv2.rectangle(frame,pt1=(400,300),pt2=(100,200),color=(255,255,0),thickness=cv2.FILLED)
    cv2.circle(frame,center=(350,250),radius=50,color=(255,51,255),thickness=cv2.FILLED)
    cv2.putText(
        frame,
        text="luminar",
        org=(250,300),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=1,
        color=(0,0,0),
        thickness= 2)
    if success ==False:
        break
    print(frame.shape)
    cv2.imshow("Video Display",frame)
    if cv2.waitKey(50) & 0XFF == 27:
        break

# cv2.putText(video_path,
#             text="Helloo..",
#             org=)
