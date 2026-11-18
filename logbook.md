## 2026-11-3 Nanobind install and tests
* There was alread a pixi environment with ROS2 installed.
* I wanted to add tesseract-nanobind to the Pixi env, but got a message that no matching version was found:

       Because all versions of tesseract-robotics-nanobind have no wheels with a matching platform tag (e.g., 'manylinux_2_28_x86_64') and you require tesseract-robotics-nanobind, we can conclude that your requirements are unsatisfiable.

        hint: Wheels are available for 'tesseract-robotics-nanobind' (v0.35.0.8) on the following platforms: 'manylinux_2_35_aarch64', 'manylinux_2_35_x86_64', 'macosx_14_0_arm64'`, win_amd64" 

* Problem was that nanbind relies on glibc 2.35 and pixi by default works on glibc 2.28. 
* Fix was to set glibc target in pixi.toml
* Copied the example from the nanobind repo to nanobind_example.py and could run it
* Also installed VS Code in WSL and added Pixi and Python plugins (were not yet installed on my laptop)


        


