from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class TeachingCrew(Crew):
      
  task_config  = "config\agents.yaml"
  agent_config = "config\tasks.yaml"
  
  @agent
  def sir_zia(self) -> Agent:
    return Agent(
        config=self.agent_config["sir_zia"],
    )
    
  @task
  def describe_topic(self) -> Task:
    return Task(
        config=self.task_config["describe_topic"],
    )
    
  @crew
  def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        verbose=True,
    )