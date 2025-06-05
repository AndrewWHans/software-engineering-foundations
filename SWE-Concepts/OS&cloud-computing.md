# Operating Systems (OS)

**What exactly are operating systems?**
<br>
Operating systems are system software that manages all the resources of the computing device. They act as an *intermediary* between the user and the computer's hardware. <br>
Due to an OS being large and complex, it must be created piece-by-piece with defined inputs and outputs (IO) and functons that control and monitor the execution of other programs. This would include application programs and other system software of the computer. <br>
The OS allows the user to communicate to the computer without needing to know the computer's language. From a computer point-of-view, this makes the operating system a resource allocator.<br> Simply put:
[**Without an operating system, a computer is useless**](https://edu.gcfglobal.org/en/computerbasics/understanding-operating-systems/1/) <br><br>

## Common Operating Systems and functions

Each OS has their own *GUI*, which is a way to allow the user to click on icons or buttons or menus on a displayed screen that has a combination of both text and graphics. <br>
Some common OS models include: Microsoft Windows, macOS, Linux

As a **function**, the operating system has many operations such as:
- Resources: managing & allocating memory, CPU time, and other hardware resources within programs and processes that run on the computer.
- Processing: addressing the starting/stopping and managing processes/programs. The system ensures each process uses the CPU, synchronizes, and has access to resources in case.
- Memory: OS handles the computer's primary memory and provides mechanisms for optimizing memory use, ensuring accurate allocation and deallocations are proper to run programs smoothly.
- File Systems: manage how files get stored to storage devices, ensuring smooth access through directories and permissions. This includes attributes, types, operations, and access methods.
- Security: implements security policies and mechanisms like access control or encryption <br>
And many more! There are **types** of operating systems too, including *batch, time-sharing, distributed, network, real-time*. <br>
To check out more, please refer to this [link](https://www.geeksforgeeks.org/types-of-operating-systems/). <br>

## Concepts

**Moore's Law**: the prediction that the number of transistors on an integrated circuit will double every 18 months. <br>
The **kernel** is the core of the operating system, responsible for managing system resources and interacting directly with the hardware. <br>
Mobile operating systems include not only a core kernel but also a **middleware**, a set of software frameworks that provide additional services to app developers. An example of this is Google's Android/Apple's iOS featuring the kernel along with middleware supporting databases, multimedia, and graphics.
## Types of kernels include: <br>

1) Monolithic
    - all operating systems operate in kernel spaces. Has dependencies between system components and complex code.
    - usually faster than other types of kernels (don't have to switch between the user & kernel modes for all system calls)<br>
    - for memory: about 100s of MBs-GBs

Examples are: Unix, Linux, Open VMS, etc.

2) Micro
    - minimalist approach, virtual memory and thread scheduling.
    - more stable with less services in kernel space. Used in small OS
    - is analogous, typical memory size is about ~10-100 MB <br>
    
Examples are: Mach, L4,AmigaOS, Minix, K42, etc.

3) Hybrid
    - combination of monolithic & micro, speed and design of monolithic while having the modularity and stability of a microkernel.
    - memory size is 500MB-several GBs

Examples: Windows NT, Netware, BeOS, ReactOS, etc.

4) Exo
    - kernel that follows end-to-end principle. Has the fewest hardware abstractions possible and allocates physical resources to applications.
    - memory size is about 1-10 of MB.

Examples are: Nemesis, ExOS, MIT Exokernel, XOK, etc.

5) Nano
    - offers hardware abstraction but no system services.
    - does the bare minimum services for system to work.
    - is analogous, typical size is about <100 KB<br>

Examples are: EROS, CapROS, seL4, etc.
<br>

## References

[Operating System Concepts 10th edition](https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf) <br>
[What is an Operating System?](https://www.geeksforgeeks.org/what-is-an-operating-system/) <br>
[Functions of an Operating System](https://www.geeksforgeeks.org/functions-of-operating-system/) <br>
[Kernel in Operating System](https://www.geeksforgeeks.org/kernel-in-operating-system/) <br>
[What is middleware?](https://www.redhat.com/en/topics/middleware/what-is-middleware)
[Time-sharing](https://www.ibm.com/history/time-sharing) <br>
[Understanding cloud computing](https://www.redhat.com/en/topics/cloud-computing) <br>