from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Testers')
        self.assertEqual(str(t), 'Testers')
    def test_user_create(self):
        t = Team.objects.create(name='Testers')
        u = User.objects.create_user(username='test', email='test@example.com', password='pw', team=t)
        self.assertEqual(u.email, 'test@example.com')
    def test_activity_create(self):
        t = Team.objects.create(name='Testers')
        u = User.objects.create_user(username='test', email='test@example.com', password='pw', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10, points=5)
        self.assertEqual(a.type, 'run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W1', description='desc', suggested_points=10)
        self.assertEqual(w.name, 'W1')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Testers')
        l = Leaderboard.objects.create(team=t, total_points=100)
        self.assertEqual(l.total_points, 100)
