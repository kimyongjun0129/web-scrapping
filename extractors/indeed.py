import requests
from bs4 import BeautifulSoup


def extract_indeed_jobs(keyword):
    return berlin_job_scrapping(keyword)


def berlin_job_scrapping(keyword):
    jobs_info = []
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    soup = BeautifulSoup(response.content, "html.parser")
    job_info = soup.find_all("div", class_="bjs-jlid__wrapper")

    for job in job_info:
        job_info = {
            "site_name":
            "berlin-site",
            "company_name":
            job.find("a", class_="bjs-jlid__b").text,
            "skill_name":
            job.find("h4", class_="bjs-jlid__h").text,
            "description":
            job.find("div", class_="bjs-jlid__description").text.strip(),
        }
        jobs_info.append(job_info)
    return jobs_info
