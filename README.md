# University Mystery — Constraint Satisfaction Problem

Solution to **Portfolio Exercise #3** for *CCS2600 Artificial Intelligence Techniques* (University of York Europe Campus).

The program models the University Mystery puzzle as a Constraint Satisfaction Problem and solves it by labelling using the `python-constraint` library.

## Authors

- Konstantinos Plassaras — CSY24080
- Alexios Kalmpouros — CSY24078
- Panagiotis-Sotirios Peppas — CSY24120

## Requirements

- Python 3.8 or later
- `python-constraint` library

Install the dependency with:

```bash
pip install python-constraint
```

## How to Run

```bash
python csp.py
```

The program prints the total number of valid solutions found, a table showing the first solution by office position and the answer to the question *"Which professor's research focus is Medieval Literature?"*.

## Files

- `csp.py` — Python implementation of the CSP
- `README.md` — this file

## Observation on Solutions

The 15 constraints defined in the assignment admit multiple valid labellings of the variables. The program returns the first solution found that satisfies every constraint. A detailed analysis of this is included in the report.
