## Workflow: Summarizing a Conversation

1.  **Trigger**: This workflow is used when a retrieved conversation is too long to be efficiently processed.
2.  **Load Content**: Read the full content of the target conversation file.
3.  **Identify Key Information**: Scan the text to identify:
    - The user's primary goals or questions.
    - The agent's key decisions, solutions, or deliverables.
    - Any critical constraints or requirements mentioned.
4.  **Synthesize Summary**: Generate a concise summary containing only the most important points.
5.  **Use Summary**: The summary is then used as the context for the ongoing task, in place of the full conversation transcript.