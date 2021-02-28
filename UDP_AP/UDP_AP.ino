#include <WebServer.h>
#include <WiFi.h>
#include <WiFiUdp.h>

// the IP of the machine to which you send msgs - this should be the correct IP in most cases (see note in python code)
#define CONSOLE_IP "192.168.1.2"
#define CONSOLE_PORT 4210
const char* ssid = "ESP32-1"  ;
const char* password = "12345678";
WiFiUDP Udp;
IPAddress local_ip(192, 168, 1, 1);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
WebServer server(80);

int xyzPins[] = {33, 32, 35};   //x,y,z pins

void setup()
{
  Serial.begin(115200);
  pinMode(xyzPins[2], INPUT_PULLUP);  //z axis is a button.
  pinMode(25, INPUT_PULLUP);
  
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  server.begin();
}

void loop()
{
  int xVal = analogRead(xyzPins[0]);
  int yVal = analogRead(xyzPins[1]);
  int zVal = digitalRead(xyzPins[2]);
  int bval = digitalRead(25);
  Udp.beginPacket(CONSOLE_IP, CONSOLE_PORT);
  // Just test touch pin - Touch0 is T0 which is on GPIO 4.
  Udp.printf("%d,%d,%d,%d", xVal, yVal, zVal, bval);
  //Udp.printf("%d",bval);
  Udp.endPacket();
  delay(1000);
}

//#include <WebServer.h>
//#include <WiFi.h>
//#include <WiFiUdp.h>
//
//// the IP of the machine to which you send msgs - this should be the correct IP in most cases (see note in python code)
//#define CONSOLE_IP "192.168.1.2"
//#define CONSOLE_PORT 4210
//const char* ssid = "ESP32";
//const char* password = "12345678";
//WiFiUDP Udp;
//IPAddress local_ip(192, 168, 1, 1);
//IPAddress gateway(192, 168, 1, 1);
//IPAddress subnet(255, 255, 255, 0);
//WebServer server(80);
//
//void setup()
//{
//  Serial.begin(115200);
//  
//  WiFi.softAP(ssid, password);
//  WiFi.softAPConfig(local_ip, gateway, subnet);
//  server.begin();
//}
//
//void loop()
//{
//  Udp.beginPacket(CONSOLE_IP, CONSOLE_PORT);
//  // Just test touch pin - Touch0 is T0 which is on GPIO 4.
//  Udp.printf(String(touchRead(T0)).c_str());
//  Udp.endPacket();
//  delay(1000);
//}


/*

import socket

# use ifconfig -a to find this IP. If your pi is the first and only device connected to the ESP32, 
# this should be the correct IP by default on the raspberry pi
LOCAL_UDP_IP = "192.168.1.2"
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.bind((LOCAL_UDP_IP, SHARED_UDP_PORT))

def loop():
    while True:
        data, addr = sock.recvfrom(2048)
        print(data)

if __name__ == "__main__":
    loop()
    
*/
