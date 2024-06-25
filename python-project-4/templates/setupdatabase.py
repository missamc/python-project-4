from basic import db, Users


#CREATES ALL THE TABLES Model=> Db Table
db.create_all()


sam = Users('Sammy',32)
frank = Users('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])


#individual way to add names into db, up top is as a group
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
