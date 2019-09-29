from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Steve',
    email='steve777@gmail.com',
    picture='file:///C:/Users/test/Downloads/fullstack/vagrant/catalog3/images/d262ebcbbe8caa9386fbfc09f4d00b6d.png'
)

session.add(user1)
session.commit()

category1 = Category(
    name='T-Shirts',
    user=user1
)

session.add(category1)
session.commit()

category2 = Category(
    name='Hoodies',
    user=user1
)

session.add(category2)
session.commit()

category3 = Category(
    name='Joggers',
    user=user1
)

session.add(category3)
session.commit()

category4 = Category(
    name='Shoes',
    user=user1
)

session.add(category4)
session.commit()

item1 = Item(
    name='Balmain T-Shirt In Black',
    description='Balmain T-Shirt in black with print logo design on front and crew neckline',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

item2 = Item(
    name='Balmain T-Shirt In Red',
    description='Balmain T-Shirt in red with print logo design on front and crew neckline',
    category=category1,
    user=user1
)

session.add(item2)
session.commit()

item3 = Item(
    name='Balmain Hoodie in Black',
    description='Balmain hoodie in black with zip fastening on the sides.',
    category=category2,
    user=user1
)

session.add(item3)
session.commit()

item4 = Item(
    name='Balmain Logo Joggers In Black',
    description='Balmian Logo joggers in black with side stripe and waist band detailing',
    category=category3,
    user=user1
)

session.add(item4)
session.commit()

item5 = Item(
    name='Balmain Cameron Mesh Trainer in White',
    description='Balmain Cameron Mesh trainer in white with sock design and signature balmain logo on strap',
    category=category4,
    user=user1
)

session.add(item5)
session.commit()

item6 = Item(
    name='Balmain Cameron Mesh Trainer in Black',
    description='Balmain Cameron Mesh trainer in black with sock design and signature balmain logo on strap',
    category=category4,
    user=user1
)

session.add(item6)
session.commit()

item7 = Item(
    name='Moschino Mens Roman Teddy Bear T-Shirt',
    description='Moschino Roman Teddy Bear T-Shirt with print logo and design on front',
    category=category1,
    user=user1
)

session.add(item7)
session.commit()

item8 = Item(
    name='Moschino T-Shirt In White',
    description='Moschino T-Shirt in white with bold print logo across chest and crew neckline',
    category=category1,
    user=user1
)

session.add(item8)
session.commit()

item10 = Item(
    name='Moschino T-Shirt In Black',
    description='Moschino T-Shirt in black with bold print logo across chest and crew neckline',
    category=category1,
    user=user1
)

item12 = Item(
    name='Moschino Roman T-Shirt In Black',
    description='Moschino Roman T-Shirt in black with bold print logo across chest and crew neckline',
    category=category1,
    user=user1
)

session.add(item12)
session.commit()

item13 = Item(
    name='Stone Island T-Shirt In White',
    description='Stone Island T-Shirt in white with embroidered patch logo on chest and crew neckline',
    category=category1,
    user=user1
)

session.add(item13)
session.commit()

item14 = Item(
    name='Stone Island Jogger In Blue',
    description='Stone Island jogger in blue with signature badge logo on leg and drawstring waist',
    category=category3,
    user=user1,
)

session.add(item14)
session.commit()

print('Finished populating the database!')