Show all saved conference summaries in the conference-mcp project.

Run this bash command and display the results:

```bash
find /home/haen/conference-mcp/summaries -name "*.md" | sort
```

Format the output as a grouped list by conference folder. For each file:
- Parse the folder name as the conference name (replace underscores with spaces, title case)
- Parse the filename: remove the leading YYYYMMDD_ timestamp, replace underscores with spaces, remove .md extension
- Show the date from the timestamp prefix as YYYY-MM-DD

Output format:

## 저장된 요약 목록

**[Conference Name]**
1. [Title] — YYYY-MM-DD
   `[relative path from summaries/]`

Show total count at the end.
