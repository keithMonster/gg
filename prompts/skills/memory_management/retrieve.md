## Workflow: Retrieving a Conversation

1.  **Trigger**: This workflow is triggered when the agent needs to access past information to inform its current task.
2.  **Identify Search Criteria**: Determine the key information needed. This could be a date, a specific topic, a project name, or a keyword.
3.  **Scan Memory**: Use `fs.listDir` to get a list of all files in `/memory/conversations/`.
4.  **Filter & Select**: 
    - If searching by date, directly match the filename.
    - If searching by keyword/topic, use `fs.readFile` on each file and perform a text search within the content.
5.  **Present Findings**: Load the content of the most relevant file(s) into the agent's context to be used in the current task.