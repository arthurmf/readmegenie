#!/usr/bin/env python
import os
from readmegenie.crew import ReadmegenieCrew

def run():
    """
        Execute the Readmegenie crew with user-defined inputs.
    """
    inputs = {
        'repository_url': os.getenv('GITHUB_REPO'),
        'project_files': 'project_files.md',
        'project_files_overview': 'project_files_overview.md',
    }
    ReadmegenieCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
