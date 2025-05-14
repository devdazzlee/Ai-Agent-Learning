#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from guide_creator_flow.crews.poem_crew.poem_crew import PoemCrew
from guide_creator_flow.crews.story_crew.story_crew import StoryCrew


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class StoryState(BaseModel):
    paragraph_count: int = 1
    story: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)


class StoryFlow(Flow[StoryState]):
    @start()
    def generate_paragraph_count(self):
        print("Generating paragraph count")
        self.state.paragraph_count = randint(1, 3)

    @listen(generate_paragraph_count)
    def generate_story(self):
        print("Generating story")
        result = (
            StoryCrew()
            .crew()
            .kickoff(inputs={"paragraph_count": self.state.paragraph_count})
        )

        print("Story generated", result.raw)
        self.state.story = result.raw

    @listen(generate_story)
    def save_story(self):
        print("Saving story")
        with open("story.txt", "w") as f:
            f.write(self.state.story)


def kickoff():
    story_flow = StoryFlow()
    story_flow.kickoff()


def plot():
    story_flow = StoryFlow()
    story_flow.plot()


if __name__ == "__main__":
    kickoff()
