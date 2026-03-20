from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample teams
        marvel_team = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc_team = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Sample users
        User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        User.objects.create(name='Thor', email='thor@marvel.com', team='Marvel')
        User.objects.create(name='Superman', email='superman@dc.com', team='DC')
        User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='DC')

        # Sample activities
        Activity.objects.create(user='Iron Man', activity='Running', duration=30)
        Activity.objects.create(user='Batman', activity='Cycling', duration=45)

        # Sample leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Sample workouts
        Workout.objects.create(user='Thor', workout='Weightlifting', reps=100)
        Workout.objects.create(user='Wonder Woman', workout='Yoga', duration=60)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
