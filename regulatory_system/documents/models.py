from django.db import models

class Document(models.Model):
    DOCUMENT_TYPES = [('IFU','IFU'),
                      ('SOP','SOP'),
                      ('CER','CER'),
                      ('RMF','RMF'),
                      ('LABEL','Labeling'),
                      ]

    title = models.CharField(max_length=255)
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
