from crewai import Agent, Task, Crew, Process
import yaml
import os
from pathlib import Path
from typing import Dict, List
import logging
from .tools.ai_research_tools import ai_research_tool, ai_analysis_tool

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIResearchCrew:
    def __init__(self, config_path: str = "config/ai_research_config.yaml"):
        """Initialize the AI Research Crew with configuration."""
        self.config_path = config_path
        self.config = self._load_config()
        self.agents = {}
        self.tasks = []
        self._initialize_agents()
        self._initialize_tasks()

    def _load_config(self) -> Dict:
        """Load configuration from YAML file."""
        try:
            config_file = Path(__file__).parent / self.config_path
            with open(config_file, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            raise

    def _initialize_agents(self):
        """Initialize agents from configuration."""
        for agent_id, agent_config in self.config['agents'].items():
            # Create tools based on agent role
            tools = []
            if agent_id == 'ai_researcher':
                tools = [ai_research_tool]
            elif agent_id == 'ai_analyst':
                tools = [ai_analysis_tool]

            # Create the agent with tools
            self.agents[agent_id] = Agent(
                name=agent_config['name'],
                role=agent_config['role'],
                goal=agent_config['goal'],
                backstory=agent_config['backstory'],
                verbose=agent_config['verbose'],
                allow_delegation=agent_config['allow_delegation'],
                tools=tools
            )

    def _initialize_tasks(self):
        """Initialize tasks from configuration."""
        for task_id, task_config in self.config['tasks'].items():
            self.tasks.append(
                Task(
                    description=task_config['description'],
                    agent=self.agents[task_config['agent']],
                    expected_output=task_config['expected_output'],
                    context=task_config['context'],
                    output_file=task_config['output_file']
                )
            )

    def run_research(self) -> str:
        """Run the AI research crew and return the results."""
        try:
            crew = Crew(
                agents=list(self.agents.values()),
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True
            )

            result = crew.kickoff()
            logger.info("AI Research completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error running AI research: {str(e)}")
            raise

def main():
    """Main function to run the AI Research Crew."""
    try:
        research_crew = AIResearchCrew()
        results = research_crew.run_research()
        print("\nAI Research Results:")
        print(results)
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main() 