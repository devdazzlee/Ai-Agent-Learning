from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew
from typing import ClassVar, List
from pathlib import Path


class TeachingCrew(CrewBase):
      
  task_config: ClassVar[str] = "config\agents.yaml"
  agent_config: ClassVar[str] = "config\tasks.yaml"
  base_directory: ClassVar[Path] = Path(__file__).parent
  original_agents_config_path: ClassVar[str] = 'config/agents.yaml'
  original_tasks_config_path: ClassVar[str] = 'config/tasks.yaml'
  
  def __init__(self):
    self._sir_zia = Agent(
        role="Teacher",
        goal="Teach complex topics in a simple way",
        backstory="Expert educator with years of experience in teaching complex subjects",
        verbose=True
    )
    
    self._describe_topic = Task(
        description="Describe the given topic in detail",
        agent=self._sir_zia,
        expected_output="A detailed explanation of the topic"
    )
    
  @crew
  def crew(self):
    return Crew(
        agents=[self._sir_zia],
        tasks=[self._describe_topic],
        verbose=True
    )