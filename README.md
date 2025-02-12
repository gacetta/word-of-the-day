# Word of the Day Scraper with GitHub Actions Automation

This project is a practice tool designed to scrape the [Merriam-Webster Word of the Day](https://www.merriam-webster.com/word-of-the-day/) website daily, format the data into Markdown, and append it to an existing file in the repository. The updated file is then committed and pushed back to the repository automatically using GitHub Actions.

## Features

- **Web Scraping**: Collects the following details from Merriam-Webster's Word of the Day page:
  - Word
  - Definition
  - Part of Speech
  - Syllables
  - Link to the full definition
- **Markdown Formatting**: Formats the scraped data into clean Markdown and appends it to an existing `.md` file.
- **Automation**: Uses GitHub Actions with a cron job to schedule daily execution at **14:00 UTC (6:00am pacific)**.
- **Commit and Push**: Automatically commits and pushes changes back to the repository.

## Technologies Used

- **Python**: Core programming language for scraping and formatting.
- **BeautifulSoup**: For HTML parsing and web scraping.
- **Requests**: For making HTTP requests.
- **GitHub Actions**: For scheduling and automating the workflow.

## Installation

To set up and run this project locally:

1. Clone this repository:
    ```
    git clone https://github.com/your_username/word-of-the-day-scraper.git
    cd word-of-the-day-scraper
    ```

2. Create a virtual environment (optional but recommended):
    ```
    python3 -m venv .venv
    source .venv/bin/activate  
    # On Windows: 
    .venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the script manually:
    ```
    python3 scrape_word.py
    ```

## Usage

### Automatic Execution via GitHub Actions

The workflow is set up to run automatically every day at **14:00 UTC** using GitHub Actions. The cron job is defined in `.github/workflows/scrape_word.yml`.

### Running Locally

To run locally, ensure you have Python installed, activate your virtual environment, install dependencies, and execute the script as shown in the installation steps.

### Example Output in Markdown

The scraper appends data like this to your Markdown file:

---

###### *Feb 11, 2025*
### [ruminate](https://www.merriam-webster.com/dictionary/ruminate)
<small>*verb*</small> | <small>ROO-muh-nayt</small>

To ruminate is to think carefully and deeply about something.

----

