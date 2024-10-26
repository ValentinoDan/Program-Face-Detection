import cv2

front_face = cv2.CascadeClassifier("C:\\Users\\ASUS\\OneDrive\\Dokumen\\Matkul ITB\\URO\\Tugas URO 2\\front_face.xml") # membuka file yang sudah disiapkan, yaitu front_face.xml
cam = cv2.VideoCapture(0) # 0 disini menunjukkan kamera yang digunakan adalah kamera bawaan

def face_detection(frame): # function untuk mendeteksi wajah
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # membuat frame berwarna hitam putih agar performa lebih baik, tetapi outputnya akan tetap berwarna
    faces = front_face.detectMultiScale(optimized_frame, scaleFactor=1.1, minSize=(100, 100), 
    minNeighbors = 3) # scaleFactor adalah seberapa banyak ukuran gambar dikurangi pada setiap skala gambar.
    return faces

def drawer_box(frame): # membentuk box berbentuk persegi panjang
    for x,y,w,h in face_detection(frame): # x kiri/kanan, y atas/bawah, w(width)/lebar, h(height)/tinggi
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 4) # warna yang digunakan BGR bukan RGB

def close_window(): # function untuk mematikan semua programnya ketika sudah selesai
    cam.release() # mematikan kamera dan menutup semua OpenCV windows yang terbuka
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        # Menangkap frame demi frame
        _, frame = cam.read() #membaca kamera
        drawer_box(frame)
        cv2.imshow("Face_detection", frame) # memunculkan boxnya & face_detection hanya sekedar nama

        if cv2.waitKey(1) & 0xFF == ord('q'): # program berhenti ketika user memencet tombol q
                close_window()

if __name__ == "__main__":
    main()