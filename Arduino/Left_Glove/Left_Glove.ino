//This code is for the arduino on the Left Glove 

// What pins to connect the sensors to 
#define FLEXSENSORPIN0 A0 
#define FLEXSENSORPIN1 A1 
#define FLEXSENSORPIN2 A2 
#define FLEXSENSORPIN3 A3 
#define FLEXSENSORPIN4 A4 

//WILL HAVE TO CHANGE ONCE ON GLOVE AS PINS WILL LIKELY CHANGE
int ledAnalogOne[] = {11,10,9}; //the three pins of the first analog LED in the order of red, green, blue
 //These pins must be PWM

//defined variables for each sensor according to finger
float thumbReading;
float indexReading;
float middleReading;
float ringReading;
float pinkyReading;

float redVal=0;
float greenVal=0;
float blueVal=0;


void setup(void) {
  setupSerial();
  setupLights();
}

void loop(void) {
  getReadings();
  updateLEDS();

  if (shouldSend()) {
    sendResistanceValues();
  }

//  average();

  
  delay(100);
}


void setupSerial() {
  Serial.begin(9600);
}

void setupLights() {
  for(int i = 0; i < 3; i++){
    pinMode(ledAnalogOne[i], OUTPUT);   //Set the three LED pins as outputs
  }
}

bool shouldSend() {
  
  if (Serial.available() > 0) {
    while (Serial.available() > 0) {
      Serial.read();
    }
   
   return true;
  }
 return false;
 
}

void updateLEDS() {
  if(thumbReading<=100){
    redVal=255;
    greenVal=0;
    blueVal=0;   
  } else if(indexReading<=770){
    redVal=0;
    greenVal=255;
    blueVal=0;   
  } else if(middleReading<=100){
    redVal=0;
    greenVal=0;
    blueVal=255;   
  } else if(ringReading<=100){
    redVal=255;
    greenVal=100;
    blueVal=0;   
  } else if(pinkyReading<=100){
    redVal=255;
    greenVal=255;
    blueVal=0;   
  } else{
    redVal=255;
    greenVal=255;
    blueVal=255;    
  }

  setLED(redVal, greenVal, blueVal);
}

void getReadings() {
  thumbReading = singleReading(FLEXSENSORPIN0);
  indexReading = singleReading(FLEXSENSORPIN1); 
  middleReading = singleReading(FLEXSENSORPIN2); 
  ringReading = singleReading(FLEXSENSORPIN3);
  pinkyReading = singleReading(FLEXSENSORPIN4);
}

void sendResistanceValues() {
  Serial.println("** Sending Values **");
  Serial.println(thumbReading);
  Serial.println(indexReading);
  Serial.println(middleReading);
  Serial.println(ringReading);
  Serial.println(pinkyReading);
}
 
/**
 * gets a reading from an analog pin
 * @param pin the pin to read from
 * @return the reading
 */
float singleReading(int pin)
{
  float reading;
  reading = analogRead(pin);
  return reading;
}

/**
 * sets the values for the RBG LED
 * @param red the value for the red light 0-255
 * @param green the value for the green light 0-255
 * @param blue the value for the blue light 0-255
 */
void setLED(float red, float green, float blue)
{
   analogWrite(ledAnalogOne[0], red);
   analogWrite(ledAnalogOne[1], green);
   analogWrite(ledAnalogOne[2], blue);
}

/**
 * gets and print the average values taken from the sensor as per the NUMSAMPLES variable
 */
void average()
{
  int NUMSAMPLES = 100;
  uint8_t i;
  float average;
  int samples[NUMSAMPLES];
  
    // take N samples in a row, with a slight delay
  for (i=0; i< NUMSAMPLES; i++) {
    //Change the pin according to which sensor you are calibrating
   samples[i] = analogRead(FLEXSENSORPIN1);
   delay(10);
  }

  // average all the samples out
  average = 0;
  for (i=0; i< NUMSAMPLES; i++) {
     average += samples[i];
  }
  average /= NUMSAMPLES;
 
  Serial.print("Average reading "); 
  Serial.println(average);
}
