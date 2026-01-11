import re
from Levenshtein import distance as levenshtein

def normalize(text: str) -> str:
    """Remove punctuation, lowercase, collapse spaces."""
    return re.sub(r"[^a-z0-9]+", "", text.lower())

def compute_score(query: str, title: str) -> int:
    nq = normalize(query)
    nt = normalize(title)

    score = 0

    # Exact match (highest priority)
    if nt == nq:
        score += 100
    
    # Title starts with query
    if nt.startswith(nq):
        score += 50

    # Substring match
    if nq in nt:
        score += 25

    # Fuzzy match using Levenshtein distance
    dist = levenshtein(nq, nt)
    if dist == 1:
        score += 20
    elif dist == 2:
        score += 10

    return score