from crewai.flow import Flow, listen, start
from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyD4gRQkOAfWHix87V7Lo7fbms8OPdEJplE"

class LiteLmmFlow(Flow):
    
    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-1.5-flash", 
            messages=[
             {'role' : 'user',
             'content' :'Who is The Founder of Pakistan  ?'}   
            ])
        print("OutPut 😍😍😍" , output['choices'][0]['message']['content'])
        return output
    
# ✅ Move this outside the class    
def run_litellm_flow():
    obj  =  LiteLmmFlow()
    result = obj.kickoff()
    print(result)