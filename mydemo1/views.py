from django.shortcuts import render
import mysql.connector as sql
import mysql.connector
from mysql.connector import errorcode
import PIL
import time
from base64 import b64encode
# Create your views here.


fn=''
ln=''
phn=''
email=''
admin_id=0

def index(request):
	return render(request,'mydemo1/home.html')

fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signup(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into user(fname,lname,email,password) Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'mydemo1/signup.html')

em=''
pwd=''
# Create your views here.
def login(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from user where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
		
        if t==():
            return render(request,'mydemo1/error.html')
        else:
            global admin_id
            admin_id=t[0][0]
            print("admin id="+str(admin_id))
            return render(request,"mydemo1/welcome.html",context={'fname':t[0][1],'lname':t[0][2]})
    
    return render(request,'mydemo1/login.html')

def createorganisation(request):
	if request.method=="POST":
		m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
		cursor=m.cursor()
		global name
		global admin_id
		d=request.POST
		for key,value in d.items():
			if key=="org_name":
				name=value

		print(name,admin_id)

		c="insert into organisation(name,admin_id) Values('{}','{}')".format(name,admin_id)
		cursor.execute(c)
		m.commit()



		# c="insert into user_organisation Values('{}','{}')".format(admin_id,)
		# cursor.execute(c)
		# m.commit()


	return render(request,'mydemo1/createOrganisation.html')


def joinorganisation(request):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()
	c="select * from organisation,user where organisation.admin_id=user.id"
	cursor.execute(c)
	final=cursor.fetchall()

	context={
		'final':final
	}
	
	return render(request,'mydemo1/joinOrganisation.html',context=context)

def myorganisation(request):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()
	global admin_id

	c="select * from user_organisation where user_id="+str(admin_id)
	cursor.execute(c)
	a=cursor.fetchall()
	organisations=[]
	for i in a:
		c="select * from organisation where id="+str(i[1])
		cursor.execute(c)
		organisations.append(cursor.fetchall()[0])
	print(organisations)
	context={
		'or':organisations
	}

	return render(request,'mydemo1/myorganisation.html',context=context)

def madeorganisation(request):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()
	global admin_id
	c="select * from organisation where admin_id="+str(admin_id)
	cursor.execute(c)
	a=cursor.fetchall()
	context={
		'a':a
	}
	return render(request,'mydemo1/madeorganisation.html',context=context)


def addUserOr(request):

	return render(request,'mydemo1/addUserOr.html')
def addUploaderOr(request):
	return render(request,'mydemo1/addUploaderOr.html')
def renameOr(request):
	return render(request,'mydemo1/renameOr.html')

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def uploadNotesOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()
	file_name=""
	global admin_id

	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if key=="note_name":
				note_name=value
		files=request.FILES

		images=files.getlist('upload')

		datetime_current=time.strftime('%Y-%m-%d %H:%M:%S')
		c="insert into note(title,date_time,user_id,org_id) Values(%s,%s,%s,%s)"
		vals=(note_name,datetime_current,admin_id,pk)
		cursor.execute(c,vals)
		m.commit()
		# for key,value in images:
		# 	print(key,value)
		cursor.execute("select id from note where title='{}' and user_id={} and org_id={}".format(note_name,admin_id,pk))
		note_id=cursor.fetchall()
		note_id=note_id[0][0]
		for img in images:
			datetime_current=time.strftime('%Y-%m-%d %H:%M:%S')

			image=img.read()

			c="insert into photo(name,date_time,org_id,user_id,note_id,data) values(%s,%s,%s,%s,%s,%s)"
			
			vals=("PIC1.jpeg",datetime_current,pk,admin_id,note_id,image)

			cursor.execute(c,vals)
			m.commit()
	return render(request,'mydemo1/uploadNotesOr.html')

def viewNotesOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()

	c="select * from note,user where note.user_id=user.id"
	cursor.execute(c)
	final=cursor.fetchall()
	context={
		'final':final
	}

	return render(request,'mydemo1/viewNotesOr.html',context=context)


def visitNote(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='testing')
	cursor=m.cursor()

	c="select photo.data,photo.id,photo.name,photo.date_time,photo.org_id,organisation.name,photo.user_id,photo.note_id,note.title,user.email from  photo,note,user,organisation where photo.note_id=note.id and photo.user_id=user.id and photo.org_id=organisation.id and note.id="+str(pk)
	cursor.execute(c)

	images_data=cursor.fetchall()

	# images_file=[]

	for i in range(0,len(images_data)):
		images_data[i]=list(images_data[i])
		images_data[i][0]=b64encode(images_data[i][0]).decode("utf-8")

	# for i in images_data:
	# 	images_file.append(b64encode(i[0]).decode("utf-8"))
	
	context={
		'images':images_data
	}
		
	return render(request,'mydemo1/visitNote.html',context=context)