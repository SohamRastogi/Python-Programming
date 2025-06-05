class Main_Notitfication_Centre :
    def send_notification (self) :
        print("notification sended from the Notification_Centre to the user.")
    
class Sub1_Notification_Centre(Main_Notitfication_Centre) :
    pass
class Sub2_Notification_Centre(Main_Notitfication_Centre) :
    pass

# now we can make these inherited class as per our wish in number

m1 = Sub1_Notification_Centre().send_notification()
m2 = Sub2_Notification_Centre().send_notification()
    