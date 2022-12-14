from app.models import User
from app.db import Session, Base, engine
from app.models import User, Post, Comment, Vote

#Drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
  User(username='alfredo', email='pizzaByAlfredo@gmail.com', password='password123'),
  User(username='alfred', email='pizzaByAlfred@gmail.com', password='password123'), 
  User(username='alf', email='Alf@gmail.com', password='password123'),
  User(username='fred', email='fred@gmail.com', password='password123'),
  User(username='Jzargo', email='Jzargo@gmail.com', password='password123'),
  ])

db.commit()

# insert posts
db.add_all([
  Post(title='Donec posuere metus vitae ipsum', post_url='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', user_id=1),
  Post(title='Morbi non quam nec dui luctus rutrum', post_url='https://nasa.gov/donec.json', user_id=1),
  Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', post_url='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', user_id=2),
  Post(title='Nunc purus', post_url='http://desdev.cn/enim/blandit/mi.jpg', user_id=3),
  Post(title='Pellentesque eget nunc', post_url='http://google.ca/nam/nulla/integer.aspx', user_id=4)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Hey NICE POST.', user_id=1, post_id=2),
  Comment(comment_text='HEY YO WOW SUPER COOL.', user_id=1, post_id=3),
  Comment(comment_text='SUGAR COOkIES.', user_id=2, post_id=1),
  Comment(comment_text='Hello.', user_id=2, post_id=3),
  Comment(comment_text='Well, no I did not love it.', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()

db.close()