#!/usr/bin/env python3

'''
    Launches a Segmentation node.
'''
import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Package directory
    segmentation_dir = get_package_share_directory('laser_segmentation')

    # Create the launch configuration variables.
    scan_topic = LaunchConfiguration('scan_topic')
    segments_topic = LaunchConfiguration('segments_topic')
    segmentation_type = LaunchConfiguration('segmentation_type')

    # Map these variables to arguments: can be set from the command line or a default will be used
    scan_topic_launch_arg = DeclareLaunchArgument(
        'scan_topic',
        default_value='scan',
        description='Topic to subscribe to for laser scan data.'
    )

    segments_topic_launch_arg = DeclareLaunchArgument(
        'segments_topic',
        default_value='segments',
        description='Topic to publish segments to.'
    )

    segmentation_type_launch_arg = DeclareLaunchArgument(
        'segmentation_type',
        default_value='jump_distance_merge',
        description='Type of segmentation to use.'
    )

    # Prepare the laser segmentation node.
    segmentation_node = Node(
            package = 'laser_segmentation',
            namespace = '',
            executable = 'laser_segmentation',
            name = 'segmentation',
            parameters = [{
                'scan_topic': scan_topic, 
                'segments_topic': segments_topic, 
                'segmentation_type': segmentation_type
            }],
            emulate_tty = True
        )

    return LaunchDescription([
        scan_topic_launch_arg,
        segments_topic_launch_arg,
        segmentation_type_launch_arg,
        segmentation_node
    ])