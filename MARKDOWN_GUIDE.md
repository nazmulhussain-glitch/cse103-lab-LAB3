# Markdown Quick Guide

Markdown is a lightweight markup language used to format text in files such as `README.md`. GitHub automatically displays Markdown files as formatted pages. This guide demonstrates the formatting features used in this project.

## 1. Headings

Use the `#` symbol to create headings. More `#` symbols represent smaller heading levels.

```markdown
# Main heading
## Section heading
### Subsection heading
```

Headings organise documentation into clear sections and make long pages easier to read.

## 2. Emphasis and inline code

Use a pair of asterisks for **bold text**, one asterisk for *italic text*, and backticks for `inline code`.

```markdown
**Important text**
*Emphasised text*
`print("Hello")`
```

Inline code is useful when mentioning filenames, commands, variables, and function names.

## 3. Unordered and ordered lists

An unordered list uses hyphens or asterisks:

```markdown
- First item
- Second item
- Third item
```

An ordered list uses numbers:

```markdown
1. Open the project folder.
2. Review the files.
3. Run the Python program.
```

Lists are useful for instructions, requirements, and summaries.

## 4. Links and images

A link is written with the visible label in square brackets followed by the destination in parentheses.

```markdown
[Visit GitHub](https://github.com)
```

An image uses a similar format, but begins with an exclamation mark:

```markdown
![Alternative description](image-file.png)
```

Alternative text helps explain the image if it cannot be displayed.

## 5. Code blocks

Use three backticks before and after a block of code. Add a language name after the opening backticks to enable syntax highlighting.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Nazmul"))
```

Code blocks are especially useful in programming documentation because indentation and line breaks are preserved.

## 6. Tables

Tables organise related information into rows and columns.

```markdown
| Command | Purpose |
|---|---|
| `git status` | Show working-tree state |
| `git add .` | Stage changes |
| `git commit` | Save a commit |
| `git push` | Upload commits |
```

The row containing hyphens separates the table headings from the table data.

## 7. Task lists

GitHub supports checkboxes in Markdown task lists.

```markdown
- [x] Create the README file
- [x] Add a project overview
- [ ] Review future improvements
```

Use `[x]` for a completed task and `[ ]` for a pending task.

## 8. Blockquotes

Use the greater-than symbol to display a quotation or highlighted note.

```markdown
> Keep commit messages short and meaningful.
```

Blockquotes can draw attention to important information.

## 9. Horizontal rules

Three hyphens create a horizontal divider.

```markdown
---
```

A divider can separate major parts of a long document.

## 10. Markdown in this project

The project README uses headings, lists, links, code blocks, tables, and inline code. These elements make the repository easier for another student or reviewer to understand.

## 11. Quick reference

| Markdown syntax | Result or purpose |
|---|---|
| `# Heading` | Main heading |
| `**text**` | Bold text |
| `*text*` | Italic text |
| `` `code` `` | Inline code |
| `- item` | Unordered list |
| `1. item` | Ordered list |
| `[label](url)` | Link |
| `![alt](image.png)` | Image |
| `> note` | Blockquote |
| `---` | Horizontal divider |
| `- [ ] task` | Unchecked task |
| `- [x] task` | Completed task |
