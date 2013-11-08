def getPerm(user):
	perms_list = []
	perms = Permission.objects.filter(user=User.objects.get(username=user))
	for perm in perms:
		perms_list.append({perm.page.name: perm.category.types})
		
	return perms_list
	
def addUser(user,pwd,perms):
	usr = User(username=user,password=pwd,is_staf=True)
	usr.save()
	
	for key in perms.keys():
		page = Page.objects.get(name=key)
		cate = Category.objects.get(types=perms[key])
		perm = Permission(user=usr,page=page,category=cate)
		perm.save()
