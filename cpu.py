# register indexes
IM = 5
IS = 6
SP = 7

# op codes
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
        self.branchtable = {
            LDI: self.op_LDI,
            CMP: self.op_CMP,
            JMP: self.op_JMP,
            JEQ: self.op_JEQ,
            JNE: self.op_JNE
        }

    def op_LDI(self):
        pass

    def op_PRN(self):
        pass

    def op_CMP(self):
        pass

    def op_JMP(self):
        pass

    def op_JEQ(self):
        pass

    def op_JNE(self):
        pass
