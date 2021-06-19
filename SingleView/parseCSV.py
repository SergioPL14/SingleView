import pandas
import config

# with open(config.csvFile) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} , {row[1]} , {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

df = pandas.read_csv(config.csvFile)
print(df)

df = df[df['iswc'].notna()]

print(df)

df2 = df.groupby(['contributors']).apply(lambda x: '|'.join(x.contributors))['title', 'iswc']
print(df2)

str = df.at[2, 'iswc']
print('str: ' + str)
