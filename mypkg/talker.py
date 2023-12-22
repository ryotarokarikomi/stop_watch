# SPDX-FilecopyrightText: 2023 Ryotaro Karikomi ryotaro.karikomi@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Nord
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
  global n
  msg.data = n
  pub.publish(msg)
  n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
