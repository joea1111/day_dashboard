from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import NGOActivity

# --- Lab 12 Task 2: Unit Testing (Model Test) ---
class NGOActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = NGOActivity.objects.create(
            ngo_name="Test NGO",
            description="Test Description",
            location="Test Location",
            service_type="Health",
            max_employees=5,
            current_slots_taken=0
        )
        self.assertEqual(activity.ngo_name, "Test NGO")
        # Check if the calculated property remaining_slots works
        self.assertEqual(activity.remaining_slots, 5)

# --- Lab 12 Task 3: Integration & API Testing ---
class NGOActivityAPITest(APITestCase):
    def setUp(self):
        self.activity = NGOActivity.objects.create(
            ngo_name="Initial NGO",
            description="Test description",
            location="KL",
            service_type="Health",
            max_employees=10,
            current_slots_taken=0
        )
        self.list_url = '/api/activities/'

    def test_get_activities_list(self):
        # Integration test (View + Model + Data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_create_activity_api(self):
        # API test (JSON post and verification)
        data = {
            "ngo_name": "New NGO",
            "description": "API Test Activity",
            "location": "PJ",
            "service_type": "Social",
            "max_employees": 20,
            "current_slots_taken": 0
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NGOActivity.objects.count(), 2)
