from setuptools import setup, find_packages

setup(
    name="educare",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-generativeai",
        "aiohttp",
        "fastapi",
        "uvicorn",
    ],
    entry_points={
        "console_scripts": [
            "educare=main:demo",
        ],
    },
    python_requires=">=3.10",
    description="EduCare — Multi-Agent Learning & Wellness Assistant",
    author="Your Name",
    author_email="youremail@example.com",
    url="https://github.com/yourusername/educare",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
