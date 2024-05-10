#!/bin/bash

set -e

echo "CC/CXX: $CC/$CXX"
echo "CFLAGS: $CFLAGS"
echo "CXXFLAGS: $CXXFLAGS"

source /opt/ros/humble/setup.bash

# . ~/ros2_humble/install/local_setup.bash

. ~/axior_ws/install/setup.bash
. ~/realsense_ws/install/setup.bash

echo "ROS_DISTRO: $ROS_DISTRO"
echo "ROS_ROOT: $ROS_ROOT"

exec /bin/bash