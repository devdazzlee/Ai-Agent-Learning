from crewai22.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
_: bool = load_dotenv(find_dotenv())

class  PanaFlow(Flow):
    
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messege=[
                {
                "role" : "user",
                "content" : """
                        Generate a topic for blog post about 
                        the benifit of learning of Agentic Ai
                        """
                }
            ],
            max_token=100,
            temprature= 0.5
        )
        self.state['topic'] = response['choices'][0]['messege']['content']
        print(f"Step 1 Topic :{self.state['topic']}")

def kickoff():
    flow = PanaFlow()
    respose = flow.kickoff()
    print("RESPOSE" , respose)