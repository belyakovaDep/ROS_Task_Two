# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

command_list = ['turn_right', 'turn_left', 'move_forward', 'move_backward']

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        command = input()
        if command in command_list:
            msg = Twist()
            if command == 'move_forward':
                msg.linear.x = 2.0
            if command == 'move_backward':
                msg.linear.x = -2.0
            if command == 'turn_right':
                msg.angular.z = -2.0
            if command == 'turn_left':
                msg.angular.z = 2.0

            self.publisher_.publish(msg)
            self.get_logger().info('Done!')
        else:
            print("I didn't understand you! Please, use the commands from our task. I have no imagination to create more.")


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
