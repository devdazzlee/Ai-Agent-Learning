from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
from project4.crews.teaching_crew.teaching_crew import TeachingCrew

_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):
    
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[    
                {
                    "role": "user",
                    "content": "Write a Hot Topic in 2025 title only for most hot topic in the world."
                }
            ],
        )
        topic = response["choices"][0]["message"]["content"]
        self.state["topic"] = topic
        print(f"Generated topic: {topic}")
        return topic
    
    @listen("generate_topic")
    def generate_content(self):
        
        print(f"Generating content for topic")
        
        result = TeachingCrew().crew().kickoff(
            inputs={
             "topic": self.state["topic"]
            },
        )        
        print(f"Generating content result  {result.raw}")
        
def kickoff():
    flow = PanaFlow()
    response = flow.kickoff()
    print(f"Flow response: {response}")
