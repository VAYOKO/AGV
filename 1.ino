int sn1 = 4 , sn2 = 7 , sn3 = 8 , sn4 = 12 ;
int ma1 = 3 , ma2 = 5, mb1 = 6, mb2 = 9;
int periot = 0;
void setup() {

  pinMode(4, INPUT);
  pinMode(12, INPUT);
  pinMode(8, INPUT);
  pinMode(7, INPUT);

  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
}

void forward() {
  analogWrite(ma1, 100);
  analogWrite(ma2, 0);


  analogWrite(mb1, 81);
  analogWrite(mb2, 0);
}

void stop_move() {

  analogWrite(ma1, 0);
  analogWrite(ma2, 0);


  analogWrite(mb1, 0);
  analogWrite(mb2, 0);
}
void baneright() {

  analogWrite(ma1, 60);
  analogWrite(ma2, 0);


  analogWrite(mb1, 100);
  analogWrite(mb2, 0);


}


void baneleft() {

  analogWrite(ma1, 120);
  analogWrite(ma2, 0);


  analogWrite(mb1, 60);
  analogWrite(mb2, 0);

}
void loop() {

  if (digitalRead(sn1) == LOW) {
    baneright();
    delay(200);
  }
  else if (digitalRead(sn4) == LOW) {

   baneleft();
    delay(200);
  }
  else {
    forward();

  }
}
