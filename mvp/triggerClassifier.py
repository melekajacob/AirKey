from communication import ArduinoInterface
import numpy as np
import readchar
import collections
import matplotlib.pyplot as plt
import time

stillTraining = "Y"  # "Y" is for training, anything else for prediction
first = True  # always keep this true


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
    10: "Lifted Fingers"
}

lastFour = collections.deque([10, 10, 10, 10])

# values = {}
outfile = 'data/sufTriggerData2.npy'
values = np.load(outfile, allow_pickle=True).item()


label = [
    'L Thumb',
    'L Index',
    'L Middle',
    'L Ring',
    'L Pinky',
    'R Thumb',
    'R Index',
    'R Middle',
    'R Ring',
    'R Pinky',
]


def plot_bar_x(resistance_values):
    index = np.arange(len(label))
    plt.bar(index, resistance_values)
    plt.xlabel('Genre', fontsize=5)
    plt.ylabel('No of Movies', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Glove Resistance Values')
    plt.pause(0.05)


def setupArduinos():
    glove_arduino = ArduinoInterface()
    return glove_arduino


def print_values(resistance_values):
    for index, label in hand_index_to_string.items():
        print(f"{label}: {resistance_values[index]}")


def get_input():
    # key = input("Enter a key: ")
    key = readchar.readchar()
    # key = key.decode('ascii')
    keyChar = key.decode('ascii')

    if(keyChar == ' '):
        return 10
    elif (keyChar < '0' or keyChar > '9'):
        return 11

    index = int(key.decode('ascii'))
    finger = hand_index_to_string[index]

    print("\nRead "+str(index) + " which is for " + finger)
    return index


def get_prediction(resistance_values, lastFour):
    global values
    pred_finger = None

    minDiff = abs(values[0][0]-resistance_values[0])
    pred_finger = 0

    for i in range(len(values)-2):
        diff = abs(values[i][i]-resistance_values[i])
        if diff < minDiff:
            minDiff = diff
            pred_finger = i

    print(minDiff)  # Uncomment this to find best min diff val
    # values[10] is not that good so let's go with threshold for now
    if minDiff >= 30 or pred_finger in lastFour:
        pred_finger = 10  # if difference is too big, it's probs lifted

    lastFour.appendleft(pred_finger)
    lastFour.pop()

    if pred_finger == 10:
        return None

    return pred_finger


def update_training_data(finger, resistance_values):
    if (finger == 10):
        minDiff = abs(values[0][0]-resistance_values[0])
        for i in range(len(values)-1):
            diff = abs(values[i][i]-resistance_values[i])
            if diff < minDiff:
                minDiff = diff

        # print("Min diff = " + str(minDiff))
        values[finger] = minDiff
    else:
        values[finger] = resistance_values
    np.save(outfile, values)


def loop(glove_arduino):
    global stillTraining
    global lastFour
    global values
    global first

    if stillTraining == "Y":
        finger_index = get_input()
        # print(finger_index)

        if finger_index > 10:
            first = False
            plt.cla()
            plt.close()
            stillTraining = "N"
            print("Training Completed")
            print("\nPrediction has begun\n")
            return None

        resistance_values = glove_arduino.get_resistance_values()

        print("Saved Config Of: "+hand_index_to_string[finger_index])

        update_training_data(
            finger_index, resistance_values)

        prediction = get_prediction(resistance_values, lastFour)

        if prediction != None:
            print("Prediction: "+hand_index_to_string[prediction])
        # else:
        #     print("Prediction: "+hand_index_to_string[10])

        prediction = None  # so we return none
        plot_bar_x(resistance_values)
    else:
        if first:
            print("For some reason, this loop requires you to enter any character for the first iteration. Please enter a character")
            starter = get_input()
            first = False

        # finger_index = get_input()
        # time.sleep(.05)
        # print(finger_index)

        # if finger_index > 10:
        #     stillTraining = "N"
        #     print("Training Completed")
        #     return None
        resistance_values = glove_arduino.get_resistance_values()

        prediction = get_prediction(resistance_values, lastFour)
        if prediction != None:
            print("Prediction: "+hand_index_to_string[prediction])
        # else:
        #     print("Prediction: "+hand_index_to_string[10])

    return prediction


def main():
    global stillTraining
    global values
    glove_arduino = setupArduinos()
    print("Successfully Connected to Arduinos\n")
    #

    if stillTraining == "Y":
        plt.show()
        print("Do you want to reset training data? (Y/N)")
        if readchar.readchar().decode('ascii').upper() == "Y":
            values = {}
            np.save(outfile, values)
            print("Training data reset")

        print("Okay, continue training. If you press a number greater than 9, it will go into prediction")
    else:
        print("\nPrediction has begun\n")
    while 1:
        loop(glove_arduino)


if __name__ == "__main__":
    main()
