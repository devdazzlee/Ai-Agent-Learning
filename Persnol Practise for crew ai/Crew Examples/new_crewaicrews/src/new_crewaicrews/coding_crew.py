from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

# Set up environment variables for the model
os.environ["GEMINI_API_KEY"] = "AIzaSyCulHojov19SEEIY-VXw4TXcyQhboKhZEQ"
os.environ["MODEL"] = "gemini/gemini-1.5-flash"

@CrewBase
class CodingCrew():
    """CodingCrew for handling Python development tasks"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/coderagent.yaml'    
    tasks_config = 'config/codertask.yaml' 

    @agent
    def python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['python_developer'],
            verbose=True
        )

    @agent
    def senior_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_developer'],
            verbose=True
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True
        )

    @task
    def python_coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['python_coding_task'],
        )

    @task
    def code_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_review_task'],
        )

    @task
    def code_testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_testing_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CodingCrew for Python development tasks"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
