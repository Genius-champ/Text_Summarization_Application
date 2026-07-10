"""
==========================================================
HELPERS MODULE

Utility functions for:
    - Word counting
    - Compression ratio calculation
    - Processing time formatting

Compatible with:
    - Streamlit
    - Python 3.11+
==========================================================
"""


def count_words(text):
    """
    Counts the number of words in a text.

    Parameters:
        text (str): Input text

    Returns:
        int: Number of words
    """

    if not text:
        return 0

    return len(text.split())



def calculate_compression_ratio(
    original_text,
    summary_text
):
    """
    Calculates how much the document was compressed.

    Formula:

    Compression Ratio =
    (Summary Words / Original Words) × 100

    Example:

    Original document:
        2000 words

    Summary:
        400 words

    Compression:
        20%

    Parameters:
        original_text (str)
        summary_text (str)

    Returns:
        str
    """

    original_words = count_words(original_text)

    summary_words = count_words(summary_text)


    if original_words == 0:
        return "0%"


    ratio = (
        summary_words /
        original_words
    ) * 100


    return f"{ratio:.2f}%"



def format_time(seconds):
    """
    Formats processing time.

    Example:

    4.567 seconds

    becomes:

    4.57 seconds


    Parameters:
        seconds (float)

    Returns:
        str
    """

    return f"{seconds:.2f} seconds"



def calculate_statistics(
    original_text,
    summary_text,
    processing_time
):
    """
    Generates summary statistics.

    Returns:

    {
        original_words:
        summary_words:
        compression_ratio:
        processing_time:
    }

    """

    statistics = {

        "original_words":
            count_words(original_text),


        "summary_words":
            count_words(summary_text),


        "compression_ratio":
            calculate_compression_ratio(
                original_text,
                summary_text
            ),


        "processing_time":
            format_time(
                processing_time
            )
    }


    return statistics
