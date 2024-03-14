# GitHub Workflow: Pull Request Template Checklist

## Description

This GitHub workflow is designed to automatically check if a pull request includes a specific template file (`pull_request_template.md`) and if it contains all the required checkmarks. If the template is missing or incomplete, the workflow will fail, ensuring that all pull requests adhere to the project's guidelines.

## Workflow YAML

The workflow YAML file (`pull_request_template_check.yaml`)

1. **Check_template**: Checks if the `pull_request_template.md` file exists and contains all the required checkmarks.

## Usage

To use this workflow in your GitHub repository:

1. Copy the provided workflow YAML (`pull_request_template_check.yaml`) to your repository's `.github/workflows` directory.
2. Make sure your repository includes a `PULL_REQUEST_TEMPLATE.md` file with all the necessary checkmarks.
3. When a pull request is opened, the workflow will automatically run and verify the template.

## Contributing

If you have any suggestions or improvements for this workflow, feel free to open an issue or submit a pull request.

## Sample

<img width="500" alt="Screenshot 2024-03-15 at 12 24 38 am" src="https://github.com/Lenroy-Yeung/checklist_template/assets/86452090/6898de49-7530-4cba-94bf-d70cb8192704">

<img width="500" alt="Screenshot 2024-03-15 at 12 25 14 am" src="https://github.com/Lenroy-Yeung/checklist_template/assets/86452090/d3046174-e58b-4ea0-b94f-eddaa20a1562">

<img width="500" alt="Screenshot 2024-03-15 at 12 25 40 am" src="https://github.com/Lenroy-Yeung/checklist_template/assets/86452090/f2aede5e-e091-4966-8873-655f63fac81a">

