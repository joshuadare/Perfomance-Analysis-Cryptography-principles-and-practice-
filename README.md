# Perfomance-Analysis-Cryptography-principles-and-practice-
To run the AES Analysis, navigate to the "AES Project" folder and run AESProject.py in Python. If you desire to see time statistics ONLY, run AES_Timer.py. If you desire to see CPU Utilization and Memory Allocation statistics ONLY, run AES_PSUTIL.py.

To run the DES Analysis, navigate to the "DES Project" folder. For DES with a 64 bit key, run DES_Program.py in Python. For Triple DES with a 16 bit key, run 3DES_Programs.py. For Triple Des with a 24 bit key, run 3DES_Programs2.py. DES.py contains the algorithm for the DES algorithm itself, and is used for import purposes by the other program files.

To run the RSA Analysis, navigate to the "RSA Project" folder. This portion of the product only has one program file: python_rsa.py. 

Much of the code, including some of the cryptographic algorithms themselves, is imported through external modules. They can be installed through PIP if initial runs return an error for missing modules (see pycrtpyo, pyRSA, pyAES, and psutil).
