EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".c": "c",
    ".h": "c",
    ".hpp": "cpp",
    ".java": "java",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "javascriptreact",
    ".tsx": "typescriptreact",
    ".go": "go",
    ".rs": "rust",
    ".cs": "csharp",
    ".php": "php",
    ".rb": "ruby",
    ".swift": "swift",
    ".kt": "kotlin",
    ".scala": "scala",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".sql": "sql",
    ".sh": "bash",
    ".md": "markdown"
}
from pathlib import Path

def detect_language(filename: str) -> str:
    extension = Path(filename).suffix.lower()
    return EXTENSION_TO_LANGUAGE.get(extension, "text")