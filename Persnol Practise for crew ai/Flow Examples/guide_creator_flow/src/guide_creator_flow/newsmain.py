#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from guide_creator_flow.crews.news_crew.news_crew import NewsCrew

import os

os.environ["GEMINI_API_KEY"] = "AIzaSyCulHojov19SEEIY-VXw4TXcyQhboKhZEQ"
os.environ["MODEL"] = "gemini/gemini-1.5-flash"

class NewsState(BaseModel):
    article_length: str = "medium"  # short, medium, or long
    news_article: str = ""


class NewsFlow(Flow[NewsState]):

    @start()
    def set_article_length(self):
        print("Setting article length")
        # Default to medium length, but you could make this dynamic
        self.state.article_length = "medium"

    @listen(set_article_length)
    def generate_news(self):
        print("Generating news article")
        result = (
            NewsCrew()
            .crew()
            .kickoff(inputs={"article_length": self.state.article_length})
        )

        print("News article generated", result.raw)
        self.state.news_article = result.raw

    @listen(generate_news)
    def save_news(self):
        print("Saving news article")
        with open("news_article.txt", "w") as f:
            f.write(self.state.news_article)


def kickoff():
    news_flow = NewsFlow()
    news_flow.kickoff()


def plot():
    news_flow = NewsFlow()
    news_flow.plot()


if __name__ == "__main__":
    kickoff()
