from communication import ArduinoInterface
import wordPredictor
import letterPredictor
import triggerTrainer


def setupArduinos():
    # right_hand_arduino = ArduinoInterface()

    # return None, right_hand_arduino

    glove_arduino = ArduinoInterface()
    return glove_arduino


triggerTrainer.stillTraining = "N"


def get_triggered_index(resistance_values):
    return triggerTrainer.loop(None, None, resistance_values)


letters_so_far = []


def action_loop(glove_arduino):
    try:
        global letters_so_far
        glove_arduino = glove_arduino.get_resistance_values()

        if resistance_values is None:
            print("null resistance values: continuing")

        triggered_finger = get_triggered_index(resistance_values)

        if triggered_finger is not None:
            if triggered_finger == 0:

                words = wordPredictor.predict(letters_so_far)

                for word in words:
                    print("Possible Words: " + ", ".join(words))

                letters_so_far = []
            else:
                letters_so_far.append(
                    letterPredictor.get_letters(triggered_finger))
    except KeyboardInterrupt:
        raise
    except:
        pass


def main():
    # left_arduino, right_arduino = setup()
	glove_arduino = setup()

	input("Click Enter to Start")

    while 1:
        action_loop(glove_arduino)


if __name__ == "__main__":
    main()
