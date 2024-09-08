import win32com.client

def create_outlook_draft(subject, body, to_email, cc_email=None, from_email=None):
    # Create an instance of Outlook application
    outlook = win32com.client.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)  # 0: Mail item

    # Set up the email parameters
    mail.Subject = subject
    mail.HTMLBody = body
    mail.To = to_email
    
    if cc_email:
        mail.CC = cc_email

    if from_email:
        # Note: Setting the FROM address usually requires the sender to have permission to send on behalf of that address
        mail.SentOnBehalfOfName = from_email

    # Display the email (open it in Outlook)
    mail.Display()
    print("Draft email opened in Outlook!")
