from files import Filing

user_input = input("Please enter VTT file: ")
Filing.openVTTFile(Filing.create_file_path(user_input))

user_input = input("Please enter name for output file: ")
Filing.output(user_input)

print("Finished")


