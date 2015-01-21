from django.db import models


class Join(models.Model):
	email = models.EmailField()
	friends = models.ForeignKey("self", related_name='referral', null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	ip_address = models.IPAddressField(max_length=120, default='ABC')

	def __unicode__(self):
		return self.email

	class META:
		unique_together = ('email', 'ref_id',)


# class JoinFriends(models.Model):
# email = models.OneToOneField(Join, related_name="Sharer")
# friends = models.ManyToManyField(Join, related_name="friends", blank=True, null=True)
# 	emailall = models.ForeignKey(Join, related_name="emailall")
#
# 	def __unicode__(self):
# 		print("friends are : %s " % self.friends.all())
# 		print("emails are : %s " % self.emailall)
# 		print("email is : %s " % self.email)
#
# 		return self.email.email
#
# 	class META:
# 		unicode()
