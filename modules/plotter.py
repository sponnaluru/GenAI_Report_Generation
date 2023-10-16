import matplotlib.pyplot as plt
import numpy as np

def display_table_task_status_by_group(data):
    fig, ax = plt.subplots(figsize=(10, 4))
    # Hide axes
    ax.axis('off')
    ax.axis('tight')
    # Prepare the table data
    cell_data = []
    for index, row in data.iterrows():
        cell_data.append([index] + list(row))
    # Table from DataFrame without additional label
    table = ax.table(cellText=cell_data, colLabels=["Task Group/Status"] + list(data.columns), loc='center')
    # Adjust font size and table scaling for appearance
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.2)
    # Aligning the data to center
    for (i, j), cell in table.get_celld().items():
        cell.set_text_props(ha='center', va='center')
    # Make header bold and colored
    for i, cell in enumerate(table._cells[(0, col)] for col in range(len(data.columns) + 1)):
        cell.set_text_props(weight='bold')
        cell.set_facecolor('#f5f5f5')  # Light gray color, you can adjust the color as you like
    plt.show()


def plot_task_status_by_group(report):
    # Plotting the data
    report.plot(kind='bar', stacked=True, figsize=(10, 7))
    # Setting title and labels
    plt.title('Total Number of Open and Closed Tasks by Each Task Group', fontsize=16, fontweight='bold')
    plt.xlabel('Task Group', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Tasks', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_overdue_tasks_by_project(report):
    report.plot(kind='bar', color='red', figsize=(10, 7))
    # Setting title and labels
    plt.title('Total Number of Overdue Tasks by Project', fontsize=16, fontweight='bold')
    plt.xlabel('Project', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Overdue Tasks', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_percentage_overdue_by_project(percentages):
    project_labels = [str(p) for p in percentages.keys()]
    bars = plt.bar(project_labels, percentages.values(), color='green') 
    plt.xlabel('Project', fontsize=14, fontweight='bold')
    plt.ylabel('Percentage of Overdue Tasks (%)', fontsize=14, fontweight='bold')
    plt.title('Percentage of Overdue Tasks by Project', fontsize=16, fontweight='bold')
    plt.xticks(project_labels, rotation=45)
    plt.ylim(0, 100)  # Setting y-axis limit to 100 for percentage
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 1, '{:.2f}%'.format(height), 
             ha='center', va='bottom')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def display_table_mean_days(data):
    fig, ax = plt.subplots(figsize=(10, 4))  # set the size that you'd like (width, height)
    ax.axis('tight')
    ax.axis('off')
    # Define colors
    cell_colors = []
    for i, row in data.iterrows():
        if row['Project'] == 'Consolidated Mean':
            cell_colors.append(['#FFDDC1', '#FFDDC1'])  # Light orange for consolidated mean
        else:
            cell_colors.append(['#E5E5E5', '#E5E5E5'])  # Light gray for other rows
    
    table = ax.table(cellText=data.values, colLabels=data.columns, cellColours=cell_colors, loc='center')
    # Adjust the table's row height and column widths
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(data.columns))))
    plt.show()

def plot_open_forms(data):
    data.plot(kind='bar', color='dodgerblue', figsize=(10,6))
    plt.title("Number of Open Forms by Type", fontsize=16, fontweight='bold')
    plt.xlabel("Type of Form", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Open Forms", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_timeseries_created(data):
    ax = data.plot(figsize=(15, 7))
    ax.set_title("Number of 'Open' Forms Over Time by 'Created Date' Report Forms Group")
    ax.set_ylabel("Number of Forms")
    ax.set_xlabel("Date")
    plt.tight_layout()
    plt.legend(title="Report Forms Group")
    plt.show()

def plot_timeseries_status_changed(data):
    ax = data.plot(figsize=(15, 7))
    ax.set_title("Number of 'Open' Forms Over Time by 'Status Changed' Date Report Forms Group")
    ax.set_ylabel("Number of Forms")
    ax.set_xlabel("Date")
    plt.tight_layout()
    plt.legend(title="Report Forms Group")
    plt.show()   

def format_matrix_to_table(matrix):
    # Begin the formatted string with column headers
    formatted_string = "{:<20} {:<10} {:<10}\n".format("Task Group", "Close", "Open")
    formatted_string += "="*40 + "\n"
    # Loop through each row of the matrix to format the values
    for index, row in matrix.iterrows():
        formatted_string += "{:<20} {:<10} {:<10}\n".format(index, row['Close'], row['Open'])

    return formatted_string