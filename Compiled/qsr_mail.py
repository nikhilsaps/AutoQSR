from outlook_email import create_outlook_draft
from email_content import get_html_content

def qsr_mail_prep():
    subject = 'ARI Queue Status Report'
    to_email = 'manideer@amazon.com;abhijida@amazon.com;ari-coreteam@amazon.com;ari-mteam@amazon.com;ari-email-mteam@amazon.com'
    cc_email = 'ari-rtm@amazon.com;bao-lt@amazon.com'  # Add your CC addresses here
    from_email = 'buyer-abuse-wfm@amazon.com'  # Add the FROM address here
    html_content = get_html_content()
    
    create_outlook_draft(subject, html_content, to_email, cc_email, from_email)
