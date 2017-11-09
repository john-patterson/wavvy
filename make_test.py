from wavvy.datalayer import models, procedures
models.db.create_all()
procedures.add_user(
    username='thejay2012@gmail.com',
    plain_password='password'
)
