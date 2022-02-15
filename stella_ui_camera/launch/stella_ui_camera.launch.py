#!/usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stella_ui_camera',
            executable='stella_ui_camera_node',
            name='stella_ui_camera_node',
            output='screen'
        )
    ])


