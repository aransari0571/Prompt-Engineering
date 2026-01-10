import google.genai as genai

# Google API key setup (New method)
genai.configure(api_key="AIzaSyBuyBgzYPTWTuPsulr_zkBhiK82-kjPdvg")

def retriever_info(query):
    # Dummy implementation
    return "Elon Musk is the CEO of SpaceX and Tesla."

def rag_query_gemini(query):
    retrieved_info = retriever_info(query)
    
    augmented_prompt = f""" 
    Use the following retrieved information to answer the question.
    Context: {retrieved_info}
    Question: {query}"""
    
    try:
        # New API syntax
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content(augmented_prompt)
        return response.text.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    query = "Tell me about Elon Musk"
    response = rag_query_gemini(query)
    print(response)