import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from serial_motor_demo_msgs.msg import MotorCommand
from sensor_msgs.msg import Joy

class PS4ControllerNode(Node):
    def __init__(self):
        super().__init__('ps4_controller_node')
        # self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.publisher_ = self.create_publisher(
                                    MotorCommand,
                                    'motor_command',
                                    10)
        
        self.subscription = self.create_subscription(
                                    Joy,
                                    '/joy',
                                    self.joy_callback,
                                    10)
        self.subscription  # prevent unused variable warning

    # def joy_callback(self, msg): # for Twist msg type
    #     twist = Twist()
    #     twist.linear.x = msg.axes[1]  # Left stick vertical axis
    #     twist.linear.y = msg.axes[3]  # Right stick vertical axis
    #     self.publisher_.publish(twist)

    def joy_callback(self, msg): # for Twist msg type
        commands = MotorCommand()
        commands.is_pwm = True
        commands.speed_left = round(255 * msg.axes[1], 3)  # Left stick vertical axis
        commands.speed_right = round(255 * msg.axes[3], 3)  # Right stick vertical axis
        self.publisher_.publish(commands)

    # def motor_command_callback(self, motor_command):
    #     if (motor_command.is_pwm):
    #         self.send_pwm_motor_command(motor_command.mot_1_req_rad_sec, motor_command.mot_2_req_rad_sec)
    #     else:
    #         # counts per loop = req rads/sec X revs/rad X counts/rev X secs/loop 
    #         # scaler = (1 / (2*math.pi)) * self.get_parameter('encoder_cpr').value * (1 / self.get_parameter('loop_rate').value)
    #         # mot1_ct_per_loop = motor_command.mot_1_req_rad_sec * scaler
    #         # mot2_ct_per_loop = motor_command.mot_2_req_rad_sec * scaler
    #         # self.send_feedback_motor_command(mot1_ct_per_loop, mot2_ct_per_loop)
    #         pass

def main(args=None):
    rclpy.init(args=args)
    ps4_controller_node = PS4ControllerNode()
    rclpy.spin(ps4_controller_node)
    ps4_controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
