from crewai import Agent, Task, Crew

class StoryCrew:
    def __init__(self):
        # Create a story writer agent
        self.story_writer = Agent(
            role='Story Writer',
            goal='Write engaging and creative stories',
            backstory='I am a creative writer who loves to tell stories',
            verbose=True
        )

    def crew(self):
        # Create a task for writing a story
        write_story = Task(
            description='Write a creative story with the given number of paragraphs',
            agent=self.story_writer
        )

        # Create the crew
        return Crew(
            agents=[self.story_writer],
            tasks=[write_story],
            verbose=True
        ) 