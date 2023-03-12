import csv

# Training Data

if __name__ == "__main__":
    with open('survey_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Type', 'Purpose', 'Occurence', 'Boolean']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Boolean': '0' })
        writer.writerow({'Subject': 'Team-Based', 'Type': 'Sprint Retrospective', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team-Based', 'Type': 'Sprint Retrospective', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team-Based', 'Type': 'Sprint Retrospective', 'Boolean': '1'})
