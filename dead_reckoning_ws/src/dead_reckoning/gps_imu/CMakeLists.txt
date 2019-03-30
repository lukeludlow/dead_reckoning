cmake_minimum_required(VERSION 2.8.3)
project(gps_imu)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES navigation2
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
  src/
  ${catkin_INCLUDE_DIRS}
)
