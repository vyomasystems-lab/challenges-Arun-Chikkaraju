
# level1_design1 (mux) Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

My Gitpod id with the screenshot


## Screenshots

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/gitpod%20home%20screen.png)


## Verification Environment

  The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (MUX module here) which takes in 2-bit inputs which are inp0,inp1,inp2,......,inp30 and take  5-bit selection line and produces an 2bit output

The values are assigned to the input port using

```bash
    SEL=30
    INP30=1
    //SEL and INP30 are variables which are local to testbench
    dut.inp30.value = INP30
    dut.sel.value = SEL
```
The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:

```bash
   cocotb.result.TestFailure: MUX failed with: input 01 and sel 11110 actual out was 01 but got 00
```


## Test Scenario

->Test Inputs: sel=30 inp30=1     
->Expected Output: out=inp30(which is 1)  
->Observed Output in the DUT dut.out=00 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug-1
Based on the above test input and analysing the design, we see the following

```
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
	  // line add error bug
      default: out = 0;
```
For the given design, the line should be added `5'b11110: out = inp30; `  
because when the case doesnt mentioned what should happen when sel line is given as 30  
it considers the default value which is `default: out = 0;`.

## bug1 in cocotb
![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/level1_design1_bug%20identification.png)

## Design Bug-2
Based on the above test input and analysing the design, we see the following

```
      5'b01101: out = inp12;
      5'b01101: out = inp13;
```
single selection line is assigned for the two inputs ``inp12`` and ``inp13``which creates an ambiguty


## Design Fix
Updating the design and re-running the test makes the test pass.

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/level1_design1_correct%20output.png)



The updated design is checked in as adder_fix.v
