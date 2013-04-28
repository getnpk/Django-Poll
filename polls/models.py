from django.db import models
import datetime
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
    	return self.question

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll) #That tells Django each Choice is related to a single Poll
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    #p.choice_set.create(choice='Not much', votes=0)

    def __unicode__(self):
    	return self.choice
'''
$ python manage.py sql polls
BEGIN;
CREATE TABLE `polls_poll` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `question` varchar(200) NOT NULL,
    `pub_date` datetime NOT NULL
)
;
CREATE TABLE `polls_choice` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `poll_id` integer NOT NULL,
    `choice` varchar(200) NOT NULL,
    `votes` integer NOT NULL
)
;
ALTER TABLE `polls_choice` ADD CONSTRAINT `poll_id_refs_id_3aa09835` FOREIGN KEY (`poll_id`) REFERENCES `polls_poll` (`id`);

COMMIT;
'''    