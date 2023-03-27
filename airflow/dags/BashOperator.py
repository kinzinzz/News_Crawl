from datetime import datetime,timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum
from airflow.utils.email import send_email

# DAG 성공 이메일
def success_email(context):
    msg = "Your Dag has succeed"
    subject = "DAG 성공"
    send_email(dag.default_args["email"], subject=subject, html_content=msg)

# DAG 실패 이메일
def failure_email():
    msg = "Your Dag has failed"
    subject = "DAG 실패"
    send_email(dag.default_args["email"], subject=subject, html_content=msg)

local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner':'airflow',
    'email':'amazing208@gmail.com', 
    'email_on_failure':True,
    'email_on_retry':True,
    'retry_delay':timedelta(seconds=300),
    'retries':1,
    'on_sucess_callback': success_email, # DAG 성공 이메일
    'on_failure_callback': failure_email, # DAG 실패 이메일
    'start_date':datetime(2023, 3, 26, tzinfo=local_tz) # 한국시간 기준
}


with DAG(
    
    dag_id = "NewsCrawl",
    default_args=default_args,
    schedule_interval="@daily") as dag: # 하루에 한번
    
    cmd = 'cd && cd NewsCrawl && source secret_bash && scrapy crawl newscrawl'
    crawl_dag=BashOperator(
        task_id="NewsCrawl",
        bash_command=cmd,
        on_success_callback = success_email,
        on_failure_callback = failure_email,             
    )
   
    crawl_dag