#include <FirebaseArduino.h>
#include <ESP8266WiFi.h>
#define WIFI_SSID "SSID"
#define WIFI_PASSWORD "PASSWORD"
#define FIREBASE_HOST "HOST_NAME"
#define FIREBASE_AUTH "AUTH"
const int trigPin = 8;            // Making the arduino's pin 8 as the trig pin of ultrasonic sensor
const int echoPin = 9;            // Making the arduino's pin 9 as the echo pin of the ultrasonic sensor
// defining two variable for measuring the distance
long duration;
int distance;
int height;                    // height of the dustbin
int percentage;
void setup() {
  
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);   // Setting the trigPin as Output pin
  pinMode(echoPin, INPUT);    // Setting the echoPin as Input pin
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  
  
  
}


void loop() {

 
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);   
duration = pulseIn(echoPin, HIGH);
distance= duration*0.034/2;
percentage=(height-distance)*100/height;
String percent=String(percentage);

if(distance<5){
Firebase.setString("STATUS","DUSTBIN IS FULL PLEASE COME AND COLLECT");
Serial.println(distance);
Serial.print("DUSTBIN IS FULL PLEASE COME AND COLLECT");
}else if(distance>5){
Firebase.setString("STATUS","DUSTBIN NOT FULL");
Serial.println(percentage);

}





}
