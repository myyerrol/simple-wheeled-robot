int      distance;
int      distance_left;
int      distance_right;
int      motor_value;
int      motor_value_a;
int      motor_value_b;
int      motor_value_c;
int      motor_value_d;
int      motor_a               = 6;
int      motor_b               = 7;
int      motor_c               = 8;
int      motor_d               = 9;
int      servo                 = 5;
int      led                   = 2;
int      led_red               = 13;
int      led_yellow            = 12;
int      led_green             = 11;
int      distance_sensor_left  = 3;
int      distance_sensor_right = 4;
char     data;
uint16_t angle                 = 1500;

void setup()
{
    // Set serial's baud rate.
    Serial.begin(9600);
    pinMode(motor_a, INPUT);
    pinMode(motor_b, INPUT);
    pinMode(motor_c, INPUT);
    pinMode(motor_d, INPUT);
    pinMode(servo, OUTPUT);
    pinMode(led , OUTPUT);
    pinMode(led_red, OUTPUT);
    pinMode(led_yellow, OUTPUT);
    pinMode(led_green, OUTPUT);
    pinMode(distance_sensor_left, INPUT);
    pinMode(distance_sensor_right, INPUT);
    pinMode(A0, OUTPUT);
    pinMode(A1, OUTPUT);
    pinMode(A2, OUTPUT);
    pinMode(A3, OUTPUT);
    pinMode(A4, OUTPUT);
    pinMode(A5, OUTPUT);
}

void loop()
{
    if (Serial.available()) {
        switch(Serial.read()) {
            // Light up the logo.
            case 'h': {
                digitalWrite(A0, HIGH);
                digitalWrite(A1, HIGH);
                digitalWrite(A2, HIGH);
                digitalWrite(A3, HIGH);
                digitalWrite(A4, HIGH);
                digitalWrite(A5, HIGH);
                break;
            }
            // Turn off the logo.
            case 'j': {
                digitalWrite(A0, LOW);
                digitalWrite(A1, LOW);
                digitalWrite(A2, LOW);
                digitalWrite(A3, LOW);
                digitalWrite(A4, LOW);
                digitalWrite(A5, LOW);
                break;
            }
            // Move the servo in forward directory.
            case 'o' : {
                angle += 50;
                if (angle > 2500) {
                    angle = 2500;
                }
                break;
            }
            // Move the servo in reverse directory.
            case 'p' : {
                angle -= 50;
                if (angle < 500) {
                    angle = 500;
                }
                break;
            }
            case 'n': {
                digitalWrite(led, HIGH);
                break;
            }
            case 'm': {
                digitalWrite(led, LOW);
                break;
            }
            case 'g': {
                // When the distance between objects and car is far enough,
                // light the green led.
                digitalWrite(led_green, HIGH);
                digitalWrite(led_yellow, LOW);
                digitalWrite(led_red, LOW);
                break;
            }
            case 'y': {
                // When the distance between objects and car is near enough,
                // light the yellow led.
                digitalWrite(led_yellow, HIGH);
                digitalWrite(led_green, LOW);
                digitalWrite(led_red, LOW);
                break;
            }
            case 'r': {
                // When the distance between objects and car is very near,
                // light the red led.
                digitalWrite(led_red, HIGH);
                digitalWrite(led_yellow, LOW);
                digitalWrite(led_green, LOW);
                break;
            }
            case 'k': {
                // Return distance sensor's state between objects and car.
                distance_left = digitalRead(distance_sensor_left);
                distance_right = digitalRead(distance_sensor_right);
                distance = distance_left * 10 + distance_right ;
                Serial.println(distance, DEC);
                break;
            }
            case 'i': {
                while (1) {
                    // Return motor's state to raspberry pi.
                    motor_value_a = digitalRead(motor_a);
                    motor_value_b = digitalRead(motor_b);
                    motor_value_c = digitalRead(motor_c);
                    motor_value_d = digitalRead(motor_d);
                    motor_value = motor_value_a * 1000 + motor_value_b * 100 +
                        motor_value_c * 10 + motor_value_d;
                    Serial.println(motor_value, DEC);
                    delay(1000);
                    data = Serial.read();
                    if (data == 'l') {
                        break;
                    }
                }
            }
            default:
                break;
        }
    }
    // Delay enough time for servo to move position.
    digitalWrite(servo, HIGH);
    delayMicroseconds(angle);
    digitalWrite(servo, LOW);
    delay(15);
}
