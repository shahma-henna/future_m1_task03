import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("resumes.csv")

# Job role we are hiring for
job_role = "Python Developer"

# Required skills
required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Pandas",
    "NumPy"
]

# Function to calculate match percentage
def calculate_match(skills):
    candidate_skills = [skill.strip() for skill in skills.split(";")]

    matched = 0

    for skill in required_skills:
        if skill in candidate_skills:
            matched += 1

    percentage = (matched / len(required_skills)) * 100

    return percentage

# Calculate score for each candidate
df["Match Percentage"] = df["Skills"].apply(calculate_match)
# Sort candidates by score
df = df.sort_values(by="Match Percentage", ascending=False)

# Select the Top 10 candidates
top10 = df.head(10)

print("\nTop 10 Candidates\n")
print(top10[["Candidate_ID", "Match Percentage"]])
# Create bar chart
plt.figure(figsize=(10,6))

plt.bar(
    top10["Candidate_ID"].astype(str),
    top10["Match Percentage"]
)

plt.title("Top 10 Candidate Match Percentage")
plt.xlabel("Candidate ID")
plt.ylabel("Match Percentage (%)")

# Show percentage above each bar
for i, value in enumerate(top10["Match Percentage"]):
    plt.text(i, value + 1, f"{value:.0f}%", ha="center")

plt.ylim(0, 110)

plt.savefig("resume_dashboard.png", dpi=300, bbox_inches="tight")

plt.show()