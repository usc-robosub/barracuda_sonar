from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('barracuda_sonar')
    params_file = os.path.join(pkg_share, 'config', 'ping_altimeter.yaml')

    return LaunchDescription([
        Node(
            package='ping_altimeter_driver',
            executable='ping_altimeter_node',
            name='ping1d_altimeter_node',
            output='screen',
            parameters=[params_file],
        ),
    ])
