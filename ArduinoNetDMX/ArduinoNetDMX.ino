#include "DmxSimple.h"

#define DERE_PIN 2 // DE & RE Pin (must be set to HIGH to send DMX)
#define DMX_PIN Serial1 // MAC485 DI Pin

byte values[64];
int index = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(DERE_PIN, OUTPUT);
  digitalWrite(DERE_PIN, HIGH);
  Serial.begin(115200);
  DmxSimple.usePin(DMX_PIN);
  DmxSimple.maxChannel(64);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() > 0) {
    byte marker = Serial.read();
    if(marker == 0xFF && Serial.available() >= 63) {
      for(int i = 1; i < 64; i++) {
        DmxSimple.write(i, Serial.read());
      }
    }
  }
}
