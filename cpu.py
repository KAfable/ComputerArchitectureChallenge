import sys

# register indexes
IM = 5
IS = 6
SP = 7

# op codes
HLT = 0b00000001
LDI = 0b10000010
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

# flag indexes
FL_L = -3
FL_G = -2
FL_E = -1


class CPU:
    def __init__(self):
        self.pc = 0
        self.ram = [0] * 256
        self.register = [0] * 8
        self.flag = [0] * 8
        self.branchtable = {
            HLT: self.op_HLT,
            LDI: self.op_LDI,
            CMP: self.op_CMP,
            JMP: self.op_JMP,
            JEQ: self.op_JEQ,
            JNE: self.op_JNE
        }

    def load(self, filename):
        try:
            with open(filename) as program:
                mar = 0
                for line in program:
                    instruction = line.split('#')[0].strip()
                    if instruction == '':
                        continue
                    else:
                        op_code = int(f"0b{instruction}", 2)
                        self.ram_write(mar, op_code)
                        mar += 1
        except FileNotFoundError:
            print("File not found, please verify you entered a correct filepath.")
            sys.exit(1)

    def run(self):
        # reset program count
        self.register[SP] = 0
        # run commands along the program count
        while True:
            instruction = self.ram_read(self.pc)
            if instruction in self.branchtable:
                self.branchtable[instruction]()
            else:
                sys.exit(1)

    def op_HLT(self):
        sys.exit(0)

    def op_LDI(self):
        '''Loads a the next value into the indicated register.'''
        reg = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)
        self.register[reg] = value

    def op_PRN(self):
        '''Prints the next value.'''
        value = self.ram_read(self.pc + 1)
        print(value)
        self.pc += 2

    def op_CMP(self):
        '''Compares the values in two given registers and adjusts equality flags accordingly.'''
        reg_a = self.ram_read(self.pc + 1)
        value_a = self.register[reg_a]

        reg_b = self.ram_read(self.pc + 2)
        value_b = self.register[reg_b]
        if value_a < value_b:
            self.flag[FL_L] = 1
            self.flag[FL_G] = 0
            self.flag[FL_E] = 0
        elif value_a > value_b:
            self.flag[FL_L] = 0
            self.flag[FL_G] = 1
            self.flag[FL_E] = 0
        else:
            self.flag[FL_L] = 0
            self.flag[FL_G] = 0
            self.flag[FL_E] = 1

    def op_JMP(self):
        '''Jumps to the register given'''
        self.pc += 1
        reg = self.ram_read(self.pc)
        self.pc = self.register[reg]

    def op_JEQ(self):
        '''Jumps to the register given if equal flag is true.'''
        if self.flag[FL_E]:
            self.op_JMP()
        else:
            self.pc += 2

    def op_JNE(self):
        if not self.flag[FL_E]:
            self.op_JMP()
        else:
            self.pc += 2

    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        # mdr is normally a pointer to the register that stores the value, here it's the value itself
        self.ram[mar] = mdr
