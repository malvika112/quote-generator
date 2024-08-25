import os
from langchain_community.llms import Ollama

# Set environment variable for API key if needed
# os.environ["OPENAI_API_KEY"] = "NA"

# Initialize the LLM with correct base URL and model
llm = Ollama(
    model="llama2",
    base_url="http://localhost:11434"  # Ensure this URL is correct
)

# Define the Agent class
class Agent:
    def __init__(self, role, goal, backstory, allow_delegation, verbose, llm):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.allow_delegation = allow_delegation
        self.verbose = verbose
        self.llm = llm

    def perform_task(self, task):
        try:
            # Generate the article using the LLM
            prompt = f"Generate an inspiring quote along with the author's name and relevant hashtags."
            response = self.llm.predict(prompt)
            result = response.strip()  # Clean up the response

            # Ensure the result is not empty
            if not result:
                result = "Generated quote is too short. Please try again."
        except Exception as e:
            result = f"Error: {e}"

        if self.verbose:
            print(f"{self.role} is performing the task: {task.description}")

        return result

# Define the Task class
class Task:
    def __init__(self, description, agent, expected_output):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output

# Define the Crew class
class Crew:
    def __init__(self, agents, tasks, verbose):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose

    def kickoff(self):
        results = {}
        for task in self.tasks:
            result = task.agent.perform_task(task)
            results[task.description] = result
        return results

# Create the content agent
content_agent = Agent(
    role="Quote Generator",
    goal="Generate a thought or inspiring quote",
    backstory="You are an expert quote writer with the ability to create detailed and informative articles.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Create a task
task = Task(
    description="Generate an inspiring quote",
    agent=content_agent,
    expected_output="Thoughtful quote along with the author's name and relevant hashtags."
)

# Initialize the crew with agents and tasks
crew = Crew(
    agents=[content_agent],
    tasks=[task],
    verbose=True
)

# Start the crew and get the result
result = crew.kickoff()
for task_description, quote in result.items():
    print(f"task: {task_description}")
    print(f"generated: {quote}")
