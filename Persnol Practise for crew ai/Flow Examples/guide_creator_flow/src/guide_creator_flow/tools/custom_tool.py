from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

import os

os.environ["GEMINI_API_KEY"] = "AIzaSyCulHojov19SEEIY-VXw4TXcyQhboKhZEQ"
os.environ["MODEL"] = "gemini/gemini-1.5-flash"

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
