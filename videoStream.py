import cv2


def stream_video(video_feed: bool, image_path: str):
    if video_feed:
        cam = cv2.VideoCapture(0)

    while True:
        if video_feed:
            _, frame = cam.read()
        else:
            frame = cv2.imread(image_path)

        cv2.imshow("Food scanner camera", frame)

        if not video_feed:
            print('Click "0" when done')
            cv2.waitKey(0)
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit if 'q' is pressed
            break
    
    if video_feed:
        cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    live_feed = True
    image_path = '/path/to/image'
    stream_video(live_feed, image_path)
