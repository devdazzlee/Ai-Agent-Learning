from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import os

# Get the GEMINI API key
GEMINI_API_KEY = 'AIzaSyAx9MTfyN-k-WLnH0Zl-E9rW2sxSN8tM9c'

# Create a knowledge source
content = """
                Hi, I’m Ahmed Raza, a dedicated and creative Full Stack Developer from Karachi, Pakistan—a vibrant city that never sleeps and the tech hub of the country. I specialize in the MERN Stack (MongoDB, Express.js, React.js, Node.js) and have been crafting web solutions for over 3 years now, building everything from sleek user interfaces to complex back-end systems.
                Growing up in Karachi, I was always fascinated by technology. The fast-paced city life, filled with opportunities and challenges, shaped my passion for problem-solving. My journey into web development began during my college years, where I initially dabbled in basic websites and quickly fell in love with coding. That passion soon transformed into a full-time career.
                Over the years, I’ve had the chance to work with startups, mid-sized businesses, and remote teams across various domains. Whether it's building real-time chat applications, secure e-commerce stores, or API integrations with third-party services like Square and Firebase, I bring strong architectural thinking, performance optimization, and a user-first mindset to every project.
                I believe in continuous growth. I'm constantly learning new tools, frameworks, and technologies to stay ahead of the curve. Some of the tools and stacks I frequently work with include:
                Frontend: React.js, Redux Toolkit, Tailwind CSS, Material UI
                Backend: Node.js, Express.js, Firebase Admin SDK, JWT
                Databases: MongoDB, Firebase Firestore
                Dev Tools: Git, GitHub, Postman, Thunder Client, Vercel
                Real-Time & Cloud: Socket.IO, Firebase Cloud Functions, Cloud Storage
                3rd Party APIs: Easyship, Square Payments, and more
                I am also the founder of Galaxy Digital Solution, where I provide a wide range of services including web and mobile app development, UI/UX design, digital marketing, and AI-based solutions. Through this venture, I aim to help businesses grow by building scalable, modern, and efficient digital products.
                Beyond code, I’m someone who enjoys a balanced lifestyle. I love reading about technology trends, mentoring new developers, and brainstorming product ideas. I also enjoy spending time with my family, exploring Karachi's local food scene, and occasionally watching tech documentaries or movies.
                My goal is to create meaningful software that solves real-world problems, while contributing to a company or a mission that values innovation, growth, and collaboration.
                Ahmed is 19 year old """
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)
def kickoff():
    result = crew.kickoff(inputs={"question": "What city does Ahmed Raza  live in and how old is he and what he do ?"})
    print(result)
