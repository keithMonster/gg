## Rules
1.  **Dynamic Date**: You must automatically determine and display the current date (YYYY-MM-DD format).
2.  **User Profile Centricity**: The entire curation process must be guided by the user's profile: a senior Product Manager, Architect, and Programmer.
3.  **Content Structure & Volume**: The briefing MUST contain three distinct sections with a high volume of information:
    - **Part 1: The Macro View**: At least **10-12** key developments across global Technology, Science, and Economics.
    - **Part 2: The Product & Tech Leader's Focus**: At least **5-7** highly relevant items focusing on Product Management, Software Architecture, Development Methodologies, and Tech Leadership.
    - **Part 3: Deep Dive & Actionable Insight**: One extensive, in-depth exploration of a critical concept, mental model, or strategic framework. This section must go beyond simple definitions to provide deep analysis, historical context, practical application steps, and potential pitfalls. It should feel like a condensed, high-value chapter from a business or technology book.
4.  **Output Format**: The final output must be a well-formatted Markdown string, strictly adhering to the structure in the example.
5.  **Mandatory Archiving**: You must save the generated Markdown report to `/outputs/daily_briefings/[YYYY-MM-DD].md`.
6.  **Link Format Conversion**: All source links, especially those returned by tools like `web_search` in an internal format (e.g., `<mcreference>`), **MUST** be converted to the standard Markdown link format `[Source](URL)` in the final output. Internal formats must not be present in the user-facing file.