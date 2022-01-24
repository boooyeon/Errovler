from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.CharField(max_length=45,  primary_key=True)
    pw = models.CharField(max_length=45, null=False)
    nickname = models.CharField(max_length=45, null=False)
   
    class Meta:
        db_table = 'Member'
        managed = False



class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    id = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='id')
    b_date = models.DateTimeField(null=False, default='CURRENT_TIMESTAMP')
    contents = models.TextField(null=False)
    view = models.IntegerField(null=False, default=0)
    like = models.IntegerField( null=False, default=0)


    class Meta:
        db_table = 'Board'
        managed = False


class QnA_Board(models.Model):
    qna_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    qna_yn = models.CharField(max_length=10, null=False, default='N')
    id = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='id')
    qna_date = models.DateTimeField(null=False)
    contents = models.TextField(null=False)
    view = models.IntegerField(null=False, default=0)
    like = models.IntegerField( null=False, default=0)

    class Meta:
        db_table = 'QnA_Board'
        managed = False

class Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    qna_date = models.DateTimeField(null=False)
    contents = models.CharField(max_length=500, null=False)
    id = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='id')

    class Meta:
        db_table = 'Comment'
        managed = False


class Scrap(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    id = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='id')
    class Meta:
        db_table = 'Scrap'
        managed = False

class Photo_Board(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    filename = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'Photo_Board'
        managed = False



class Like_Board(models.Model):
    l_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    id = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='id')

    class Meta:
        db_table = 'Like_Board'
        managed = False