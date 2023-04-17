from django.forms import ValidationError


def validate_phone_number(phone: str):
    phone = phone.replace('', '')
    if len(phone) != 12:
        raise ValidationError('Длина номера не совпадает')

    if not phone.startswith('+7'):
        raise ValidationError('Номер должен начинатся с +7')

    digits = '+0987654321'
    for i in phone:
        if i not in digits:
            raise ValidationError(f'Телефонный номер не может содержать "{i}"!')


def validate_birthdate(birth_date: str):







def validate_iin(iin):
    if len(iin) != 12:
        raise ValidationError('Длина иин не совпадает')
