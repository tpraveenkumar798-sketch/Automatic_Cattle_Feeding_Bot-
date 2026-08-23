import cv2
import numpy as np
import time
from gpiozero import Motor, Servo
import tflite_runtime.interpreter as tflite

# ---------------- MOTOR ----------------
left_motor = Motor(forward=5, backward=6)
right_motor = Motor(forward=20, backward=21)

def forward():
    left_motor.forward()
    right_motor.forward()

def reverse():
    left_motor.backward()
    right_motor.backward()

def stop():
    left_motor.stop()
    right_motor.stop()


# ---------------- SERVO ----------------
servo = Servo(19)

def servo_action():
    print("🐄 Cow detected")

    stop()

    # Open feeder
    servo.max()      # 90°
    time.sleep(3)

    # Close feeder
    servo.min()      # 0°
    time.sleep(1)

    # Continue moving
    forward()
    moving_time_start()


# ---------------- TIMER ----------------
moving_time = 0
start_move = None

def moving_time_start():
    global start_move
    start_move = time.time()

def moving_time_stop():
    global moving_time, start_move

    if start_move is not None:
        moving_time += time.time() - start_move
        start_move = None


# ---------------- MODEL ----------------
interpreter = tflite.Interpreter(
    model_path="model.tflite"
)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)


# ---------------- VARIABLES ----------------
cow_count = 0
MAX_COWS = 4
cooldown = 0

print("🚤 Robot Started")

forward()
moving_time_start()

# ---------------- MAIN LOOP ----------------
while True:

    ret, frame = cap.read()

    if not ret:
        continue

    # Show live camera
    cv2.imshow("Final Robot", frame)

    # Prepare image
    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img.astype(np.float32) / 255.0

    # AI prediction
    interpreter.set_tensor(
        input_details[0]['index'],
        img
    )

    interpreter.invoke()

    output = interpreter.get_tensor(
        output_details[0]['index']
    )

    confidence = np.max(output)
    label = np.argmax(output)

    print(
        f"Label:{label}  Confidence:{confidence:.2f}"
    )

    # ---------------- COW DETECTION ----------------
    if (
        label == 0
        and confidence > 0.90
        and cooldown == 0
        and cow_count < MAX_COWS
    ):

        cow_count += 1

        print(f"🐄 Cow {cow_count}")

        moving_time_stop()

        servo_action()

        cooldown = 50

    # ---------------- RETURN CONDITION ----------------
    if cow_count >= MAX_COWS:

        print("🔁 Returning Back")

        moving_time_stop()

        print(
            f"Forward Time: {moving_time:.2f} sec"
        )

        stop()
        time.sleep(1)

        reverse()
        time.sleep(moving_time)

        stop()

        print("✅ Perfect Return Completed")

        break

    # ---------------- NORMAL MOVEMENT ----------------
    if cooldown == 0:
        forward()
    else:
        cooldown -= 1

    # Press ESC to stop
    if cv2.waitKey(1) & 0xFF == 27:
        break


# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()

stop()
servo.min()

print("🚤 Program Ended")