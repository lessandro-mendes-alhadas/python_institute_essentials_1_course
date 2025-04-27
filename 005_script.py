log_file = open("005_script_output.txt", "w")
print("Any text", "Other text", sep=" = ", end=" !!!", file = log_file)
log_file.close()
