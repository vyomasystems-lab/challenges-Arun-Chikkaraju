import os
import random
from pathlib import Path
from cocotb.result import TestFailure

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()

async def func(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    dut.reset.value = 0
    await  FallingEdge(dut.clk)  
    dut.reset.value = 1
    await  FallingEdge(dut.clk)
    dut.reset.value = 0
    await  FallingEdge(dut.clk)
    for opr in range(1,15):
        for i in range(1):
            a_value=random.randint(1, 50000)
            b_value=random.randint(1, 50000)
            await FallingEdge(dut.clk)
            dut.A.value=a_value
            dut.B.value=b_value
            dut.opcode.value=opr
            await FallingEdge(dut.clk)
            out=(a_value%b_value)
            dut.log.info("Design with Value of A:%s  Value of B:%s out is :%s operation is:%s "%(int(dut.A),int(dut.B),int(dut.C),int(dut.opcode)))
            await FallingEdge(dut.clk)
           
