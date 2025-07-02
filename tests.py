from functions.get_files_info import get_files_info
tests = []
tests.append(("calculator", "."))
tests.append(("calculator", "pkg"))
tests.append(("calculator", "/bin"))
tests.append(("calculator", "../"))
for test in tests:
    print(get_files_info(*test))

