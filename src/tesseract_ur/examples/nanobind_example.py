from tesseract_robotics.planning import (
    Robot, MotionProgram, JointTarget, CartesianTarget, Pose, TaskComposer,
)

# Load a bundled robot (urdf + srdf from tesseract's support package)
robot = Robot.from_tesseract_support("abb_irb2400")

# Start at all-zero joints, goal is a tool0 pose (upstream freespace_example.cpp);
# quaternion is scalar-last [qx, qy, qz, qw]
start = [0.0] * 6
goal = Pose.from_xyz_quat(0.8, -0.2, 0.8, 0.0, -1.0, 0.0, 0.0)

# Build motion program
program = (MotionProgram("manipulator", tcp_frame="tool0", working_frame="base_link")
    .set_joint_names(robot.get_joint_names("manipulator"))
    .move_to(JointTarget(start))
    .move_to(CartesianTarget(goal))
)

# Plan
composer = TaskComposer.from_config()
result = composer.plan(robot, program)

assert result.successful, result.message
for pt in result.trajectory:
    print(pt.positions)