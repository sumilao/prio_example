#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific partial_reconfigr written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__ = "Tanner Gaskin"
__copyright__ = "GPL"
__email__ = "gaskin.tanner@byu.edu"

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info

import shutil
import subprocess
import sys
import os
from datetime import datetime


GIT_DIR = os.path.dirname(os.path.realpath(__file__))

if 'BOARD' not in os.environ:
    raise EnviromentError("Please set the BOARD environment variable "
        "to get any BOARD specific overlays (e.g. Pynq-Z1).")
    board = None
    board_folder = None
    # pynq_data_files = []
elif os.environ['BOARD'] != "Pynq-Z1" and os.environ['BOARD'] != "Pynq-Z2":
    raise EnviromentError("The BOARD environment variable must be set to either \"Pynq-Z1\" or \"Pynq-Z2\".")
    board = None
    board_folder = None
else:
    board = os.environ['BOARD']
    board_folder = '/boards/{}'.format(board)
    # pynq_data_files = collect_pynq_data_files()

PYNQ_DIR = GIT_DIR + board_folder


# Install packages
def install_packages():
    subprocess.check_call(['apt-get', '--yes', '--force-yes', 'install']),
    subprocess.check_call(['pip3.6', 'install'])
    print("Installing packages done ...")


# Notebook delivery
def fill_notebooks():
    src_nb = PYNQ_DIR + '/notebooks/'
    dst_nb_dir = '/home/xilinx/jupyter_notebooks/partial_reconfig/'
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    shutil.copytree(src_nb, dst_nb_dir)

    print("Filling notebooks done ...")
    
def fill_partial_reconfig():
    src_pr_dir = PYNQ_DIR + "/partial_reconfig/"
    dst_pr_dir = "/home/xilinx/pynq/overlays/partial_reconfig/"
    
    if not os.path.exists(dst_pr_dir):
        os.makedirs(dst_pr_dir)
        
    #copies over partial_reconfig files    
    shutil.copy(src_pr_dir + "partial_reconfig.bit", dst_pr_dir + "partial_reconfig.bit")
    shutil.copy(src_pr_dir + "partial_reconfig.tcl", dst_pr_dir + "partial_reconfig.tcl")
    shutil.copy(src_pr_dir + "partial_reconfig.py", dst_pr_dir + "partial_reconfig.py")
    shutil.copy(src_pr_dir + "__init__.py", dst_pr_dir + "__init__.py")
    
    #copies over partial bitstreams for the PR regions
    if os.path.exists(dst_pr_dir + "partial_bit/"):
        shutil.rmtree(dst_pr_dir + "partial_bit/")
    shutil.copytree(src_pr_dir + "partial_bit/", dst_pr_dir + "partial_bit/")
    
    #copies over partial bitstreams for the PR regions
    if os.path.exists(dst_pr_dir + "drivers/"):
        shutil.rmtree(dst_pr_dir + "drivers/")
    shutil.copytree(src_pr_dir + "drivers/", dst_pr_dir + "drivers/")
    
    print("installing Partial Reconfiguration Input/Output done...")
    
def remove_notebooks():
    dst_nb_dir = '/home/xilinx/jupyter_notebooks/partial_reconfig/'
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)

def remove_prio():
    dst_prio_dir = "/home/xilinx/pynq/overlays/partial_reconfig/"
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_prio_dir)

if len(sys.argv) > 1 and sys.argv[1] == 'install':
    install_packages()
    fill_notebooks()
    fill_partial_reconfig()

if len(sys.argv) > 1 and sys.argv[1] == 'uninstall':
    print("Removing partial_reconfig")
    remove_notebooks()
    remove_prio()


def package_files(directory):
    paths = []
    for (path, directories, file_names) in os.walk(directory):
        for file_name in file_names:
            paths.append(os.path.join('..', path, file_name))
    return paths


extra_files = package_files('partial_reconfig')


setup(
      name='prio',
      version='3.0.6',
      description='BYU PYNQ PRIO package',
      author='BYU CCL',
      author_email='gaskin.tanner@byu.edu',
      url='https://github.com/gaskint/prio_pip_test.git',
      packages=find_packages(),
      download_url='https://github.com/gaskint/prio_pip_test.git',
      package_data={
          '': extra_files,
      }
      )
