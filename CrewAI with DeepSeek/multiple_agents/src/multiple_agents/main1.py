from crewai.flow import Flow, start, listen
from multiple_agents.crews.dev_crew.dev_crew import DevCrew
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyD4gRQkOAfWHix87V7Lo7fbms8OPdEJplE"

class DevFlow(Flow):
    
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff( 
            inputs={
                "problem" : "Write a python code for two numbers"
            }
        )
        return output.raw
        
def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result) 
        