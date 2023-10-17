import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from modules.plotter import format_matrix_to_table

def read_csv(file_name):
    return pd.read_csv(file_name)

# Function to get overdue tasks
def count_overdue_tasks(filename):
    df = pd.read_csv(filename)
    df = df[df['OverDue'].notna()]
    df['OverDue'] = df['OverDue'].astype(str)
    overdue_tasks = df[df['OverDue'].str.strip().str.upper() == 'TRUE']
    return len(overdue_tasks)

# Function to get task status by group
def report_task_status_by_group(filename):
    df = pd.read_csv(filename)
    df['Status'] = df['Status'].astype(str).str.upper()
    df['Task Group'] = df['Task Group'].astype(str).str.upper()
    df['Status'] = df['Status'].apply(lambda x: 'Open' if 'OPEN' in x else ('Close' if 'CLOSE' in x else x))
    df = df[df['Status'].isin(['Open', 'Close'])]
    valid_task_groups = ['SAFETY', 'SITE MANAGEMENT', 'DESIGN TEAM', 'QUALITY', 'N/A']
    df = df[df['Task Group'].isin(valid_task_groups)]
    report = df.groupby(['Task Group', 'Status']).size().unstack(fill_value=0)
    return report

# Function to get barchart for overdue tasks
def report_overdue_tasks_by_project(filename):
    df = pd.read_csv(filename)
    df['OverDue'].fillna('False', inplace=True)  # replace NaN with 'False'
    overdue_tasks = df[df['OverDue'].astype(str).str.strip().str.upper() == 'TRUE']
    projects = [1328, 1329, 1330, 1335, 1338, 1340, 1343, 1345]
    overdue_count_by_project = overdue_tasks.groupby('project').size().reindex(projects, fill_value=0)
    return overdue_count_by_project

# Function to get barchart for percentage of overdue tasks
def percentage_overdue_by_project(filename):
    df = pd.read_csv(filename)
    df['OverDue'].fillna('False', inplace=True)
    df['OverDue'] = df['OverDue'].astype(str).str.strip().str.upper()
    overdue_tasks = df[df['OverDue'] == 'TRUE']
    projects = [1328, 1329, 1330, 1335, 1338, 1340, 1343, 1345]
    total_tasks = df['project'].value_counts()
    overdue_task_counts = overdue_tasks['project'].value_counts()
    percentages = {}
    for project in projects:
        if project in total_tasks:
            percentages[project] = (overdue_task_counts.get(project, 0) / total_tasks[project]) * 100
        else:
            percentages[project] = 0
    return percentages;

# Function to get mean elasped days in project
def mean_of_days_elapsed_in_projects(filename):
    projects_list = [1328, 1329, 1330, 1335, 1338, 1340, 1343, 1345]
    df = pd.read_csv(filename)
    df = df[df['Project'].isin(projects_list)]
    df['Created'] = pd.to_datetime(df['Created'], dayfirst=True)
    today = datetime.today()
    df['Days Elapsed'] = (today - df['Created']).dt.days
    mean_days_elapsed_by_project = df.groupby('Project')['Days Elapsed'].mean().round(2)
    consolidated_mean = round(df['Days Elapsed'].mean(), 2)
    # Display results in aligned format
    print("{:<10} {:<15}".format('Project', 'Days Elapsed'))
    print('-' * 25)
    for project, days_elapsed in mean_days_elapsed_by_project.items():
        print("{:<10} {:<15.3f}".format(project, days_elapsed))
    print('-' * 25)
    print("{:<10} {:<15.3f}".format('Consolidated', consolidated_mean))
    return {'By Project': mean_days_elapsed_by_project, 'Consolidated': consolidated_mean}


# Function to get Open forms data
def generate_open_forms_data(filename):
    df = pd.read_csv(filename)
    df = df[df['Status'].str.contains('open', case=False, na=False)]
    type_counts = df['Type'].value_counts()
    valid_types = [
        'Site Management', 'Subcontractor Inspections', 'Quality 00 General', 'Permits',
        'Safety Forms', 'Quality 02 Architectural', 'Quality 04 MEP Services',
        'Quality 01 Structural', '00 Project Management', 'Design Team / BC(A)R',
        'BU - Head Office Inspection', 'Quality 03 Civil'
    ]
    type_counts = type_counts[type_counts.index.isin(valid_types)]
    return type_counts

# Function to get Time series plot of Report Forms Group by Report Forms Group - Created Date
def generate_timeseries_data_created(file_path):
    df = pd.read_csv(file_path)
    df['Created'] = pd.to_datetime(df['Created'], dayfirst=True)
    open_forms = df[df['Report Forms Status'] == 'Open']
    grouped_data = open_forms.groupby(['Report Forms Group', 'Created']).size().reset_index(name='Count')
    time_series_data = grouped_data.pivot(index='Created', columns='Report Forms Group', values='Count').fillna(0)
    return time_series_data

# Function to get Time series plot of Report Forms Group by Report Forms Group - Status Changed Date
def generate_timeseries_data_status_changed(file_path):
    df = pd.read_csv(file_path)
    df['Status Changed'] = pd.to_datetime(df['Status Changed'], dayfirst=True)
    open_forms = df[df['Report Forms Status'] == 'Open']
    grouped_data = open_forms.groupby(['Report Forms Group', 'Status Changed']).size().reset_index(name='Count')
    time_series_data = grouped_data.pivot(index='Status Changed', columns='Report Forms Group', values='Count').fillna(0)
    return time_series_data