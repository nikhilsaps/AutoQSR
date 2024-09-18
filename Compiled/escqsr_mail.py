from outlook_email import create_outlook_draft
from escemail_content import get_html_content

def escqsr_mail_prep():
    subject = 'Queue Status Escalations'
    to_email = 'ari-ww-escalations@amazon.com'
    cc_email = 'mohprave@amazon.com'
    from_email = 'buyer-abuse-wfm@amazon.com'  # Add the FROM address here
    html_content = get_html_content()
    
    create_outlook_draft(subject, html_content, to_email, cc_email, from_email)
