import requests
import orchestrator.utils.constants as constants

def trigger_airflow_dag(dag_id):

    print("Trying to trigger DAG : " + dag_id)

    url = str(constants.AIRFLOW_URL).format(dag_id)

    print("API : " + url)
    payload = "{}"

    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
