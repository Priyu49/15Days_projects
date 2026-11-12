from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from App.load_records import load_records


def smart_search(query, top_n=3):

    # Load productivity records
    records = load_records()

    if not records:
        print("No records available!")
        return []

    if not query.strip():
        print("Please enter a search query.")
        return []

    # Convert records into searchable text
    documents = []

    for record in records:

        text = " ".join([
            str(record.get("title", "")),
            str(record.get("category", "")),
            str(record.get("priority", "")),
            str(record.get("status", "")),
            str(record.get("due_date", ""))
        ])

        documents.append(text)

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Convert user query into a vector
        query_vector = vectorizer.transform([query])

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(
            query_vector,
            tfidf_matrix
        ).flatten()

    except ValueError:
        print("Unable to process the search query.")
        return []

    # Get the most relevant records
    ranked_indices = similarity_scores.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_n]:

        score = similarity_scores[index]

        # Ignore records with zero similarity
        if score > 0:

            result = records[index].copy()

            result["similarity_score"] = round(
                float(score), 4
            )

            results.append(result)

    return results


# Run smart search from terminal
if __name__ == "__main__":

    user_query = input(
        "Enter what you want to search: "
    )

    search_results = smart_search(user_query)

    print("\n========== SMART SEARCH RESULTS ==========")

    if search_results:

        for index, record in enumerate(
            search_results, start=1
        ):

            print(f"\nResult {index}")
            print("Title:", record["title"])
            print("Category:", record["category"])
            print("Priority:", record["priority"])
            print("Status:", record["status"])
            print(
                "Similarity Score:",
                record["similarity_score"]
            )

    else:
        print("No relevant tasks found.")
        