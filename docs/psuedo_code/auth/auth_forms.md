# Pseudo Code for Auth/Forms.py

## Import Dependencies

Import FlaskForm from flask_wtf
Import StringField, PasswordField, SubmitField, BooleanField from wtforms
Import DataRequired, Email, EqualTo, Length, ValidationError from wtforms.validators
Import User model to perform email uniqueness check

---

## Registration Form

class RegistrationForm(FlaskForm):
    Field: username
        - Type: StringField
        - Validators: DataRequired, Length(min=3, max=50)

    Field: email
        - Type: StringField
        - Validators: DataRequired, Email()

    Field: password
        - Type: PasswordField
        - Validators: DataRequired, Length(min=8)

    Field: confirm_password
        - Type: PasswordField
        - Validators: DataRequired, EqualTo('password')

    Field: submit
        - Type: SubmitField

    Custom Validator: validate_email(self, email)
        - Query database to see if user with that email exists
        - If yes: raise ValidationError("Email already in use.")

---

## Login Form

class LoginForm(FlaskForm):
    Field: email
        - Type: StringField
        - Validators: DataRequired, Email()

    Field: password
        - Type: PasswordField
        - Validators: DataRequired

    Field: remember
        - Type: BooleanField ("Remember Me")

    Field: submit
        - Type: SubmitField

---

## Miscellaneous

* In the HTML templates, use `{{ form.hidden_tag() }}` to include CSRF token.
* Password validation rules (uppercas, lowercase, digits, special char) can be added as custom validators.
* Field naming must match `request.form['email']` in the routh if not using `form.email.data`
