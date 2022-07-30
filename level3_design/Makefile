# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/design3.v            # provide your design path

TOPLEVEL :=design3           # design file
MODULE   :=design3_test    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
