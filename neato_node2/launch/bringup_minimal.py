from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    use_udp = DeclareLaunchArgument('use_udp', default_value="true")
    host = DeclareLaunchArgument('host', default_value="")

    return LaunchDescription([
        use_udp,
        host,
        Node(
            package='neato_node2',
            executable='neato_node',
            name='neato_driver',
            parameters=[{"use_udp": LaunchConfiguration('use_udp')}, {"host": LaunchConfiguration('host')}],
            output='screen'
        ),

        Node(
            package='fix_scan',
            executable='fix_scan',
            name='fix_scan'
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_laser',
            arguments=["-0.1016", "0", "0.0889", "-3.14159", "0", "0", "base_link", "base_laser_link"]
        )
    ])