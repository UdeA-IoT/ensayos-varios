
# Fase 1

## Descripción 

Control de arduino usando el serial

|Comando|Descripción|
|---|---|
|```0```|Apagar led|
|```1```|Encender led|

### Software


```C
// Commands
#define ON '1'
#define OFF '0'

int incomingByte = 0; // for incoming serial data

/** setup **/
void setup() {  
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(115200);         // opens serial port, sets data rate to 115200 bps
}

/** loop **/
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte == ON) {
      digitalWrite(LED_BUILTIN, HIGH);      
    }
    else {
      digitalWrite(LED_BUILTIN, LOW);   
    }
  }
}
```

### Hardware

Agregar imagen (pnf, archivo fritzing, simulacion en tinkercad)

## Enlaces


