## Workflow: Saving a Conversation

1.  **Trigger**: This workflow is triggered at the end of a user interaction session or when explicitly commanded.
2.  **Get Timestamp**: Generate a timestamp in the format `YYYY-MM-DD_HH-MM-SS`.
3.  **Define Path**: Construct the full file path: `/memory/conversations/[timestamp].md`.
4.  **Format Content**: Structure the conversation in a clear, readable Markdown format. Include user prompts and agent responses.
5.  **Write to File**: Use the `fs.writeFile` tool to save the formatted content to the designated path.