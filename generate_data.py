from random import randint, sample
import json

def generate_data(name_experience: str, path:str,horizon:int, nb_qualifications:int, nb_staff:int, nb_jobs:int, gain_range:tuple):
    """
    Generate a random instance of the problem
    params:
        name_experience: name of the instance
        path: path to the file where the instance will be saved
        horizon: horizon of the problem
        nb_qualifications: number of qualifications
        nb_staff: number of staff
        nb_jobs: number of jobs
        gain_range: range of the gain of the jobs
    return: 
        the instance
    """
    # Qualifications list
    qualifications = ["Qualification_" + str(i) for i in range(nb_qualifications)]
    # Staff list
    staff = []
    for i in range(nb_staff):
        name = "Individu_" + str(i)
        nb_qualifications_personnel = randint(1,nb_qualifications)
        qualifications_personnel = sample(qualifications, nb_qualifications_personnel)
        vacations = sample([i for i in range(horizon)], randint(1, horizon))
        staff.append({"name": name, "qualifications": qualifications_personnel,"vacations": vacations})
    # Jobs list
    jobs = []
    for i in range(nb_jobs):
        gain = randint(gain_range[0], gain_range[1])
        due_date = randint(1, horizon)
        working_days_per_qualification = {}
        nb_qualifications = randint(1, nb_qualifications)
        qualifications_per_job = sample(qualifications, randint(1, nb_qualifications))
        for qualification in qualifications_per_job:
            working_days_per_qualification[qualification] = randint(1, horizon)
        jobs.append({"name": "Job_"+str(i), "gain": gain, "due_date": due_date, "daily_penalty": 3, "working_days_per_qualification": working_days_per_qualification})
    # Save the instance
    instance = {"horizon": horizon, "qualifications": qualifications, "staff": staff, "jobs": jobs}
    filePath = path + name_experience + ".json"
    with open(filePath, 'w') as fp:
        json.dump(instance, fp)
    return instance



if __name__ == "__main__":
    name_experience = "test_sample"
    generate_data("test_sample","./data/",horizon = 5, nb_qualifications = 3, nb_staff = 2, nb_jobs = 5, gain_range = (1, 10))