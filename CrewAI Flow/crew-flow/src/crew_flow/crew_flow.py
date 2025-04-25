from crewai.flow.flow import Flow, start, listen 
from litellm import completion
import time

# Chaining prompted Which Run one by one first run first then next.

API_KEY = "AIzaSyD4gRQkOAfWHix87V7Lo7fbms8OPdEJplE"

class CityFunFact(Flow):
    
    @start()
    def generate_random_city(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{ "role" : "user",
                       "content": "Generate 12 Areas of karachi name."}]
        )
        result = response["choices"][0]["message"]["content"]
        print("City Name: ", result)
        return result
    
    @listen(generate_random_city)
    def generate_fun_fact(self, area_name):
        response  = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{ "role" : "user",
                       "content": f"Generate a fun fact about {area_name} area with emojis."}]
        )
        result = response["choices"][0]["message"]["content"]
        print("Fun Fact: ", result)
        self.state["fun_fact"] = result
        
    @listen(generate_fun_fact)
    def save_fun_fact(self): 
        print("Saving Fun Fact...")
        with open("fun_facts.txt", "w" , encoding="utf-8") as file:
            file.write(self.state["fun_fact"])
        return self.state["fun_fact"]
        
def kick_off():
    obj = CityFunFact()
    data = obj.kickoff()
    print("Data: ", data)