from urllib.request import urlopen
from bs4 import BeautifulSoup
import re as rej
import requests


def main_func(self, app, tech):
    # start and set 0
    app.processEvents()
    self.generalOutput.clear()
    self.log.append("starting...")
    self.generalOutput.append("لطفا صبر کنید")
    n = 0
    n2 = 0
    salary_sum = 0
    max_salary = 0
    job_skill = {}

    job_type = {
        "remote": 0,
        "fullTime": 0,
        "partTime": 0,
        "project": 0
    }

    job_level = {
        "intern": 0,
        "junior": 0,
        "senior": 0
    }
    i = 0
    # starting analyze
    while True:
        i += 1
        url = f"https://quera.ir/magnet/jobs/{tech}?page={i}"
        # url = "https://quera.ir/magnet/jobs/python?page=3"
        app.processEvents()
        self.log.append(f"Analyze: technologies :  <  {tech}  >  &   page :  {i}  ")
        # page = urlopen(url)
        # html = page.read().decode("utf-8")
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        re = soup.find_all('article')
        n += len(re)
        for j in range(len(re)):
            typeT = re[j].find('div', attrs={"class": "chakra-stack css-4xzh6k"})
            try:
                remote = typeT.find("p").text
                if remote == "امکان دورکاری":
                    job_type["remote"] += 1
            except:
                pass
            typeT = typeT.find_all("span")

            typeC = typeT[1].text
            if typeC == 'پاره‌وقت':
                job_type["partTime"] += 1
            elif typeC == 'تمام‌وقت':
                job_type["fullTime"] += 1
            elif typeC == 'پروژه‌ای':
                job_type["project"] += 1

            level = typeT[0].text
            if level == "Senior":
                job_level["senior"] += 1
            elif level == "Junior":
                job_level["junior"] += 1
            elif level == "Intern":
                job_level["intern"] += 1

            skills = re[j].find_all('div', attrs={"class": "TechnologyLabel_techLabel__3f-73"})
            for skill in skills:
                skill = str(skill.text)
                skill = rej.sub(r'\s*', '', skill)
                if skill not in job_skill:
                    job_skill[skill] = 1
                else:
                    job_skill[skill] += 1
            try:
                salary = typeT[2].text
                if "۱۲" in salary:
                    salary = 12
                elif "۱۰" in salary:
                    salary = 10
                elif "۸" in salary:
                    salary = 8
                elif "۶" in salary:
                    salary = 6
                elif "۴" in salary:
                    salary = 4
                elif "۲" in salary:
                    salary = 2
                elif "۱" in salary:
                    salary = 1
                salary_sum += salary
                n2 += 1
                if salary > max_salary:
                    max_salary = salary
                    link = "quera.ir" + re[j].find('a', attrs={"class": "chakra-button"})["href"]
            except:
                pass

        try:
            a = soup.find('button', attrs={"aria-label": "صفحه بعدی"})["disabled"]
            break
        except:
            pass

    job_skill = sorted(job_skill.keys(), key=lambda item: job_skill[item], reverse=True)
    job_skill = job_skill[:3]
    job_skill = '    '.join(job_skill)

    self.log.append("done")
    self.generalOutput.clear()

    self.generalOutput.append(f"تعداد فرصت های شغلی:  {n} مورد")
    self.generalOutput.append("")
    self.generalOutput.append(f"نوع همکاری‌ها:\nتمام‌وقت:  {int(job_type['fullTime'] / n * 100)} درصد")
    self.generalOutput.append(f"پاره‌وقت:  {int(job_type['partTime'] / n * 100)} درصد")
    self.generalOutput.append(f"پروژه‌ای:  {int(job_type['project'] / n * 100)} درصد")
    self.generalOutput.append("")
    self.generalOutput.append(f"موقعیت‌های با امکان دورکاری:  {int(job_type['remote'] / n * 100)} درصد")
    self.generalOutput.append("")
    self.generalOutput.append(f"درصد هر کدام از سطح‌های مورد نیاز:")
    self.generalOutput.append(f"ارشد:  {int(job_level['senior'] / n * 100)} درصد")
    self.generalOutput.append(f"جوان:  {int(job_level['junior'] / n * 100)} درصد")
    self.generalOutput.append(f"کارآموز:  {int(job_level['intern'] / n * 100)} درصد")
    self.generalOutput.append("")
    self.generalOutput.append(f"سه مهارت پر‌تکرار:   {job_skill}")
    self.generalOutput.append("")
    self.generalOutput.append(f"میانگین حقوق:   {salary_sum / n2:.2f} ملیون تومان")
    self.generalOutput.append("")
    self.generalOutput.append(f"لینک فرصت شغلی با بیشترین درآمد:   {link}")

    # print(n)
    # print(job_level)
    # print(job_type)
    # print(job_skill)
    # print(salary_sum / n2)
    # print(link)
