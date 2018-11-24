//Temperatura en LCD 16x2
#include <LiquidCrystal.h>
//Declarar LCD y pines
LiquidCrystal lcd(7,6,5,4,3,2);
void setup() {
  // put your setup code here, to run once:
  //Definir las dimenciones del LCD (16x2)
  //y los caracteres que deben salir en las lineas
  lcd.begin(16,2);
  lcd.print("Temperatura");
  lcd.setCursor(0,1);
  lcd.print("C=");

}

void loop() {
  // put your main code here, to run repeatedly:
  float centigrados = leerGradosC();
  //Visualizar por pantalla los grados
  lcd.setCursor(2,1);
  lcd.print(centigrados);
  //Tiempo y cambio de visualizacion de la temperatura
  delay(1000);
}
float leerGradosC(){
  int dato;
  float C;
  //Leer datos de temperatura
  dato = analogRead(A0);
  //Convertir dato de entrada en grados C .
  C = (500.0 * dato / 1024);
  return C;
}
