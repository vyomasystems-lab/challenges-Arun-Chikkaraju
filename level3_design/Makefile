# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/level3_design.v               # provide your design path

TOPLEVEL :=level3_design           # design file
MODULE   :=level3_design     # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
