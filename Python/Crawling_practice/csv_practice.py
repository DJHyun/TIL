import csv

lunch = [{
    '김밥카페':'02-1234-5678',
    '양자강':'02-2345-6789',
    '순남시래기':'02-9876-5432'
}]

lunch2 = [
    {
    '상호명':'양자강',
    '전화번호':'02-2345-6789'
    }
]

menu = ['김밥','탕수육','시래기']
# 리스트를 가지고 csv를 만들때(writerow -> 리스트를 인자)
# with open('lunch.csv','w') as f:
#     writer = csv.writer(f)
#     writer.writerow(menu)

# 딕셔너리를 가지고 csv를 만들때(DictWriter.writerow -> dict를 인자)
with open('lunch.csv','w') as f:
    field = ('상호명','전화번호')
    writer = csv.DictWriter(f,fieldnames = field)
    writer.writeheader()
    for l in lunch2:
        writer.writerow(l)

# csv를 읽는것
with open('lunch.csv',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    



f.close()