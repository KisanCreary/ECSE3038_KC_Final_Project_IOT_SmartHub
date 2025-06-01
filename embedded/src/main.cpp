#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"
#include <ArduinoJson.h>
const char * ENDPOINT = "http://192.168.1.174:8000";
int ledLight;
int ledRed;

void sendSensorData(float temp, float humidity, float lux, int motion) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://<http://192.168.1.174:8000>:<port>/data"); 
    http.addHeader("Content-Type", "application/json");

    StaticJsonDocument<200> json;
    json["temperature"] = temp;
    json["humidity"] = humidity;
    json["lux"] = lux;
    json["presence"] = motion;

    String body;
    serializeJson(json, body);
    int response = http.POST(body);
    http.end();
  }
}

void fetchAndExecuteCommand() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://<http://192.168.1.174:8000>:<port>/action");
    int response = http.GET();

    if (response == 200) {
      String payload = http.getString();
      StaticJsonDocument<200> doc;
      deserializeJson(doc, payload);

     digitalWrite(ledLight, doc["light"]);
    digitalWrite(ledRed, doc["fan"]); // or any pin assigned to fan
    }
    http.end();
  }
}
