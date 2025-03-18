from setuptools import setup, find_packages

setup(
    name="frony-document-chunker",
    version="0.1.0",
    packages=["frony_document_chunker"],
    install_requires=[
        "numpy",
        "pandas",
        "python-dotenv",
        "transformers",
        "langchain-text-splitters",
        "levenshtein",
        "openai",
    ],
)
