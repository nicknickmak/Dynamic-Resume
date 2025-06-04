import openai
import yaml
from jinja2 import Environment, FileSystemLoader, Template

# Open AI API Key
openai.api_key = "MY OPENAI API KEY"

# Load YAML data
def load_experience(path):
    with open(path, "r") as file:
        return yaml.safe_load(file)

data = load_experience("dynamic-resume.yml")

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('resume_template.html')

# Render the template with YAML data
output = template.render(data)

# Save the generated HTML
with open("resume.html", "w") as f:
    f.write(output)

print("Resume generated successfully!")