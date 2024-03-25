import requests
import os
import sys

def copy_workflow_logs(repo_owner, repo_name, run_id, output_folder):
    # GitHub API endpoint for fetching workflow run logs
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}/logs"
    
    # Fetch logs using GitHub API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a folder for logs if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Write logs to a new file
        log_file_path = os.path.join(output_folder, f"workflow_logs_{run_id}.txt")
        with open(log_file_path, "w") as f:
            f.write(response.text)
        
        print(f"Workflow logs copied successfully to: {log_file_path}")
    else:
        print(f"Failed to fetch logs. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python copy_logs.py [REPO_OWNER] [REPO_NAME] [RUN_ID] [OUTPUT_FOLDER]")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    run_id = sys.argv[3]
    output_folder = sys.argv[4]

    copy_workflow_logs(repo_owner, repo_name, run_id, output_folder)