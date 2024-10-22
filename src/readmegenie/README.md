# **ReadMeGenie CrewAI Project**

Welcome to the **ReadMeGenie CrewAI** project! This project leverages the **CrewAI framework** to build a multi-agent system that reads a GitHub repository, interprets the content of its files, and generates a detailed **README.md** file automatically.

## **Project Overview**

The **ReadMeGenie Crew** consists of specialized AI agents with distinct roles that collaborate to analyze a given GitHub repository. The agents work together to:
1. **List all the files** in the repository.
2. **Retrieve the content** of these files directly from the repository.
3. **Generate a comprehensive project overview** and write it into a `README.md`.

The primary objective of this project is to automate the documentation process by generating detailed and informative markdown files for any codebase.

---

## **Project Structure**

The project is organized as follows:

```
readmegenie/
├── config/
│   ├── agents.yaml       # Defines the agents and their roles
│   ├── tasks.yaml        # Defines the tasks assigned to each agent
├── tools/
│   └── custom_tool.py    # Custom tools for interacting with GitHub repositories
├── crew.py               # Main CrewAI configuration and agent logic
├── main.py               # Entry point to run the crew
├── output/               # Output folder where results (e.g., README.md) are saved
└── .env                  # Environment variables. Includes: GITHUB_REPO, OPENAI_API_KEY and GH_TOKEN
```

---

## **Installation**

### **Prerequisites**
- Python **3.12** (Ensure compatibility with CrewAI)
- **Poetry** (for dependency management)
- **CrewAI framework**

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd readmegenie
   ```

2. **Install Dependencies**
   Using **Poetry** to install dependencies:
   ```bash
   poetry install
   ```


3. **Set up Environment Variables**
   Create a `.env` file with the following content:
   ```bash
   GITHUB_REPO=<owner/repo_name>  # Replace with the target GitHub repository
   OPENAI_API_KEY=sk-<your-openai-api-key>
   GH_TOKEN=<github_pat_TOKEN>
   ```

---

## **Usage**

1. **Configure Agents and Tasks**

   - Modify `config/agents.yaml` to adjust the agents' behavior and tools.
   - Modify `config/tasks.yaml` to define tasks and workflows.

2. **Run the Crew**
   Use the following command to **start the crew** and kick off the agents:
   
   ```bash
   crewai run
   ```

3. **Expected Output**

   The generated **README.md** and detailed file overviews will be saved in the `output/` folder.

---

## **How It Works**

1. **Agent: GitHub Repository Researcher**
   - **Goal:** Retrieve and list all files from the specified GitHub repository.
   - **Tools Used:** `GitHubFileRetriever` and `FileWriterTool`

2. **Agent: GitHub Code Interpreter**
   - **Goal:** Fetch the content of each file, interpret it, and write a comprehensive overview.
   - **Tools Used:** `GitHubFileContentRetriever` and `FileWriterTool`

3. **Agent: Documentation Writer**
   - **Goal:** Read the file overviews and create a detailed **README.md**.
   - **Tools Used:** `FileReadTool`

### **Custom Tools**

The project includes two **custom tools**:
1. **GitHub File Retriever:** Fetches all file paths from the main branch of a repository.
2. **GitHub File Content Retriever:** Retrieves the content of individual files from the repository.

---

## **Example Workflow**

1. **GitHub Repository Researcher** retrieves the following files:
   ```
   .gitignore, README.md, src/handler.py, src/helpers/aws_wrangler.py, etc.
   ```

2. **GitHub Code Interpreter** fetches and analyzes these files to produce:
   ```
   - .gitignore: Specifies files to ignore in version control.
   - handler.py: Main application logic for handling requests.
   - aws_wrangler.py: Helper functions for AWS operations.
   ```

3. **Documentation Writer** creates the following `README.md`:
   ```markdown
   # Project Overview
   This project contains scripts and tools for handling AWS operations...

   ## Installation
   pip install requirements.txt

   ## Usage
   Run the main handler script using...
   ```

---

## **Customization**

- **Agents and Tasks:** Modify the configuration files (`agents.yaml`, `tasks.yaml`) to change the behavior of agents or create new tasks.
- **Tools:** Add new tools by implementing them in the `tools/` folder. For more on creating custom tools, see [CrewAI documentation](https://docs.crewai.com/how-to/create-custom-tools).

---

## **Side Notes and Learnings**

Got it! Here's the corrected version of the **"Side Notes and Learning"** section:

---

## **Side Notes and Learning**

- **Custom Tool Development:**  
   I initially tried using the [GitHubSearchTool](https://docs.crewai.com/tools/githubsearchtool) from CrewAI in multiple ways, but after spending almost an entire day without success, I decided to build my own custom tool to handle file retrieval from GitHub.

- **Exploring Open-Source Models:**  
   I intended to experiment with open-source models like **Together AI** and **Groq**, but I encountered difficulties due to the limited depth of CrewAI’s documentation—particularly in the areas of **tools** and **LLM providers**. The lack of comprehensive examples made it challenging to explore alternative models effectively.

- **First Version Challenges:**  
   This project is just the **first version**, and there are still many areas for improvement in terms of **agent behavior** and **output consistency**.

- **Output Variability:**  
   One key observation is that the **output varies between executions**, even with identical inputs. Running the system multiple times can result in **different README.md files**, highlighting the non-deterministic nature of LLMs and the multi-agent system.

- **Agent-Task Prompting Complexity:**  
   A significant challenge was aligning **Agent and Task prompts** to ensure the agents performed as intended. Crafting precise prompts to guide the agents toward the desired behavior required a lot of experimentation, and even then, the output did not always align perfectly with expectations.

---

## **Contributing**

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## **Support**

If you have any questions or need help, feel free to reach out.

---

## **Acknowledgments**

Thanks to the **CrewAI** team for creating a robust framework for building multi-agent systems.

---