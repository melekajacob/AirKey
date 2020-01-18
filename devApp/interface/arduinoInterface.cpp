#include <iostream>
#include <fstream>
#include <cstdlib>
#include <unistd.h>
#include <uv.h>

#define SLEEP_TIME 5000000
#define RESISTANCE_VALUES 5
#define START_CHAR 0.0

using namespace std;

ifstream GetInputStream() {
	system("stty -F /dev/cu.usbmodem14201 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts");	//Activates the tty connection with the Arduino
	
	ifstream Arduino_Input("/dev/ttyACM0");	

	return Arduino_Input;
}

double* getResistanceValues(ifstream stream) {
	do {
		if (stream.eof()) {
			response.success = false;

			return repsonse;
		}
		
		stream >> current;
	} while (current != START_CHAR);
	
	for (int i = 0; i < RESISTANCE_VALUES; i++) {

	}
}

void startArduinoProcessing(atomic<bool> *ready, atomic<bool> stop, mutex lock, double resistanceValues[5]) {
	ifstream GetInputStream();

	idel(SLEEP_TIME);

	*ready = false;

	while (!stop) {
		lock.lock();



		resistanceValues

		lock.unlock();
	}

}

class ArduinoConnection {
	ArduinoConnection() {
		this.inputStream = GetInputStream();

		
	}

	public:
		vector<double> read() {

		}


	private:
		ifstream inputStream;


}

int ()
{

	ifstream GetInputStream()

	
	//Opens the tty connection as an ofstream, not used in this example
	
	double Voltage;	//The Arduino is reading the voltage from A0
	
	long int Time = time(NULL);
	int i;
	while(time(NULL)-Time < 5){}	//Wait five seconds for the Arduino to start up
	
	for(i = 0; i < 100;)
	{
		Time = time(NULL);
		while(time(NULL)-Time < 1){}	//wait one second to get good numbers into the Arduino stream
		while(!Arduino_Input.eof())	//while the eof flage isn't set
		{
			Arduino_Input >> Voltage;	//will set the error flag if not ready, will get a number from the Arduino stream if ready
			cout << Voltage << endl;	//Output it to the cout stream
			i++;	//Increament i, it is not known how many numbers I'll get at a time
		}
		Arduino_Input.clear();	//eof flag won't clear itself
	}
	Arduino_Input.close();	//Close the ifstream
	return(0);
}