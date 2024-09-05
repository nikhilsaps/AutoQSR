from outlook_email import create_outlook_draft
from email_content import get_html_content

def qsr_mail_prep():
    subject = 'Three Rows of Five Tables'
    to_email = 'example@noone.com'
    html_content = get_html_content()
    
    create_outlook_draft(subject, html_content, to_email)
