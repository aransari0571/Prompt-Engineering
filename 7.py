# 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
#7. Using Prompt Templates with f-Strings

def generate_flexible_prompt(action, subject, tone):
    prompt = f"Write a {tone} {action} about {subject}."
    return prompt

# Example inputs
action = "story"
subject = "the first human on Mars"
tone = "adventurous"

# Generate prompt
prompt = generate_flexible_prompt(action, subject, tone)
print("Generated Prompt:", prompt)
