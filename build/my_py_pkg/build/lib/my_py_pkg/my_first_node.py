#!/usr/bin/evn python3

import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello ROS2")
    #node.get_logger().error("Hello ROS2")
    #node.get_logger().warning("Hello ROS2")
    rclpy.spin(node)     #program is still running
    rclpy.shutdown()

if __name__=="__main__":
    main()
