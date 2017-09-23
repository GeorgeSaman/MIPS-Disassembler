
# MIPS DISASSEMBLER
######################################
# GEORGE SAMAN                       #
# EMAIL: george.issa.saman@gmail.com #
######################################

# ENTER YOUR FILE NAME CONTAINING THE OBJECTCODE (MACHINE CODE)
myfilename = "objcode.txt"   


def read_Instructions(filename):
    array = []
    infile = open(filename,"r") # create a handle
    lines  = infile.readlines() # lines is a list.
    for line in lines:
        fields = line.split()    # split list into smaller lists with space as a seperator
        objcode_string = fields[1] # take the objcode
        objcode = int(objcode_string,16) # convert to integer, convert from base = 16 
        array.append(objcode)
   
    infile.close()
    return array

TLB = {0 : "mfc0",
       2 : "cfc0",
       4 : "mtc0",
       6 : "ctc0"
}
    
    
funct_dict = {0b000000: "sll",  #00
              0b000010: "srl",  #02
              0b000011: "sra",  #03
              0b000100: "sllv", #04
              0b000110: "srlv", #06
              0b000111: "srav", #07
              
              0b001000: "jr",  #10
              0b001001: "jalr",#11
              0b001100: "syscall",#14
              0b001101: "break",#15
              
              0b010000: "mfhi", #20
              0b010001: "mthi", #21
              0b010010: "mflo", #22
              0b010011: "mtlo", #23
        
              0b011000: "mult", #30
              0b011001: "multu",#31
              0b011010: "div",  #32
              0b011011: "divu", #33
              
              0b100000: "add",  #40
              0b100001: "addu", #41
              0b100010: "sub",  #42
              0b100011: "subu", #43
              0b100100: "and",  #44
              0b100101: "or",   #45
              0b100110: "xor",  #46
              0b100111: "not",  #47
              
              
              0b101010: "slt", #52
              0b101011: "sltu" #53
              
        }

regs_dict = {0 : "$zero",
             1 : "$at",
             2 : "$v0",
             3 : "$v1",
             4 : "$a0",
             5 : "$a1",
             6 : "$a2",
             7 : "$a3",
             8 : "$t0",
             9 : "$t1",
             10: "$t2",
             11: "$t3",
             12: "$t4",
             13: "$t5",
             14: "$t6",
             15: "$t7",
             16: "$s0",
             17: "$s1",
             18: "$s2",
             19: "$s3",
             20: "$s4",
             21: "$s5",
             22: "$s6",
             23: "$s7",
             24: "$t8",
             25: "$t9",
             26: "$k0",
             27: "$k1",
             28: "$gp",
             29: "$sp",
             30: "$fp",
             31: "$ra"
             
            }
opcode_type = {
    0b000000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print(funct_dict[function]," ",regs_dict[rd],",",regs_dict[rs],",",regs_dict[rt],","),
    0b000001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("bltz"," ",regs_dict[rs],",",imm,"(",regs_dict[rt],")"),
    0b000010 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("jump", " ",targetAddress),
    0b000011 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("jal", " ",targetAddress),
    0b000100 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("beq", " ",regs_dict[rs],",",regs_dict[rt],",",imm),
    0b000101 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("bne", " ",regs_dict[rs],",",regs_dict[rt],",",imm),
    0b000110 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("blez", " ",regs_dict[rs],",",imm,"(",regs_dict[rt],")"),
    0b000111 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("bgtz", " ",regs_dict[rs],",",imm,"(",regs_dict[rt],")"),
    
    0b001000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("addi"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("addiu"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001010 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("slti"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001011 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("sltiu"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001100 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("andi"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001101 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("ori"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001110 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("xori"," ",regs_dict[rt],",",regs_dict[rs],",",imm),
    0b001111 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lui"," ",regs_dict[rt],",",imm),
    
   # TLB and FlTp
    #0b010000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print(TLB[rs],",",imm),
    
   #0b010001 : FlPt(funtion,shamt,rd,rs,rt,imm,targetAddress),
   
    0b100000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lb"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b100001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lh"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b100010 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lwl"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b100011 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lw"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b100100 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lbu", " ",regs_dict[rs],",",regs_dict[rt],",",imm),
    0b100101 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lhu", " ",regs_dict[rs],",",regs_dict[rt],",",imm),
    0b100110 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lwr"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    
    0b101000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("sb"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b101001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("sh"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b101010 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("swl"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b101011 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("sw"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b101110 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("swr", " ",regs_dict[rs],",",regs_dict[rt],",",imm),
  
    0b110000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("ll"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b110001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("lwcl"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
   
    0b111000 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("sc"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")"),
    0b111001 : lambda function, shamt, rd, rs, rt, imm, targetAddress :print("swcl"," ",regs_dict[rt],",",imm,"(",regs_dict[rs],")")
    
    
    
}

######## START OF MAIN LOOP ########################
  
instructions = read_Instructions(myfilename) # returns an array of the objcode of all instructions in integer
for instr in instructions:
    print(format(instr,'#032b'))          # print them in hex
    op = instr >> 26                      # right left 26 bits to get ***OPCODE***
    function = instr & 0x3F               # to take the first 6 bits 0011 1111 ***FUNCTION***
    shamt  = (instr >> 6) & 0x1F          # Masked with 0001 1111    ***SHAMT***
    rd     = (instr >> 11) & 0x1F         # Masked with 0001 1111    ***rd***
    rt     = (instr >> 16) & 0x1F         # Masked with 0001 1111    ***rt***
    rs     = (instr >> 21) & 0x1F         # Masked with 0001 1111    ***rs***
    imm    = instr & 0xFFFF               # Masked with 1111 1111    **address/immediate**
    signBit= imm >> 15
    if (signBit == 1):
        imm = imm - (instr & 0x10000)     # convert it to a negative number
    targetAddress = instr & 0x3FFFFFF     # Masked with 0X3FFFFFF    **targetAddress for Jump instructions**
    opcode_type[op](function, shamt, rd, rs, rt, imm, targetAddress)
     
            
######## END OF MAIN LOOP ############################

    
