from functions.get_file_content import get_file_content
tests = []
# tests.append(("calculator", "lorem.txt"))
#tests.append(("calculator", "pkg"))
#tests.append(("calculator", "/bin"))
#tests.append(("calculator", "../"))

tests.append(("calculator", "main.py"))
tests.append(("calculator", "pkg/calculator.py"))
tests.append(("calculator", "/bin/cat"))
for test in tests:
    print(get_file_content(*test))

