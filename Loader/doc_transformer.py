import textwrap
from IPython.display import Markdown

def to_markdown(text, bullet_point='*', blockquote_symbol='> '):
    """
    Converts a given text to Markdown format.
    Args:
    text (str): The text to be converted.
    bullet_point (str, optional): The bullet point symbol for lists. Defaults to '*'.
    blockquote_symbol (str, optional): The symbol for blockquotes. Defaults to '> '.
    Returns:
    Markdown: The text converted to Markdown format.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Replace bullet points and handle new lines for blockquotes
    wrapped_text = text.replace('•', f'  {bullet_point}')
    wrapped_text = textwrap.indent(wrapped_text, blockquote_symbol, lambda line: True)

    return Markdown(wrapped_text)