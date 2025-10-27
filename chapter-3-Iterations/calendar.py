# Create a 12x4 nested list representing a calendar with 12 months and 4 weeks each
calendar = []
# Iterate over 12 months
for m in range(12):
    months = []
    # Iterate over 4 weeks
    for w in range(4):
        months.append(w)
    calendar.append(months)
# Print the resulting calendar structure
print(calendar)

