from tesseract_robotics import get_tesseract_resource_path
from tesseract_robotics.common import GeneralResourceLocator
from tesseract_robotics.planning import Robot

# Resolves package://tesseract/... URLs to the [support] extra's files
#locator = GeneralResourceLocator(paths=[get_tesseract_resource_path()])

robot = Robot.from_urdf(
    "package://ur_description/urdf/robot.urdf",
    "package://tesseract)ur+/urdf/robot.srdf",
)


print(robot.get_joint_names("manipulator"))  # the SRDF group's six joints
