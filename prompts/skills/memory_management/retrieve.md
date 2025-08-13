## Workflow: Retrieving a Memory (v1.0)

1.  **Trigger**: This workflow is triggered when the `system_prompt` requires consulting past memories.
2.  **Identify Keywords**: Based on the user's current query, identify key topics, entities, or date ranges.
3.  **Scan Log Files**: Use `fs.readFile` to scan the contents of the daily log files in `/memory/conversations/`.
4.  **Filter Relevant Entries**: Search for lines or sections containing the identified keywords.
5.  **Extract Context**: Retrieve not just the matching line, but also the surrounding conversation turns (e.g., 2-3 lines before and after) to provide full context.
6.  **Present Findings**: Present the retrieved, contextual snippets for internal analysis to inform the next steps.