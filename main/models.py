from django.db import models


class Keypair(models.Model):
    ident = models.IntegerField(default = 0)
    bits = models.IntegerField(default = 0)
    public_key = models.CharField(max_length= 999999, default = '')
    private_key = models.CharField(max_length= 999999, default = '')
    def __str__ (self):
        return str(self.ident) +'-'+str(self.bits)

class Certificate (models.Model):
    ident = models.IntegerField(default = 0)
    subject = models.CharField(max_length = 999999)
    serial_number = models.CharField(max_length = 999999)
    issuer = models.CharField(max_length = 999999)
    certificate = models.CharField(max_length = 999999, default = '')
    def __str__ (self):
        return self.serial_number

class CertificateAutority (models.Model):
    ident = models.IntegerField(default = 0)
    private_key = models.CharField(max_length = 999999, default = '')
    public_key = models.CharField(max_length = 999999, default = '')
    name = models.CharField(max_length = 100)
