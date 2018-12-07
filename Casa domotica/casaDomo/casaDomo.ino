#include <Servo.h>
// Declaramos la variable para controlar el servo
Servo servoDisco;

char casaDomotica;

//asignamos los pines que se utilizaran
int LuzDisco1 = 38; 
int LuzDisco2 = 36;
int LuzPasillo =28 ;
int LuzGradas = 30;
int LuzSala = 34;
int servoPuer = 0;
int Disco1 = 0;
int Disco2 = 0;
int LuzPas = 0; 
int LuzGra = 0;
int LuzSal = 0;
int todo = 0;

void setup() {
  // put your setup code here, to run once:
  // Iniciamos el monitor serie para mostrar el resultado
  Serial.begin(9600);

  pinMode(LuzDisco1,OUTPUT);
  pinMode(LuzDisco2,OUTPUT);
  pinMode(LuzPasillo,OUTPUT);
  pinMode(LuzGradas,OUTPUT);
  pinMode(LuzSala,OUTPUT);

  // Iniciamos el servo para que empiece a trabajar con el pin 10
  servoDisco.attach(10);
  servoDisco.write(0); // Inicializamos al ángulo 0 el servomotor
  servoDisco.write (130); // cerramos la puerta
  
}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()>0) {
    casaDomotica = Serial.read();
    Serial.print(casaDomotica);

    if(casaDomotica == '1'){
      if(Disco1==0){
        digitalWrite(LuzDisco1, HIGH);
        delay(100);
        Disco1 = 1;
      }else{
        digitalWrite(LuzDisco1, LOW);
        delay(100);
        Disco1 = 0;}
      }else{
        if(casaDomotica == '2'){
          if(Disco2==0){
            digitalWrite(LuzDisco2, HIGH);
            delay(4000);
            Disco2 = 1;
          }else{
            digitalWrite(LuzDisco2, LOW);
            delay(4000);
            Disco2 = 0;}
          }else{
            if(casaDomotica == '3'){
              if(LuzPas==0){
                digitalWrite(LuzPasillo, HIGH);
                delay(4000);
                LuzPas = 1;
              }else{
                digitalWrite(LuzPasillo, LOW);
                delay(4000);
                LuzPas = 0;}
              }else{
                if(casaDomotica == '4'){
                  if(LuzGra==0){
                    digitalWrite(LuzGradas, HIGH);
                    delay(4000);
                    LuzGra = 1;
                  }else{
                    digitalWrite(LuzGradas, LOW);
                    delay(4000);
                    LuzGra = 0;}
                  }else{
                    if(casaDomotica == '5'){
                      if(LuzSal==0){
                        digitalWrite(LuzSala, HIGH);
                        delay(4000);
                        LuzSal = 1;
                      }else{
                        digitalWrite(LuzSala, LOW);
                        delay(4000);
                        LuzSal = 0;}
                      }else{
                        if(casaDomotica == '6'){
                          if(todo==0){
                            digitalWrite(LuzDisco1,HIGH);
                            digitalWrite(LuzDisco2,HIGH);
                            digitalWrite(LuzPasillo,HIGH);
                            digitalWrite(LuzGradas,HIGH);
                            digitalWrite(LuzSala,HIGH);
                            delay(4000);
                            todo = 1;
                            }else{
                            digitalWrite(LuzDisco1,LOW);
                            digitalWrite(LuzDisco2,LOW);
                            digitalWrite(LuzPasillo,LOW);
                            digitalWrite(LuzGradas,LOW);
                            digitalWrite(LuzSala,LOW);
                            delay(4000);
                            todo = 0;}
                          }else{
                            if(casaDomotica == '7'){
                              if(servoPuer==0){
                                servoDisco.write(0);
                                delay(4000);
                                servoPuer = 1;
                              }else{
                                servoDisco.write(90);
                                delay(4000);
                                servoPuer = 0;
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
