#PF-Exer-30

def find_average(mark_list):
	total=0
	for i in range(0, len(mark_list)):
		total+=int(mark_list1[i])
	marks_avg=total/len(mark_list)
	return marks_avg

m_list=[1,2,3,4]
m_list1=["1",2,3,4]
try:
    mark1="A"
    mark1=int("A")
    m_list2=[mark1,2,3,4]

    print("Average marks:", find_average(m_list))
    print("Average marks:", find_average(m_list1))
    print("Average marks:", find_average(m_list2))
except TypeError:
    print("TypeError error")
except :
    print("Common Error")