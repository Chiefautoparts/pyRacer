import cx_Freeze

executables = [cx_Freeze.Executables("pygameVideo15.py")]

cx_Freeze.setup(
	name="A bit Racey",
	options={"build_exe": {"packages":["pygame"],
							"include_files": ["racecar.png"]}},
	executables = executables

	)