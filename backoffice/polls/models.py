from foundation import models


class Question(models.Question):

    class Meta:
        proxy = True

class Choice(models.Choice):

    class Meta:
        proxy = True
