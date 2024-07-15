from django.db import models

# Create your models here.

class Main(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class BI_PE(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class LAW(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class POLIT(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class M(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class E(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class HIST(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class Main_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()
    def __str__(self):
        return self.text

class BI_PE_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class LAW_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class POLIT_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class M_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class E_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class HIST_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class Main_pecase(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class school_pecase(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class uni_pecase(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word

class uni_pecase_fem(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word


class uni_pecase_man(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word


class uni_pecase_mf(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word


class school_pecase_fem(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word


class school_pecase_man(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()

    def __str__(self):
        return self.word


class Main_pecase_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class school_pecase_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class uni_pecase_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class uni_pecase_fem_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class uni_pecase_man_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class uni_pecase_mf_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text


class school_pecase_fem_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text

class school_pecase_man_ngram(models.Model):
    text = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.FloatField()
    normalized_range = models.FloatField()
    ngram = models.IntegerField()

    def __str__(self):
        return self.text