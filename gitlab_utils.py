import requests

def fetch_failed_jobs(project_id, token, limit=5):
    """Fetch last N failed jobs from a GitLab project"""
    try:
        headers = {"PRIVATE-TOKEN": token}
        url = f"https://gitlab.com/api/v4/projects/{project_id}/jobs?scope=failed&per_page={limit}"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return []
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

def fetch_job_log(project_id, job_id, token):
    """Fetch job trace log"""
    try:
        headers = {"PRIVATE-TOKEN": token}
        url = f"https://gitlab.com/api/v4/projects/{project_id}/jobs/{job_id}/trace"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching log for job {job_id}: {e}")
        return None
