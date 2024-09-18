from outlook_email import create_outlook_draft
from invemail_content import get_html_content

def invqsr_mail_prep():
    subject = 'Queue Status'
    to_email = 'trms-ari-blr@amazon.com;trms-ari-hyd@amazon.com;ari-sjo-operations@amazon.com;ari-hyd@amazon.com;ari-hyd-in@amazon.com;ari-lang-wwteam@amazon.com'
    cc_email = 'ari-rtm@amazon.com;'  # Add your CC addresses here
    from_email = 'buyer-abuse-wfm@amazon.com'  # Add the FROM address here
    html_content = get_html_content()
    
    create_outlook_draft(subject, html_content, to_email, cc_email, from_email)
