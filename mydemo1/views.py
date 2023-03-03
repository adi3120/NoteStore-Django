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
        m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
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
        m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
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
		m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
		cursor=m.cursor()
		global name
		global admin_id
		d=request.POST
		for key,value in d.items():
			if key=="org_name":
				name=value


		c="insert into organisation(name,owner_id) Values('{}','{}')".format(name,admin_id)
		cursor.execute(c)
		m.commit()
		c="select id from organisation where name=%s and owner_id=%s"
		vals=(name,admin_id)
		cursor.execute(c,vals)
		orgid=cursor.fetchall()
		orgid=orgid[0][0]
		c="insert into user_org(userid,orgid) Values('{}','{}')".format(admin_id,orgid)
		cursor.execute(c)
		m.commit()

		


	return render(request,'mydemo1/createOrganisation.html')

def myorganisation(request):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	global admin_id

	c="select * from organisation where id in(select orgid from user_org where userid="+str(admin_id)+")"
	print(c)
	cursor.execute(c)
	a=cursor.fetchall()
	print(a)
	context={
		'or':a
	}

	return render(request,'mydemo1/myorganisation.html',context=context)

def madeorganisation(request):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	global admin_id
	c="select * from organisation where owner_id="+str(admin_id)
	cursor.execute(c)
	a=cursor.fetchall()
	context={
		'a':a
	}
	return render(request,'mydemo1/madeorganisation.html',context=context)


def addUserOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if(key=="user_id"):
				c="insert into user_org values(%s,%s)"
				print(c)
				vals=(value,pk)
				cursor.execute(c,vals)
				m.commit()
	return render(request,'mydemo1/addUserOr.html')

def addUploaderOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if(key=="user_id"):
				c="insert into note_uploader values(%s,%s)"
				print(c)
				vals=(pk,value)
				cursor.execute(c,vals)
				m.commit()
	return render(request,'mydemo1/addUploaderOr.html')
def renameOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if(key=="org_name"):
				c="update organisation set name=%s where id=%s"
				vals=(value,pk)
				cursor.execute(c,vals)
				m.commit()
	c="select name from organisation where id="+str(pk)
	cursor.execute(c)
	oldName=cursor.fetchall()


	context={
		"oldName":oldName[0][0]
	}

	return render(request,'mydemo1/renameOr.html',context=context)

def deleteOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()

	c="delete from organisation where id="+str(pk)
	cursor.execute(c)
	m.commit()
	global admin_id
	c="select * from organisation where owner_id="+str(admin_id)
	cursor.execute(c)
	a=cursor.fetchall()
	context={
		'a':a
	}
	return render(request,'mydemo1/madeorganisation.html',context=context)


def uploadNotesOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	file_name=""
	global admin_id
	c="select count(*) from organisation where id=%s and owner_id=%s"
	vals=(pk,admin_id)
	cursor.execute(c,vals)
	isuploader=cursor.fetchall()
	print(isuploader)
	if isuploader[0][0]==0:
		return render(request,'mydemo1/nottheuploader.html')


	

	

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
		print("OK DONE")
		vals=(note_name,admin_id,pk)
		cursor.execute("select id from note where title=%s and user_id=%s and org_id=%s",vals)
		
		note_id=cursor.fetchall()
		note_id=note_id[0][0]
		c="insert into note_uploader values(%s,%s)"
		x=(note_id,admin_id)
		cursor.execute(c,x)
		m.commit()

		print(note_id)
		for img in images:
			datetime_current=time.strftime('%Y-%m-%d %H:%M:%S')

			image=img.read()

			c="insert into photo(name,date_time,org_id,user_id,note_id,data) values(%s,%s,%s,%s,%s,%s)"
			
			vals=("PIC1.jpeg",datetime_current,pk,admin_id,note_id,image)

			cursor.execute(c,vals)
			m.commit()
	return render(request,'mydemo1/uploadNotesOr.html')

def addPhotosNo(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	file_name=""
	global admin_id

	c="select count(*) from note_uploader where uploader_id=%s and note_id=%s"
	vals=(admin_id,pk)
	cursor.execute(c,vals)
	isuploader=cursor.fetchall()
	print(isuploader)
	if isuploader[0][0]==0:
		return render(request,'mydemo1/nottheuploader.html')
	if request.method=="POST":
		d=request.POST
		
		files=request.FILES

		images=files.getlist('upload')
		print(images)

		datetime_current=time.strftime('%Y-%m-%d %H:%M:%S')

		
		note_id=pk
		c="select org_id from note where id="+str(note_id)
		cursor.execute(c)
		x=cursor.fetchall()
		org_id=x[0][0]
		for img in images:
			datetime_current=time.strftime('%Y-%m-%d %H:%M:%S')

			image=img.read()

			c="insert into photo(name,date_time,org_id,user_id,note_id,data) values(%s,%s,%s,%s,%s,%s)"
			
			vals=("PIC1.jpeg",datetime_current,org_id,admin_id,note_id,image)

			cursor.execute(c,vals)
			m.commit()
	context={
		"note":pk,
	}
	return render(request,'mydemo1/addPhotosNo.html',context=context)


	

def viewNotesOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()

	c="select * from note,user where note.user_id=user.id and note.org_id="+str(pk)
	cursor.execute(c)
	final=cursor.fetchall()
	context={
		'final':final
	}

	return render(request,'mydemo1/viewNotesOr.html',context=context)


def visitNote(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()

	c="select photo.data,photo.id,photo.name,photo.date_time,photo.org_id,organisation.name,photo.user_id,photo.note_id,note.title,user.email from  photo,note,user,organisation where photo.note_id=note.id and photo.user_id=user.id and photo.org_id=organisation.id and note.id="+str(pk)
	cursor.execute(c)

	images_data=cursor.fetchall()


	for i in range(0,len(images_data)):
		images_data[i]=list(images_data[i])
		images_data[i][0]=b64encode(images_data[i][0]).decode("utf-8")

	
	context={
		'images':images_data
	}
		
	return render(request,'mydemo1/visitNote.html',context=context)

def deleteNote(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()
	c="select org_id from note where id="+str(pk)
	cursor.execute(c)
	org_id=cursor.fetchall()
	org_id=org_id[0][0]
	global admin_id
	c="select count(*) from organisation where id=%s and owner_id=%s"
	vals=(org_id,admin_id)
	cursor.execute(c,vals)
	isuploader=cursor.fetchall()
	if isuploader[0][0]==0:
		return render(request,'mydemo1/nottheuploader.html')
	
	c="delete from note where id="+str(pk)
	cursor.execute(c)
	m.commit()
	c="select * from note,user where note.user_id=user.id and note.org_id="+str(org_id)
	cursor.execute(c)
	final=cursor.fetchall()
	context={
		'final':final
	}

	return render(request,'mydemo1/viewNotesOr.html',context=context)

def renameNo(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()

	c="select org_id from note where id="+str(pk)
	cursor.execute(c)
	org_id=cursor.fetchall()
	org_id=org_id[0][0]

	global admin_id
	c="select count(*) from organisation where id=%s and owner_id=%s"
	vals=(org_id,admin_id)
	cursor.execute(c,vals)
	isuploader=cursor.fetchall()

	if isuploader[0][0]==0:
		return render(request,'mydemo1/nottheuploader.html')
	
	if request.method=="POST":
		d=request.POST
		for key,value in d.items():
			if(key=="note_name"):
				c="update note set title=%s where id=%s"
				vals=(value,pk)
				cursor.execute(c,vals)
				m.commit()

	c="select title from note where id="+str(pk)
	cursor.execute(c)
	oldName=cursor.fetchall()


	context={
		"oldName":oldName[0][0]
	}

	return render(request,'mydemo1/renameNo.html',context=context)

def allUserOr(request,pk):
	m=sql.connect(host="localhost",user="root",passwd="MNMisBST@123",database='notestore')
	cursor=m.cursor()

	c="select id,fname,lname,email from user where id in(select userid from user_org where orgid="+str(pk)+")"
	print(c)
	cursor.execute(c)
	val=cursor.fetchall()

	

	c="select name from organisation where id="+str(pk)
	cursor.execute(c)
	org_name=cursor.fetchall()
	org_name=org_name[0][0]

	context={
		'users':val,
		'name':org_name,
	}

	return render(request,"mydemo1/allUserOr.html",context=context)
	