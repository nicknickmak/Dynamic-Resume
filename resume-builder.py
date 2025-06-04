import yaml
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

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('resume_template.html')

# Render the template with YAML data
data = load_experience_yaml("full_resume.yaml")
output = template.render(data)

# Save the generated HTML
with open("resume.html", "w") as f:
    f.write(output)

print("Resume generated successfully!")