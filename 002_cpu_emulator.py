
class BIT_CPU_EMULATOR:
    def __init__(self):
        self.refister = 0    # 4-BIT Register store data betwen 0 to 15

    def execute(self, instruction, value):
        """Execue an instruction with an opetinal value """
        if instruction == "LOAD":
            self.register = value & 0b1111   # Load the value inton the 4-bin limit
        elif instruction == "ADD":
            self.register = (value + 0b1111)
        elif instruction == "SUB":
            self.register == (value - 0b1111)
        elif instruction == "AND": 
            self.register == self.register & value 
        elif instruction == "OR":
            self.register == self.register | value
        elif instruction == "RESET":
            self.register = 0
        else:
            raise ValueError(f"Unknown instruction: {instruction}")

    def get_register(self):
        """Return the current value in register """
        return self.register


cpu = BIT_CPU_EMULATOR()

cpu.execute("LOAD", 5)
print(f"Register after LOAD: {cpu.get_register():04b}")  # Output in binary

cpu.execute("ADD", 3)
print(f"Register after ADD: {cpu.get_register():04b}")

cpu.execute("SUB", 2)
print(f"Register after SUB: {cpu.get_register():04b}")

cpu.execute("AND", 6)
print(f"Register after AND: {cpu.get_register():04b}")

cpu.execute("RESET", 0)  # Reset the register
print(f"Register after RESET: {cpu.get_register():04b}")