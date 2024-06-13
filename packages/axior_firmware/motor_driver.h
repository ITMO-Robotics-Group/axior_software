// #ifdef L298_MOTOR_DRIVER
#define RIGHT_MOTOR_BACKWARD 8
#define LEFT_MOTOR_BACKWARD  11
#define RIGHT_MOTOR_FORWARD  7
#define LEFT_MOTOR_FORWARD   10
#define RIGHT_MOTOR_ENABLE 6
#define LEFT_MOTOR_ENABLE 9
// #endif

void initMotorController();
void setMotorSpeed(int i, int spd);
void setMotorSpeeds(int leftSpeed, int rightSpeed);
