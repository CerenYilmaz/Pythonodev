class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
class BinaryGate(LogicGate):
    def __init__(self,n,a,b):
        LogicGate.__init__(self,n)
        self.pinA = a
        self.pinB = b
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n,a)
        self.pin = a
class AndGate(BinaryGate):
    def __init__(self,n,a,b):
        BinaryGate.__init__(self,n,a,b)
    def performGateLogic(self):
        a = self.pinA
        b = self.pinB
        if a==1 and b==1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
     def __init__(self,n,a,b):
        BinaryGate.__init__(self,n,a,b)
    def performGateLogic(self):
        a = self.pinA
        b = self.pinB
    if a==0 and b==0:
        return 0
    else:
        return 1
class XorGate(BinaryGate):
    def __init__(self,n,a,b):
        BinaryGate.__init__(self,n,a,b)
    def performGateLogic(self):
        a = self.pinA
        b = self.pinB
    if a==0 and b==1:
        return 1
    elif a==1 and b==0:
        return 1
    else:
        return 0
class NotGate(UnaryGate):
    def __init__(self,n,a):
        BinaryGate.__init__(self,n,a)
    def performGateLogic(self):
        a = self.pin
    if a==1:
        return 0
    else:
        return 1
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print "Cannot Connect: NO EMPTY PINS"
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate "+ \self.getName()+"-->")
        else:
            return self.pinA.getFrom().getOutput()




   
