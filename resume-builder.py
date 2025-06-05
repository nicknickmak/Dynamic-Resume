from openai import OpenAI
import yaml
from jinja2 import Environment, FileSystemLoader, Template
from dotenv import load_dotenv
import os

load_dotenv()

# Open AI API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

"""
Loads a YAML file of experiences
@param path - path name to YAML file of experiences
"""
def load_experience_yaml(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)
    
"""
Returns the loaded the Job Description txt file
@param path - path name to txt file of the job description
"""
def load_jd_text(path):
    with open(path, "r") as file:
        return file.read()

"""
Filter the given experiences with the input job description using open AI
Return only the filtered experiences
"""
def filter_experience_with_openai(job_description, experiences_dict):

    # convert to YAML formatted string
    experiences_string = yaml.dump(experiences_dict)
    
    template = os.getenv("FILTER_EXPERIENCE_PROMPT")
    prompt = template.format(
        job_description=job_description,
        experiences_string=experiences_string
    )

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[        
        {"role": "user", "content": prompt}
    ],
    temperature=0.2)
    return response.choices[0].message.content

"""
Formats the given content dictionary to our set html format and writes the file.
"""
def create_resume(template, content_dictionary, template_path):
    html = template.render(content_dictionary)
    with open(template_path, 'w') as file:
        file.write(html)
    print("✅ Generated resume.html with filtered experiences!")

def main():
    # Load files
    job_description = load_jd_text("job_description.txt")
    all_experiences = load_experience_yaml("full_resume.yaml")

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('resume_template.html')

    # Filter with openAI
    filtered_yaml_str = filter_experience_with_openai(job_description, all_experiences)
    filtered_experiences_dictionary = yaml.safe_load(filtered_yaml_str)

    if not all_experiences['work_experience']:
        print('resume template is missing "work_experience" section')
    
    if not filtered_experiences_dictionary['work_experience']:
        print('filtered experiences is missing "work_experience" section')

    all_experiences['work_experience'] = filtered_experiences_dictionary['work_experience']

    # Output file
    create_resume(template, all_experiences, 'resume.html')


if __name__ == "__main__":
    main()