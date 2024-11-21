from prefect import flow

@flow
def etl_flow():
    print("hello world")
