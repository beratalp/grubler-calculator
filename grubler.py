# !/usr/bin/env python3
# This script determines if a given 3D kinematic chain is over-defined, fully defined or
# under-defined using the Grübler's Criteria.


n_of_linkages = int(input("Enter number of linkages: "))
n_of_3dof_joints = int(input("Enter number of joints with 3DOF: "))
n_of_2dof_joints = int(input("Enter number of joints with 2DOF: "))
n_of_1dof_joints = int(input("Enter number of joints with 1DOF: "))
system_dof = int(input("Enter the system DOF: "))

n_of_joints = n_of_1dof_joints + n_of_2dof_joints + n_of_3dof_joints

rhs = 6*(n_of_linkages - 1 - n_of_joints) + n_of_1dof_joints + 2*n_of_2dof_joints + 3*n_of_3dof_joints
if system_dof == rhs:
    print("System is fully defined.")
elif system_dof < rhs:
    print("System is over-defined.")
else:
    print("System is under-defined.")


