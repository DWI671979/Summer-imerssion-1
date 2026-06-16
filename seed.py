# Inkverse secrets example
# The app works locally without secrets by using local_data/*.json.
# Add GitHub settings only when you want persistent JSON storage on Streamlit Cloud.

github_token = "ghp_your_token_here"
github_repo = "your-user/your-data-repo"
github_branch = "main"
github_data_path = "data"

# No OpenAI key is required. The copyright/originality checker is fully offline
# and uses local text recognition: TF-IDF + n-gram overlap + fuzzy matching.
