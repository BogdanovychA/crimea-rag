system-prompt =
    You are a knowledge base assistant. Your task is to answer questions based solely on the provided context. If the context does not contain the answer, say so, and do not try to make up an answer.

    Context for analysis:
    {context}

    User question:
    {question}

hello-text =
    Hello!
    I am an AI from provider "{ $llm_name }", model: "{ $llm_model }".
    You can ask me any question about the website ["Crimea is Ukraine"](https://crimea-is-ukraine.org/en/).

only-text-supported = I can only work with text.

kb-search-step-name = Knowledge base search

kb-search-step-output = { $count ->
    [0]      No relevant fragments found in the knowledge base.
    [one]    Found 1 relevant fragment in the knowledge base.
   *[other]  Found { $count } relevant fragments in the knowledge base.
}

home-page = Home

source-element-content =
    Source: { $url }

    Text snippet:
    { $content }

sources-title = Sources

unexpected-error = Unexpected error. Please contact the developer.

request-too-large =
    Your request is too large. It will be shortened. Maximum length: { $max_query_length } { $max_query_length ->
        [one]   character.
       *[other] characters.
    }
