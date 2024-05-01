# Extract to daily notes

Extracts blocks from single Markdown files.  
Format of blocks is hard-coded.  
Creates daily notes if not present.  
Appends blocks to daily notes.

## Block format

```markdown
## 2405011315

Content
#tag
```

## Usage

- `pip install click`
- `python3 main input.md daily_notes/`
