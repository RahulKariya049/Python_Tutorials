import os
from rapidfuzz import process

# Simulated folders (e.g., os.listdir("D:/Python Projects"))
real_folders = [
    "GitDemo",
    "python projects",
    "NLP Test",
    "My Scripts",
    "Utilities",
    "Git Utilities"
]

def get_best_match(spoken: str, candidates: list[str], threshold: int = 80) -> str | None:
    """
    Match a spoken folder name with fuzzy logic and return the best candidate folder name.
    """
    # Normalize
    spoken_clean = spoken.lower().strip()

    normalized_candidates = {c.lower().strip(): c for c in candidates}

    match, score, _ = process.extractOne(spoken_clean, normalized_candidates.keys())

    if match and score >= threshold - (5 if len(spoken_clean) <= 6 else 0):  # relax for short words
        return normalized_candidates[match]

    return None

# User's voice recognized input (possibly incorrect)
spoken_folders = ["pythan projects", "gitdemo", "git utilities", "utility"]

for spoken in spoken_folders:
    match = get_best_match(spoken, real_folders)
    print(f"word spoken: {spoken}, word match: {match}")

# How It Works
# process.extractOne(query, choices) tries to find the closest match.

# It returns a tuple:

# (matched_string, confidence_score, index)
# Score > 80 is generally considered reliable.