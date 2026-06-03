hello-text =
    Hello!
    I am an AI from provider "{ $llm_name }", model: "{ $llm_model }".
    You can ask me any question about the website ["Crimea is Ukraine"](https://crimea-is-ukraine.org/en/).

kb-search-step-name = search on the "Crimea is Ukraine" website

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
