# Mode 2: IDE - GitHub Copilot Chat
#
# Steps:
#   1. Open Copilot Chat
#      (left sidebar icon  OR  Ctrl+Shift+I / Cmd+Shift+I)
#   2. Type this prompt:
#      "Read sample.csv and create a bar chart using matplotlib.
#       Chart title: 'My Day'. Save the figure as mode2.png.
#       Write the code into mode2.py and make it ready to run."
#   3. Copilot will generate and insert the code directly into this file
#   4. Open the terminal and run:  python mode2.py
#
# Key insight: Copilot can SEE all your files in the Codespace.
# It knows sample.csv exists and what's in it.
#
# ------------------------------------------------------------------
# Copilot will write code here:
# ------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
csv_path = "sample.csv"
df = pd.read_csv(csv_path)

# Sort the data by hours (descending) for the bar chart
df_sorted = df.sort_values(by="hours", ascending=False)

# Create the bar chart
plt.bar(df_sorted["activity"], df_sorted["hours"])

# Add labels and title
plt.title("My Day")
plt.xlabel("Activity")
plt.ylabel("Hours")

# Save the plot
plt.savefig("mode2.png")


