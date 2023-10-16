from modules.data_handler import count_overdue_tasks, report_task_status_by_group, report_overdue_tasks_by_project, percentage_overdue_by_project, mean_of_days_elapsed_in_projects, generate_open_forms_data, generate_timeseries_data_status_changed, generate_timeseries_data_created
from modules.plotter import plot_task_status_by_group, plot_overdue_tasks_by_project, plot_percentage_overdue_by_project, display_table_mean_days, plot_open_forms, plot_timeseries_created, plot_timeseries_status_changed, display_table_task_status_by_group

import pandas as pd

#The total number of tasks that are overdue.
def get_count_of_tasks_overdue():
    overdue_count = count_overdue_tasks("resources/tasks.csv")
    print(f"Total number of overdue tasks: {overdue_count}")

#Total Number of Open and Closed Tasks by Each Task Group
def get_task_status_by_group():
    report = report_task_status_by_group("resources/tasks.csv")
    display_table_task_status_by_group(report)
    print(report)

#Bar chart of the total number of open and closed tasks by each Task Group
def get_plot_task_status_by_group():
    report = report_task_status_by_group("resources/tasks.csv")
    plot_task_status_by_group(report)
    print(report)

#Bar chart of the total number of overdue tasks by project. 
def get_plot_report_overdue_tasks_by_project():
    report = report_overdue_tasks_by_project("resources/tasks.csv")
    plot_overdue_tasks_by_project(report)

#Bar chart of the percentage of overdue tasks by project
def get_plot_percentage_overdue_by_project():
    percentages = percentage_overdue_by_project("resources/tasks.csv")
    plot_percentage_overdue_by_project(percentages)

#The mean number of days elapsed since forms were opened by project
def get_table_mean_of_days_elapsed_in_projects():
    results = mean_of_days_elapsed_in_projects('resources/forms.csv')
    df = pd.DataFrame(list(results['By Project'].items()), columns=['Project', 'Mean Days Elapsed'])
    df.loc[len(df.index)] = ['Consolidated Mean', results['Consolidated']]
    display_table_mean_days(df)

#Bar chart of the number of open forms by Type of form.
def get_plot_generated_open_forms_data():
    data = generate_open_forms_data('resources/forms.csv')
    plot_open_forms(data)

#Time series plot of the number of forms opened (which are currently open) by Report Form Group
#By Created Date
def get_plot_generate_timeseries_data_created():
    data = generate_timeseries_data_created('resources/forms.csv')
    plot_timeseries_created(data)

#By Status Changed Date
def get_plot_generate_timeseries_data_status_changed():
    data = generate_timeseries_data_status_changed('resources/forms.csv')
    plot_timeseries_status_changed(data)

if __name__ == "__main__":
    get_count_of_tasks_overdue()
    get_task_status_by_group()    
    get_plot_task_status_by_group()
    get_plot_report_overdue_tasks_by_project()
    get_plot_percentage_overdue_by_project()
    get_table_mean_of_days_elapsed_in_projects()
    get_plot_generated_open_forms_data()
    get_plot_generate_timeseries_data_created()
    get_plot_generate_timeseries_data_status_changed()