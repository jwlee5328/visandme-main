# Mode 1: Web Interface (Google Gemini) -> Copy & Paste
#
# Steps:
#   1. Go to gemini.google.com
#   2. Paste the contents of sample.csv into the chat
#   3. Ask Gemini:
#      "Here is my CSV data: [paste the file contents].
#       Write Python code using matplotlib to create a bar chart.
#       Chart title: 'My Day'. Save the figure as mode1.png."
#   4. Copy the code Gemini gives you
#   5. Paste it below the dashed line
#   6. Open the terminal and run:  python mode1.py
#
# Key insight: Gemini has NO access to your files.
# You must copy-paste the data AND the code manually.
#
# ------------------------------------------------------------------
# Paste Gemini's code below this line:
import pandas as pd
import matplotlib.pyplot as plt
import io

# Input data
csv_data = """activity,hours
Sleep,7
Study,4
Meals,1.5
Exercise,0.5
Leisure,3
Other,8"""

# Load data into a DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Sort the data by hours (descending) for the bar chart
df_sorted = df.sort_values(by='hours', ascending=False)

# Create the bar chart
plt.bar(df_sorted['activity'], df_sorted['hours'])

# Add labels and title
plt.title('My Day')
plt.xlabel('Activity')
plt.ylabel('Hours')

# Save the plot
plt.savefig('mode1.png')
# ------------------------------------------------------------------

