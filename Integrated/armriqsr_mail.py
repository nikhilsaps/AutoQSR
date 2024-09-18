from outlook_email import create_outlook_draft
from armriemail_content import get_html_content

def armriqsr_mail_prep():
    subject = 'Queue Status ARM Holistic RI'
    to_email = 'ari-preventions@amazon.com'
    cc_email = 'ari-rtm@amazon.com;vtripath@amazon.com;polimern@amazon.com;bramanaa@amazon.com;rkadiyal@amazon.com;kosurun@amazon.com;mravali@amazon.com;'
    from_email = 'buyer-abuse-wfm@amazon.com'  # Add the FROM address here
    html_content = get_html_content()
    
    create_outlook_draft(subject, html_content, to_email, cc_email, from_email)
