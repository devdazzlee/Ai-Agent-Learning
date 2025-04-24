from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyD4gRQkOAfWHix87V7Lo7fbms8OPdEJplE"

def gemini_llm():
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": "Write Come Crazy Jokes 😂😂😂."}]
    )
    print(response['choices'][0]['message']['content'])



def gemini_llm_second():
    response = completion(
        model="gemini/gemini-2.0-flash-exp", 
        messages=[{"role": "user", "content": "Founder of Pakistan ?"}]
    )
    print(response['choices'][0]['message']['content'])




def gemini_llm_third():
    response = completion(
        model="gemini/gemini-2.0-flash-exp", 
        messages=[{"role": "user", "content": "Founder of Pakistan ?"}]
    )
    print(response['choices'][0]['message']['content'])
