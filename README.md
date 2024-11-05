# GitHub Activity CLI

A command-line interface (CLI) tool to fetch and display recent GitHub activity for a specified user. It retrieves the most recent events via the GitHub API, providing details of each activity in a human-readable format. This project demonstrates handling API requests, JSON parsing, and command-line argument usage in Python.

## Features
- Fetch recent GitHub activity for a specified user.
- Optionally filter by event type (e.g., `PushEvent`, `WatchEvent`).
- Displays activity such as commits pushed, watched repositories, and issue comments.
- Graceful error handling for invalid usernames or network issues.

## Requirements
- Python 3.x
- Internet connection to access the GitHub API

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/github-activity-cli.git
   cd github-activity-cli

## Usage

To use this CLI tool, run the Python script from the command line, passing the GitHub username as the required argument. Optionally, you may include a specific event type to filter results.

```bash
python main.py <username> [event_type]

##project from: https://roadmap.sh/projects/github-user-activity

