import os
from github import Github

def check_pull_request_template():
    token = os.environ['GITHUB_TOKEN']
    repo_name = os.environ['GITHUB_REPOSITORY']
    pr_number = os.environ['PR_NUMBER']

    # Initialize GitHub client
    github_client = Github(token)
    repo = github_client.get_repo(repo_name)
    pr = repo.get_pull(int(pr_number))

    template_file = repo.get_contents("PULL_REQUEST_TEMPLATE.md")
    template_content = template_file.decoded_content.decode()

    # Check if all checkboxes are checked
    all_checked = all('- [x]' in template_content.split('\n'))

    if not all_checked:
        pr.create_issue_comment("Please make sure all checkboxes in the pull request template are checked.")
        # Optionally, you can label the PR, assign someone, etc.

if __name__ == "__main__":
    check_pull_request_template()
