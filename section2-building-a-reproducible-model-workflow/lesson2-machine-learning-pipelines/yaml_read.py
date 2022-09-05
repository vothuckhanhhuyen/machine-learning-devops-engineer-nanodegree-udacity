import yaml

with open("conda.yml") as fp:
    d = yaml.safe_load(fp)

print(d)

with open("MLproject") as fp:
    d = yaml.safe_load(fp)
print(d)
