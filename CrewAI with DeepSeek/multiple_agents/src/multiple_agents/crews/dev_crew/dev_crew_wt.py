from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class  DevCrew:
    """Poem Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
          role="Junoir python developer",
          goal="write python code solution with out python type hints. for this problem '{problem}'",
          backstory="You have 3 years of experience in python web development experience you know how to use flask, django"
        )
        
        
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
          role="Senior python developer",
          goal=""" review the python code generate by junoir_python_developer for this problem '{problem}'
                    apply type hints
                    apply pydocs
                    write 3 pytest test for the code """,
          backstory=""" 
                        You have 20 years of experience in machine learning , deep learning , generate ai , and agentic ai
                        """
        )

    @task
    def write_code(self) -> Task:
        return Task(
           description="ou have to write python solution with out type hint for this problem '{problem}'",
           expected_output="return python code only",
           agent=self.junior_python_developer()
        )
        
    @task
    def review_code(self) -> Task:
        return Task(
            description=""" 
                            review the python code generate by junoir_python_developer for this problem '{problem}'
                            optimize the code
                            apply type hints
                            apply pydocs
                            write 3 pytest test for the code 
                            """,
           expected_output="return python code only",
           agent=self.senior_python_developer()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
