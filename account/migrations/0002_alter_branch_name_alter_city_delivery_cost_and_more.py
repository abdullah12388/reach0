# Generated by Django 4.1.7 on 2023-06-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(choices=[(' فرع امبابة ', 'فرع امبابة'), (' فرع فيصل ', 'فرع فيصل'), (' فرع غمرة ', 'فرع غمرة'), (' فرع مصر الجديدة ', 'فرع مصر الجديدة'), (' فرع الخليفة المامون ', 'فرع الخليفة المامون'), (' فرع الخلفاوي ', 'فرع  الخلفاوي'), (' فرع شارع الترعة ', 'فرع شارع الترعة'), (' فرع منيه السيرج ', 'فرع منبه السيرج')], max_length=50),
        ),
        migrations.AlterField(
            model_name='city',
            name='delivery_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='delivery_cost',
            field=models.FloatField(default=0),
        ),
    ]
