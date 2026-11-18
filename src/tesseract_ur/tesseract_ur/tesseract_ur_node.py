# from tesseract_robotics import get_tesseract_resource_path
# from tesseract_robotics.common import GeneralResourceLocator

import numpy as np
from tesseract_robotics.planning import (
    Robot, MotionProgram, JointTarget, plan_ompl,
)
from tesseract_robotics.viewer import TesseractViewer

robot = Robot.from_urdf(
    "package://tesseract_ur/urdf/ur5e_default.urdf",
    "package://tesseract_ur/urdf/ur5e.srdf",
)

program = (
    MotionProgram("ur_manipulator", tcp_frame="tool0", working_frame="base_link")
    .move_to(JointTarget(np.zeros(6)))
    .move_to(JointTarget(np.array([0.5, -0.5, 0.5, 0.0, 0.5, 0.0])))
)

result = plan_ompl(robot, program)
if result.successful:
    for state in result.trajectory:
        print(state.positions)

with TesseractViewer() as viewer:
    viewer.update_environment(result)
    print(f"Viewer at {viewer.url}")
    input("Press Enter to exit...")


def main() -> None:
    print('Hi from tesseract_ur.')


if __name__ == '__main__':
    # main()
    pass
