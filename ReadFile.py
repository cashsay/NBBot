file = open("data")
data = file.read()
file = file.close()

data = data.strip().split()
output = "exports.Data=[\n"


for x in data:
    output = output + "  \"" + x + "\"" + "," + "\n"

output = output.strip().strip(",")
output = output + "\n]"

file = open("data.js","w")
file.write(output)
file.close()