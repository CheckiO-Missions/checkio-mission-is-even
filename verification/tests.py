"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [2],
            "answer": True,
        },
        {
            "input": [5],
            "answer": False,
        },
        {
            "input": [0],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": [6],
            "answer": True,
        },
        {
            "input": [17],
            "answer": False,
        },
    ]
}
