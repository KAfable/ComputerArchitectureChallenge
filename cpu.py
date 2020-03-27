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
        '''Loads a the next value into the indicated register.'''
        reg = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)
        self.register[reg] = value

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

    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        # mdr is normally a pointer to the register that stores the value, here it's the value itself
        self.ram[mar] = mdr
