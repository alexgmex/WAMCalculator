import functions as f

# Extract raw data from PDF
raw, name, sid = f.extract_pdf('transscript.pdf')

# Create course list
course = f.create_course_list(raw)

# Calculate WAM
wam = f.calculate_wam(course)

# Print results
print(f"WAM for{name},{sid}: {wam}")