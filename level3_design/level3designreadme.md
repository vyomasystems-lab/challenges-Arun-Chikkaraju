# level3 (32-bit ALU) Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

My Gitpod id with the screenshot


## Screenshots

![App Screenshot](https://github.com/Arun-Chikkaraju/vyoma-arun/blob/main/gitpod%20home%20screen.png)

## Description
The design will perform some of the arithmetic and logical operations which deals with 32bit data and the instruction based on the 
instruction the specified operation will be done and the output is stored in the 32bit register

This design consists of 16 commands or instructions which are :

![App Screenshot](d31)


## Verification of the design

  As part of the level3 design we should insert some bugs in our design and capture them using cocotb we have to do the makefile as well
  for each command seperate test function is written and identified for the bug
  
  Bug1:
  
  for the AND logical operation which holds an instruction 1010 there is a bug
  ![App Screenshot](d32)
  
  The reason for this is:
  
  ```bash
  module AND_gate(A, B, Out); //AND gate
  input [31:0] A;
  input [31:0] B;
  output [31:0] Out;
  assign Out = (A & (~B));    <== bug here
endmodule
    
  ```
  for the AND operation output should be A&B but we are getting instead ((A & (~B)) 
  
  Bug2:
  
  for the SUB operation we can observe output wrong which is instruction 0010 
  
  ![App Screenshot](d33)
  
  The reason for this is:
  
  ```bash
  module SUB_er(A, B, Out);//subtractor
  input [31:0] A;
  input [31:0] B;
  output [7:0] Out; <==bug here
  reg [32:0] SUB_local;                
  always @(*) begin
    SUB_local = B-A;
  end
  assign Out = SUB_local[32:0];
endmodule
    
  ```
  The functionality of the subraction is correct but out of 32 bits only 8bits from the out is driven to the DUT
  
  
  Bug3:
  
  for the modulo operation in which instruction is 0101 there is a difference between the expected and actual output
  
  ![App Screenshot](d34)
  
   The reason for this is:
  
  ```bash
  module DIV_er(A, B, Out, Remainder);//divider/remainder
  input [31:0] A;
  input [31:0] B;
  output [31:0] Out;
  output [31:0] Remainder;
  reg [31:0] DIV_local;
  reg [31:0] REMAIN_local;
  always @(*) begin
    DIV_local = B/A;
    REMAIN_local = A%A;          <=== bug here
  end
  assign Out = DIV_local[31:0];
  assign Remainder = REMAIN_local[31:0];
endmodule
    
  ```
  instead of A%B it performing A%A
  
  
## conclusion 

The design3 was sucessfully verified and the bugs were identified using cocotb platform
