# First Example
# This example demonstrates how to use the router and listen decorators in a flow.

import random
from crewai.flow.flow import Flow, listen, start, router
from pydantic import BaseModel

class RouteFlow(Flow):

    @start()
    def pakistan(self):
        print("Below are the cities of Pakistan")

    @router(pakistan)
    def selected_city(self):
        cities = ["karachi", "lahore", "islamabad", "peshawar", "quetta"]
        self.city = random.choice(cities)
        print("Selected city is:", self.city)
        if self.city == "karachi":
            return "karachi"
        if self.city == "lahore":
            return "lahore"
        if self.city == "islamabad":
            return "islamabad"
        if self.city == "peshawar":
            return "peshawar"
        if self.city == "quetta":
            return "quetta"

    @listen("karachi")
    def karachi1(self):
        print(f"Fun fact about {self.city}: It's the biggest city of Pakistan.")

    @listen("lahore")
    def lahore1(self):
        print(f"Fun fact about {self.city}: It's known as the heart of Pakistan.")

    @listen("islamabad")
    def islamabad1(self):
        print(f"Fun fact about {self.city}: It's the capital city of Pakistan.")

    @listen("peshawar")
    def peshawar1(self):
        print(f"Fun fact about {self.city}: It's one of the oldest cities in South Asia.")

    @listen("quetta")
    def quetta1(self):
        print(f"Fun fact about {self.city}: It's called the 'Fruit Garden of Pakistan'.")

def kickoff():
    flow = RouteFlow()
    flow.kickoff()


def plot():
    obj = RouteFlow()
    obj.plot()
    
    
    
    
#  Second Example

# import random
# from crewai.flow.flow import Flow, listen, router, start
# from pydantic import BaseModel

# class ExampleState(BaseModel):
#     success_flag: bool = False

# class RouterFlow(Flow[ExampleState]):

#     @start()
#     def start_method(self):
#         print("Starting the structured flow")
#         random_boolean = random.choice([True, False])
#         self.state.success_flag = random_boolean

#     @router(start_method)
#     def second_method(self):
#         if self.state.success_flag:
#             return "success"
#         else:
#             return "failed"

#     @listen("success")
#     def third_method(self):
#         print("Third method running")

#     @listen("failed")
#     def fourth_method(self):
#         print("Fourth method running")

# def kickoff():
#     flow = RouterFlow()
#     flow.kickoff()
    
# def plot():
#     obj = RouterFlow()
#     obj.plot()