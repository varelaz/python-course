class Operation:
    def apply(self, current):
        raise NotImplementedError()

    def revert(self, current):
        raise NotImplementedError()


class Add(Operation):
    def __init__(self, value):
        self.value = value

    def apply(self, current):
        return self.value + current

    def revert(self, current):
        return self.value - current


class Sub(Operation):
    def __init__(self, value):
        self.value = value

    def apply(self, current):
        return current - self.value

    def revert(self, current):
        return current + self.value


class Mul(Operation):
    def __init__(self, value):
        self.value = value
        self.original_value = None

    def apply(self, current):
        if self.value == 0:
            self.original_value = current

        return current * self.value

    def revert(self, current):
        if self.original_value is not None:
            return self.original_value
        return current / self.value


class Div(Operation):
    def __init__(self, value):
        self.value = value

    def apply(self, current):
        return current / self.value

    def revert(self, current):
        return current * self.value


class ExpressionWithHistory:
    def __init__(self, value):
        self.operations = []
        self.op_index = 0
        self.value = value

    def execute(self, operation):
        if not isinstance(operation, Operation):
            raise ValueError("Operation required")

        self.operations = self.operations[:self.op_index]
        self.op_index += 1
        self.operations.append(operation)
        
        self.value = operation.apply(self.value)

    def back(self):
        if self.op_index > 0:
            operation = self.operations[self.op_index-1]
            self.value = operation.revert(self.value)
            self.op_index -= 1

    def forward(self):
        if self.op_index < len(self.operations):
            self.op_index += 1
            operation = self.operations[self.op_index-1]
            self.value = operation.apply(self.value)


exp = ExpressionWithHistory(0)
print("Current value,", exp.value)

exp.execute(Add(10))
print("Add 10,", exp.value)

exp.execute(Sub(3))
print("Sub 10,", exp.value)

exp.execute(Mul(3))
print("Mul 3,", exp.value)

exp.back()
print("Back,", exp.value)

exp.back()
print("Back,", exp.value)

exp.forward()
print("Forward,", exp.value)

exp.forward()
print("Forward,", exp.value)

