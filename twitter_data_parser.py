import json,sys

#input, output file name set
try:
	input_file_name=sys.argv[1]
#print(sys.argv[1])
	temp=input_file_name.split(".")
	output_file_name=temp[0]+"_parsed."+temp[1]
	print(output_file_name)
except e:
	print ("Enter proper filename")


tweet=open(input_file_name,"r") # input the file name


output=open(output_file_name,"w")


for line in tweet:
	line_object=json.loads(line)
	try:
		tweet_body=line_object["text"]
		#print(tweet_body)
		tweet_time=line_object["created_at"]
		#print(tweet_time)
		print_string="{body:\""+tweet_body+"\"},{tweet_time:\""+tweet_time+"}\n"
		#output.write(print_string)
		#print(print_string.encode('utf8'))
		output.write(print_string.encode('utf8'))
	except KeyError:
		print ("Error! Error \n")
		tweet_body = "Null"
		tweet_time = "Null"

tweet.close()	
#print (tweet)

