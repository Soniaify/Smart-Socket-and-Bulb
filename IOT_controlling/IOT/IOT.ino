int relay_pin = 7;

String cmd = "";

void setup() {
  pinMode(relay_pin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    cmd = Serial.readStringUntil('\n');
    cmd.trim();
  }
  if (cmd == "on") {
      digitalWrite(relay_pin, LOW);
      Serial.println("Device turned ON");
  } 
  else if (cmd == "off") {
      digitalWrite(relay_pin, HIGH);
      Serial.println("Device turned OFF");
  }
  else{
    Serial.println("Invalid command");
  }
}
