from constraint import Problem, AllDifferentConstraint

# Create the CSP instance.
problem = Problem()

# Define the variable groups matching exactly the formal definition
subjects     = ["ComputerScience", "Mathematics", "Philosophy", "History"]
cars         = ["Tesla", "BMW", "Mercedes", "Volvo", "Audi"]
research     = ["ArtificialIntelligence", "ClimateChange", "QuantumPhysics",
                "Neuroscience", "MedievalLiterature"]
universities = ["Oxford", "Cambridge", "MIT", "Stanford", "Harvard"]
decors       = ["Blue", "Green", "Red", "Yellow", "White"]
drinks       = ["Espresso", "HerbalTea", "GreenTea", "BlackCoffee"]

# The shared domain for every variable is the five office positions
OFFICES = [1, 2, 3, 4, 5]

# Add all 28 variables with their common domain
for entity in subjects + cars + research + universities + decors + drinks:
    problem.addVariable(entity, OFFICES)

# C_uniq_1 to C_uniq_6 where each attribute group is pairwise different.
problem.addConstraint(AllDifferentConstraint(), subjects)
problem.addConstraint(AllDifferentConstraint(), cars)
problem.addConstraint(AllDifferentConstraint(), research)
problem.addConstraint(AllDifferentConstraint(), universities)
problem.addConstraint(AllDifferentConstraint(), decors)
problem.addConstraint(AllDifferentConstraint(), drinks)

# C1: The Computer Science professor has blue decor
problem.addConstraint(lambda cs, blue: cs == blue, ["ComputerScience", "Blue"])

# C2: The Oxford graduate drives a Tesla
problem.addConstraint(lambda ox, te: ox == te, ["Oxford", "Tesla"])

# C3: The AI researcher drinks espresso
problem.addConstraint(lambda ai, es: ai == es, ["ArtificialIntelligence", "Espresso"])

# C4: The Cambridge graduate is in office 1
problem.addConstraint(lambda ca: ca == 1, ["Cambridge"])

# C5: The BMW driver's office is adjacent to the green decor office
problem.addConstraint(lambda bm, gr: abs(bm - gr) == 1, ["BMW", "Green"])

# C6: The Climate Change researcher drinks herbal tea
problem.addConstraint(lambda cc, ht: cc == ht, ["ClimateChange", "HerbalTea"])

# C7: The Mathematics professor has red decor
problem.addConstraint(lambda ma, re: ma == re, ["Mathematics", "Red"])

# C8: The Mercedes driver researches Quantum Physics
problem.addConstraint(lambda me, qp: me == qp, ["Mercedes", "QuantumPhysics"])

# C9: The professor in office 3 drinks green tea
problem.addConstraint(lambda gt: gt == 3, ["GreenTea"])

# C10: The Cambridge graduate's office is adjacent to the yellow decor office
problem.addConstraint(lambda ca, ye: abs(ca - ye) == 1, ["Cambridge", "Yellow"])

# C11: The Volvo driver teaches Philosophy
problem.addConstraint(lambda vo, ph: vo == ph, ["Volvo", "Philosophy"])

# C12: The Neuroscience researcher's office is adjacent to the Audi driver's office
problem.addConstraint(lambda ne, au: abs(ne - au) == 1, ["Neuroscience", "Audi"])

# C13: The History professor drinks black coffee
problem.addConstraint(lambda hi, bc: hi == bc, ["History", "BlackCoffee"])

# C14: The professor with white decor graduated from MIT
problem.addConstraint(lambda wh, mi: wh == mi, ["White", "MIT"])

# C15: The Stanford graduate's office is right of the Harvard graduate's office
problem.addConstraint(lambda st, ha: st == ha + 1, ["Stanford", "Harvard"])

# Solve the CSP by labelling all variables
solutions = problem.getSolutions()

# Report on the number of solutions found
print(f"Number of solutions found: {len(solutions)}\n")

# Display the first valid solution as a table indexed by office position
solution = solutions[0]
print("=" * 72)
print(f"{'Office':<8}{'Subject':<18}{'Car':<10}{'Research':<22}{'University':<12}{'Decor':<8}{'Drink':<12}")
print("=" * 72)

for office in OFFICES:
    # Look up which entity from each group is assigned to this office
    subject    = next((s for s in subjects     if solution[s] == office), "-")
    car        = next((c for c in cars         if solution[c] == office), "-")
    focus      = next((r for r in research     if solution[r] == office), "-")
    university = next((u for u in universities if solution[u] == office), "-")
    decor      = next((d for d in decors       if solution[d] == office), "-")
    drink      = next((b for b in drinks       if solution[b] == office), "-")
    print(f"{office:<8}{subject:<18}{car:<10}{focus:<22}{university:<12}{decor:<8}{drink:<12}")

print("=" * 72)

# Final answer to the question
medieval_office = solution["MedievalLiterature"]
medieval_university = next(u for u in universities if solution[u] == medieval_office)
print(f"\nQ: Which professor's research focus is Medieval Literature?")
print(f"A: The professor in office {medieval_office}, who graduated from {medieval_university}.")
