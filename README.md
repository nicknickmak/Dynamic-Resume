# Project Goal

Generate a customized resume by filtering relevant experience from a YAML file based on a given job description using an LLM.

## System Architecture Overview:

- INPUTS:

  - dynamic-resume.yml (all my experience)
  - [job-description.txt] (the job description to apply for)
  - resume_template.html (the template to fill out)
  - styles.css (decoration/formatting)

- PROCESS:

  1. Load and parse YAML (experience)
  2. Read the job description
  3. Use LLM to rank or selecte relevant experience from YAML
  4. Render selected experiences into the HTML template
  5. Output COMPANY_resume.html

- OUTPUT
  - COMPANY_resume.html
    - this can be printed as a PDF and sent to application.

## Requirements

- Information must be accurate and true
- Resume must fit 1 page
- Resume must look nice and not too sparse
- Most recent job must be included
- Must use LLM
- Resume must make autofilling easy for at least 3 different companies/systems
  - workday
  - Microsoft

## Optional Features

- LLM can alter text to be better
- Allow options for choosing different items to add
- Generate a cover letter/template based off job description and resume
- Warning if a job requires skills that I don't have


## Setup
Start by running:
    
    \.install-requirements.bat

Make sure you get the .env file from the owner.
- This includes important secrets like the OpenAI API Key and prompts

Finally run:

    python .\resume-builder.py
