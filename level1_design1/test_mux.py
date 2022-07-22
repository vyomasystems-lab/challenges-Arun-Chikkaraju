# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    Select=30;

    # input driving
    dut.sel.value = Select
   

    await Timer(2, units='ns')

    assert dut.out.value == out, f"mux result is incorrect: {dut.out.value} != inp30"


    cocotb.log.info('##### CTB: Develop your test here ########')
