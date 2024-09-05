import win32com.client

def create_outlook_draft(subject, body, to_email):
    # Create an instance of Outlook application
    outlook = win32com.client.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)  # 0: Mail item

    # Set up the email parameters
    mail.Subject = subject
    mail.HTMLBody = body
    mail.To = to_email

    # Display the email (open it in Outlook)
    mail.Display()
    print("Draft email opened in Outlook!")
