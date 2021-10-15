#!/bin/bash
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh

export PYTHONPATH=$PWD:$PYTHONPATH
export LD_LIBRARY_PATH=$PWD/install/lib:$LD_LIBRARY_PATH
export ROOT_INCLUDE_PATH=$PWD/install/include/FCCAnalyses:$ROOT_INCLUDE_PATH
export LD_LIBRARY_PATH=`python -m awkward.config --libdir`:$LD_LIBRARY_PATH

export ONNXRUNTIME_ROOT_DIR=/cvmfs/sft.cern.ch/lcg/releases/onnxruntime/1.8.0-47224/x86_64-centos7-gcc8-opt

