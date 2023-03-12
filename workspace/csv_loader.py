import csv

# Training Data

if __name__ == "__main__":
    with open('survey_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Type', 'Estimated_Time', 'Occurence', 'Boolean']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<2hr', 'Occurence': 'Monthly', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<1hr', 'Occurence': 'Weekly', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Business Updates', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })

        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '1' })
        writer.writerow({'Subject': 'General Announcements', 'Type': 'Product Performance', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0' })

        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Retrospective', 'Estimated_Time': '<1hr', 'Occurence': 'Daily', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Retrospective', 'Estimated_Time': '<1hr', 'Occurence': 'Daily', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Retrospective', 'Estimated_Time': '<2hr', 'Occurence': 'Daily', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Retrospective', 'Estimated_Time': '<1hr', 'Occurence': 'Daily', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Retrospective', 'Estimated_Time': '<30min', 'Occurence': 'Daily', 'Boolean': '1'})

        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Stand Up Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Daily', 'Boolean': '0'})

        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Planning', 'Estimated_Time': '<1hr', 'Occurence': 'Annually', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Planning', 'Estimated_Time': '<2hr', 'Occurence': 'Monthly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': 'Sprint Planning', 'Estimated_Time': '<1hr', 'Occurence': 'Monthly', 'Boolean': '0'})

        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Monthly', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<10min', 'Occurence': 'Monthly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<1hr', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '0'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<30min', 'Occurence': 'Weekly', 'Boolean': '1'})
        writer.writerow({'Subject': 'Team_Based', 'Type': '1-On-1 Meeting', 'Estimated_Time': '<1hr', 'Occurence': 'Weekly', 'Boolean': '0'})