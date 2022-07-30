# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)



VERILOG_SOURCES = $(PWD)/projdesign3.v           # provide your design path

TOPLEVEL := projdesign3          # design file
MODULE   := test_design3    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
