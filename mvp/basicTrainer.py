from communication import ArduinoInterface
import numpy as np
import readchar

# right_hand_index_to_string = {
#     0: "Thumb",
#     1: "Index",
#     2: "Middle",
#     3: "Ring",
#     4: "Pinky",
# }

hand_index_to_string = {
    0: "Left Thumb",
    1: "Left Index",
    2: "Left Middle",
    3: "Left Ring",
    4: "Left Pinky",
    5: "Right Thumb",
    6: "Right Index",
    7: "Right Middle",
    8: "Right Ring",
    9: "Right Pinky",
}


values = {}


def setupArduinos():
    # right_hand_arduino = ArduinoInterface()

    # return None, right_hand_arduino

    glove_arduino = ArduinoInterface()
    return glove_arduino


def print_values(resistance_values):
    for index, label in hand_index_to_string.items():
        print(f"{label}: {resistance_values[index]}")


def get_input():
    # key = input("Enter a key: ")
    # key = readchar.readchar()
    key = readchar.readchar().decode('ascii')
    print("\nRead " + key)

    return key


def get_prediction(resistance_values):
    min_ = float("inf")
    pred_key = None

    for key, (averaged, _) in values.items():
        diff = np.linalg.norm(resistance_values - averaged)

        if diff < min_:
            pred_key = key
            min_ = diff

    return pred_key


def update_training_data(key, resistance_values):
    if key.upper() in values:
        current_avg, num = values[key.upper()]
        values[key.upper()] = (
            ((num * current_avg) + resistance_values) / (num + 1), (num + 1))
    else:
        values[key.upper()] = (resistance_values, 1)


# def loop(left_hand_arduino, right_hand_arduino):
def loop(glove_arduino):
    key = get_input()

    resistance_values = glove_arduino.get_resistance_values()
    prediction = get_prediction(resistance_values)
    print(f"Prediction: {prediction}")
    update_training_data(key, resistance_values)


def main():
    # left_hand_arduino, right_hand_arduino = setupArduinos()
    glove_arduino = setupArduinos()

    while 1:
        # loop(left_hand_arduino, right_hand_arduino)
        loop(glove_arduino)
    print("Training Completed")


if __name__ == "__main__":
    main()
