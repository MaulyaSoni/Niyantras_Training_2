from core import Task , Workflow
from builder import WorkflowBuilder

def main():
    workflow1 = (
        WorkflowBuilder()
        .add_task_step("GatherData")
        .add_task_step("DataCleaning").depends_on("GatherData")
        .add_task_step("EDA").depends_on("DataCleaning")
        .add_task_step("TrainModel").depends_on("EDA")
        .add_task_step("AnalyseOutput").depends_on("TrainModel")
        .build()
    )
    
    for name , task in workflow1.tasks.items():
        print(name , task)

if __name__ == "__main__":
    main()