from models.completion_context import CompletionContext

class ContextExtractor:

    def extract(self, request):
        # Extract prefix: all characters in file_content up to cursor_position
        prefix = request.file_content[:request.cursor_position]

        # Extract suffix: all characters in file_content from cursor_position onward
        suffix = request.file_content[request.cursor_position:]

        # Return a CompletionContext instance with extracted prefix and suffix
        return CompletionContext(
            prefix=prefix,
            suffix=suffix,
            language=request.language
        )