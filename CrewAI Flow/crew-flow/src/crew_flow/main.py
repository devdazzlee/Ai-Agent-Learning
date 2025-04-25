from crewai.flow.flow import Flow, start, listen 
import time

# SimpleFlow is a class that inherits from Flow and defines a simple flow with three steps.
# Each step is defined as a method decorated with @start or @listen.
class SimpleFlow(Flow):

    @start()    
    def function_one(self):
        print("Step 1: Starting")
        time.sleep(2)

    @listen(function_one)        
    def function_two(self):
        print("Step 2: Listening")
        time.sleep(2)
        
    @listen(function_two)        
    def function_three(self):
        print("Step 3: Processing")
        time.sleep(2)
        
def kick_off():
    print("Crew Flow is starting...")
    print("Crew Flow is running...")
    obj = SimpleFlow()
    obj.kickoff()