from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool, FileReadTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure tools
file_writer = FileWriterTool(directory='output/')
file_reader = FileReadTool(directory='output/')

# Import custom tools
from readmegenie.tools.custom_tool import GitHubFileRetriever, GitHubFileContentRetriever

# Initialize custom tools
github_file_retriever = GitHubFileRetriever()
github_content_retriever = GitHubFileContentRetriever()

@CrewBase
class ReadmegenieCrew:
    """Define the Readmegenie crew."""

    @agent
    def github_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['github_researcher'],
            tools=[github_file_retriever, file_writer],
            llm=os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini'),
            verbose=True,
            max_iter=3,
            max_rpm=100,
        )

    @agent
    def github_code_interpreter(self) -> Agent:
        return Agent(
            config=self.agents_config['github_code_interpreter'],
            tools=[github_content_retriever, file_writer],
            llm=os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini'),
            verbose=True,
            max_iter=3,
            max_rpm=100,
        )

    @agent
    def documentation_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_writer'],
            tools=[file_reader],
            llm=os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini'),
            verbose=True,
            max_iter=3,
            max_rpm=100,
        )

    @task
    def repository_research_task(self) -> Task:
        return Task(config=self.tasks_config['repository_research_task'])

    @task
    def github_code_interpreter_task(self) -> Task:
        return Task(config=self.tasks_config['github_code_interpreter_task'])

    @task
    def readme_creation_task(self) -> Task:
        return Task(config=self.tasks_config['readme_creation_task'])

    @crew
    def crew(self) -> Crew:
        """Create and configure the crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            #manager_llm=os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini'),
            verbose=True,
            planning=True,
            planning_llm=os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini'),
            memory=False, # Memory management is disabled
        )