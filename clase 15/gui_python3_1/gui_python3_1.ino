char serialData;
int pinRojo = 13;
int pinVerde = 8;
int pinAma = 10;
void setup() {
  // put your setup code here, to run once:
  pinMode(pinRojo,OUTPUT);
  pinMode(pinVerde,OUTPUT);
  pinMode(pinAma,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0) {
    serialData = Serial.read();
    Serial.println(serialData);

    if(serialData == '0'){
      digitalWrite(pinRojo, HIGH);
      }else{
        if(serialData == '1'){
          digitalWrite(pinRojo, LOW);
           if(serialData == '2'){
             digitalWrite(pinVerde, HIGH);
             }else{
               if(serialData == '3'){
                 digitalWrite(pinVerde, LOW);
                  if(serialData == '4'){
                    digitalWrite(pinAma, HIGH);
                    }else{
                      if(serialData == '5'){
                        digitalWrite(pinAma, LOW);
                         if(serialData == '6'){
                           digitalWrite(pinRojo,HIGH);
                           digitalWrite(pinVerde,HIGH);
                           digitalWrite(pinAma,HIGH);
                           }else{
                            if(serialData == '7'){
                              digitalWrite(pinRojo,LOW);
                              digitalWrite(pinVerde,LOW);
                              digitalWrite(pinAma,LOW);
                              }else{
                              }
                             }
                            }
                           }
                          }
                         }
                        }
                       }
                      }
                     }
