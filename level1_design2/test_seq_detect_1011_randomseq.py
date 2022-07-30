import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    seq_seen = 0
    # reset
    dut.reset.value = 0
    await  FallingEdge(dut.clk)  
    dut.reset.value = 1
    await  FallingEdge(dut.clk)
    await  FallingEdge(dut.clk) 
    cocotb.log.info(dut.next_state.value) 
    dut.reset.value = 0
    await  FallingEdge(dut.clk)
    for i in range(50):  
        INP_bit=random.randint(0,1)
        await FallingEdge(dut.clk)
        dut.inp_bit.value=INP_bit
        await FallingEdge(dut.clk)
        dut.log.info("input bit is %s and seqseen bit is %s present_state %d"%(int(dut.inp_bit),int(dut.seq_seen),int(dut.current_state)))
