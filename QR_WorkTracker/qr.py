import io

import qrcode
import qrcode.image.svg
from django.core import signing

MAX_AGE_SECONDS = 60

def empty_token(machine):
    if not machine.qr_token:
        raise ValueError(f"Machine {machine} has no QR token")
    return machine.qr_token

def create_token(machine):
    return signing.TimestampSigner(key=empty_token(machine)).sign(machine.code)

def verify_token(machine, token):
    try:
        signing.TimestampSigner(key=empty_token(machine)).unsign(token, max_age=MAX_AGE_SECONDS)
    except signing.BadSignature:
        return False
    return True

def render_svg(text):
    buffer = io.BytesIO()
    qrcode.make(text, image_factory=qrcode.image.svg.SvgPathImage).save(buffer)
    return buffer.getvalue()

