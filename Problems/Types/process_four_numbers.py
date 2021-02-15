args = sys.argv
list_of_args = []

for i in range(1, len(args)):
    if isinstance(int(args[i]), int):
        list_of_args.append(args[i])

if len(list_of_args) > 0:
    print(list_of_args)
