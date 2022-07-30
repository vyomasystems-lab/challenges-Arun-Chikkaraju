# level2 ( Bitmanipulation Coprocessor) Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

My Gitpod id with the screenshot


## Screenshots

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/gitpod%20home%20screen.png)

## Description
This design consists of a three 32-bit input values which are called as operands and 32- bit instruction which are given as inputs which which produces an 33-bit
output the extra bit is called as valid bit.

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic1.png)


## Verification Environment

  The CoCoTb based Python test is developed as explained.To the reference the python testbench file is also given for the better understanding
  we need to drive the inputs from the dut to test_mkbitmanip.py file and need to obsverve the bugs.

```bash
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x34
    mav_putvalue_src3 = 0x55
    mav_putvalue_instr = 0x40004033
```
 According to the given table:
 
 ![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic2.png)
 
 we need to give the different combination of ``mav_putvalue_instr`` and ``mav_putvalue_src1  mav_putvalue_src2   mav_putvalue_src3 ``and oberve the outputs 
 (required output and dut output)
 
 ![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic3.png)
 



## verification approach

according to the above table we need to decode the instruction like this:
![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic4.png)

for the simplicity of the code the values of the registers rs1 rs2 and rd are considered as 0 
The output depends on the func7 f3 and opcode 


## Test Scenario(Failed cases)

It is observed that for some of the testcases bugs are identified in which the output of dut differs from the actual output

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic5.png)

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic6.png)

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic7.png)

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic8.png)


## Test Scenario(Passed cases)

It is observed that for some of the testcases which correct .The output of dut is same as the actual output

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic9.png)

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic10.png)

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/pic11.png)



## conclusion 

The design was verified and the bugs were identified using cocotb
