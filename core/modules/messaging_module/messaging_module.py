

from abc import abstractmethod


class MessagingModule:

    @abstractmethod
    async def init(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create_topics(self, topics, *args, **kwargs):
        pass

    @abstractmethod
    async def send(self, topic, data, key=None, *args, **kwargs): raise NotImplementedError


    @abstractmethod
    async def subscribe(self, topic, id, callback, key=None, *args, **kwargs): raise NotImplementedError


    @abstractmethod
    async def unsubscribe(self, topic, id, key=None, *args, **kwargs): raise NotImplementedError


    @abstractmethod
    async def flush(self, *args, **kwargs):
        pass

    @abstractmethod
    async def close(self, *args, **kwargs):
        pass