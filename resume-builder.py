import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("dynamic-resume.yml", "r") as file:
    data = yaml.safe_load(file)


# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('resume_template.html')

# Render the template with YAML data
output = template.render(data)

# Save the generated HTML
with open("resume.html", "w") as f:
    f.write(output)

print("Resume generated successfully!")