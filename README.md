# PYNQ-PRIO PIP INSTALL Package

This repository contains the pip install package for the Partially-Reconfigurable Input/Output (PRIO) Project on the PYNQ.

This project allows the use of Partially-Reconfigurable regions in the PYNQ's FPGA to communicate with external hardware via the I/O pins on the PYNQ. Partial-Reconfiguration is when partitions are created inside an FPGA that can be programmed separate from the rest of the FPGA. Partial Reconfiguration enables a part of the FPGA to be reconfigured while the rest of the FPGA continues to function. This can lower the number of needed devices, increase flexibility and can improve speed. It also can provide abstraction to partial designs, allowing them to be treated more like plug-and-play software by the end-users.

Although the PRIO Project does provide better flexibility for some I/O protocol like IIC by using Partial-Reconfiguration, the main objective of this repository is to provide the user with knowledge of how to use partial reconfiguration on the PYNQ. A guide has been provided to help teach users how to design and implement their own partially-reconfigurable regions and insert-able modules. Also included in this pip are guides and demos that teach users how to use the provided partial regions and designs

## Quick Start

In order to install it on your PYNQ, you're PYNQ must be running the v2.4 image. The 2.4 image for the PYNQ-Z1 can be found <a href="http://pynq.io" target="_blank">here</a>. See the <a href="http://pynq.readthedocs.io/en/latest/getting_started.html" target="_blank">Quickstart guide</a> for details on writing the image to an SD card.

To install the PRIO project, run the following command from a terminal connected to your board:

```console
sudo -H pip3.6 install git+https://github.com/gaskint/prio_example.git
```
The pip install will create a partial_reconfig folder in  ~/pynq/overlays/ on the PYNQ board. This directory will contain the necessary files, including bitstreams and python files, that are needed for Partial-Reconfiguration on the PYNQ.

The pip package will also create a partial_reconfig directory in ~/jupyter_notebooks on the PYNQ. This folder will contain documentation to help you get started, as well as demos that can you show how to use Partial-Reconfigurable Input/Output in various applications.

To get started go, to ~/jupyter_notebooks/prio/Getting_Started_Partial_Reconfiguration_Input_Output.ipynb in Jupyter Notebooks for further details.

## Board Files and Overlays

All board related files including Vivado projects, bitstreams, and example notebooks, can be found in the `/boards` folder.

In Linux, you can rebuild the overlay by running *make* in the corresponding overlay folder (e.g. `/boards/Pynq-Z1/prio`). In Windows, you need to source the appropriate tcl files in the corresponding overlay folder.
