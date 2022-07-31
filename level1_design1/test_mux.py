import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random

@cocotb.test()
def mux_test1(dut):
    yield Timer(2)
    
    SEL=30
    INP30=1
    dut.inp30.value = INP30
    dut.sel.value = SEL
    yield Timer(2)
    if dut.out != INP30:
        raise TestFailure("MUX failed with: input %s and sel %s actual out was %s but got %s" % (dut.inp30, dut.sel,dut.inp30,dut.out))
    else:
        dut.log.info("MUX pased with: input %s and sel %s actual out was %s and got %s" % (dut.inp30, dut.sel,dut.inp30,dut.out))
        
@cocotb.test()        
def mux_test2(dut):
    yield Timer(2)
    
    SEL=12
    INP12=0
    dut.inp12.value = INP12
    dut.sel.value = SEL
    yield Timer(2)
    if dut.out != INP12:
        raise TestFailure("MUX failed with: input %s and sel %s actual out was %s but got %s" % (dut.inp12, dut.sel,dut.inp12,dut.out))
    else:
        dut.log.info("MUX pased with: input %s and sel %s actual out was %s and got %s" % (dut.inp12, dut.sel,dut.inp12,dut.out))
        
        
        
@cocotb.test()        
def mux_test3(dut):
    yield Timer(2)
    
    SEL=21
    INP21=1
    dut.inp21.value = INP21
    dut.sel.value = SEL
    yield Timer(2)
    if dut.out != INP21:
        raise TestFailure("MUX failed with: input %s and sel %s actual out was %s but got %s" % (dut.inp21, dut.sel,dut.inp21,dut.out))
    else:
        dut.log.info("MUX pased with: input %s and sel %s actual out was %s and got %s" % (dut.inp21, dut.sel,dut.inp21,dut.out))
        
        
@cocotb.test()        
def mux_test4(dut):
    yield Timer(2)
    
    SEL=10
    INP10=1
    dut.inp10.value = INP10
    dut.sel.value = SEL
    yield Timer(2)
    if dut.out != INP10:
        raise TestFailure("MUX failed with: input %s and sel %s actual out was %s but got %s" % (dut.inp10, dut.sel,dut.inp10,dut.out))
    else:
        dut.log.info("MUX pased with: input %s and sel %s actual out was %s and got %s" % (dut.inp10, dut.sel,dut.inp10,dut.out))
        

        
        
