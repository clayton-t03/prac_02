FILENAME = "projects.txt"
projects = []
HEADER = "NAME\t Start Date\t Priority\t Cost Estimate\t Completion Percentage"

def save_projects(filename):
    out_file = open(filename, "w")
    print(HEADER, file=out_file)
    for i in range(len(projects)):
        print(f"{projects[i][0]}\t {projects[i][1]}\t {projects[i][2]}\t {projects[i][3]}\t {projects[i][4]}", file=out_file)
    out_file.close()



def load_projects(filename):
    """read file from project.txt"""
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        line = line.replace("\n", "")
        project = line.split("\t")
        projects.append(project)
        for i in range(len(projects)):
            projects[i][2] = int(projects[i][2])
            projects[i][3] = float(projects[i][3])
            projects[i][4] = float(projects[i][4])



    in_file.close()
load_projects(FILENAME)
print(projects)
