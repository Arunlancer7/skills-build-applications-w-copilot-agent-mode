from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam', members=['A', 'B'])
        self.assertEqual(team.name, 'TestTeam')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='TestTeam', points=50)
        self.assertEqual(lb.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='Test', workout='Pushup', reps=20)
        self.assertEqual(workout.reps, 20)
