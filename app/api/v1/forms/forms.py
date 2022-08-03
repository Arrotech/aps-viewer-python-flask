from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import IMAGES


class UploadForm(FlaskForm):
    image = FileField('Image', validators=[
                      FileAllowed(IMAGES, 'only images are accepted.')])
