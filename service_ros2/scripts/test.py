#!/usr/bin/env python3
import rclpy

from service_ros2.srv import CupPose

def send_pos_callback(request, response):
    if request.req == True:
        response.x = 1.0
        response.y = 1.0
        response.z = 1.0
        response.d = 1.0
    else:
        response.x = 0.0
        response.y = 1.0
        response.z = 1.0
        response.d = 0.0
    return response

rclpy.init()
node = rclpy.create_node('service_ros2')
srv = node.create_service(CupPose, 'service', send_pos_callback)
while rclpy.ok():
    rclpy.spin_once(node)
node.destroy_service(srv)
