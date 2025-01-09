# Git Commit Generator
###### (Created by claude)

A Python script to generate a realistic pattern of git commits for testing and development purposes. The script creates commits with timestamps spread across the past year, following a natural daily activity pattern.

## Features

- Generates commits spanning exactly one year from the current date
- Creates 1-5 random commits per day
- Commits are timestamped between 10 AM and 10 PM
- Maintains chronological order within each day
- Automatically initializes git repository if needed
- Sets up default git configuration if not present

## Requirements

- Python 3.x
- Git installed and accessible from command line

## Installation

1. Clone or download this repository
2. Place the script in your target git repository directory

## Usage

1. Navigate to your repository directory
2. Run the script:
```bash
python git_commit_generator.py
```

The script will automatically:
- Initialize a git repository if one doesn't exist
- Create an activity.txt file to track commits
- Generate commits with random timestamps
- Display progress as commits are created

## Output

- Creates an activity.txt file with timestamped entries
- Each commit includes the exact timestamp in its message
- Commits are distributed throughout the day (10 AM - 10 PM)
- Repository history will show regular activity over the past year

## Important Notes

This script is intended for testing and development purposes only. Please use responsibly:

- Do not use to misrepresent actual development activity
- Consider ethical implications before pushing to public repositories
- Be aware that artificially inflating contribution graphs may violate terms of service of hosting platforms

## Customization

To modify the script's behavior, you can adjust the following parameters in the code:

- Time range (currently 10 AM - 10 PM)
- Number of commits per day (currently 1-5)
- Date range (currently 1 year)
- Commit message format

## License

This project is released under the MIT License. Feel free to modify and distribute while maintaining attribution.

## Contributing

Feel free to submit issues and enhancement requests!
