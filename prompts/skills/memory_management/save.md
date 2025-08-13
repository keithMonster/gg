## Workflow: Saving a Conversation (v1.1)

1.  **Trigger**: This workflow is automatically triggered at the end of a user interaction session.
2.  **Get Timestamp**: **Crucial Rule**: The timestamp for the filename MUST be dynamically and programmatically obtained from the system (e.g., via `date +%Y-%m-%d_%H-%M-%S`). It MUST NOT be a hardcoded or static value.
3.  **Define Path**: Construct the full file path: `/memory/conversations/[timestamp].md`.
4.  **Format Content**: Structure the latest turn of the conversation in a clear, readable Markdown format.
5.  **Write/Append Logic**:
    *   First, check if a file at the given path already exists.
    *   **If it exists**: Read the file's current content, append the new formatted content, and use `fs.writeFile` to save the entire merged content back to the file.
    *   **If it does not exist**: Use `fs.writeFile` to create the new file with the formatted content.
    *   This ensures that a single conversation log is continuously appended to, rather than being overwritten.