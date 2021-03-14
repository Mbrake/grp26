# Generated by Django 3.1 on 2020-09-10 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20200907_2054"),
    ]

    operations = [
        migrations.CreateModel(
            name="AthleteFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to=users.models.athlete_directory_path),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("a", "Accepted"),
                            ("p", "Pending"),
                            ("d", "Declined"),
                        ],
                        default="p",
                        max_length=8,
                    ),
                ),
                (
                    "offer_type",
                    models.CharField(
                        choices=[("a", "Athlete"), ("c", "Coach")],
                        default="a",
                        max_length=8,
                    ),
                ),
                ("stale", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="coachrequest",
            name="owner",
        ),
        migrations.RemoveField(
            model_name="coachrequest",
            name="recipient",
        ),
        migrations.AlterField(
            model_name="user",
            name="coach",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="athletes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="AthleteRequest",
        ),
        migrations.DeleteModel(
            name="CoachRequest",
        ),
        migrations.AddField(
            model_name="offer",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_offers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="offer",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_offers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="athletefile",
            name="athlete",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="coach_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="athletefile",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="athlete_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
