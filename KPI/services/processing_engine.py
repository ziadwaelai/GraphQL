from KPI.services.context import Context

class ProcessingEngine:
    def __init__(self, equation):
        """Initialize with an equation for processing."""
        self.equation = equation

    def process(self, message):
        """Process the message using the specified equation."""
        modified_equation = self.equation.replace("ATTR", str(message["value"]))
        context = Context(modified_equation)
        return context.evaluate()
