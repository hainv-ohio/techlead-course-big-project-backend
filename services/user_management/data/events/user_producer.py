

class UserProducer:
    def record_login_event(self, email):
        self.producer.send('topic', {'email': email})
