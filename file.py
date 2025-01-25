import csv


def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="UTF-8")
    file.write("Title, Company_name, Skill_name\n")

    for job in jobs:
        file.write(
            f"{job['site_name']},{job['company_name']},{job['skill_name']}\n"
        )

    file.close()
