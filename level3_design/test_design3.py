from cocotb.binary import BinaryValue
import os
import sys
import operator
from cocotb.result import ReturnValue


  
@cocotb.test()
def project1(dut):
    clock = Clock(dut.clk, 10, units="us")   
    cocotb.start_soon(clock.start())
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await  FallingEdge(dut.clk)
    await  FallingEdge(dut.clk)
  
    dut.A.value=77
    dut.B.value=49
    dut.opcode.value=1
    dut.log.info("output value is %d and error out  bit is %d"%(int(dut.C),int(dut.ERR_out))) 



