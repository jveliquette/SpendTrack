from django.test import TestCase, Client
from django.urls import reverse


class FeatureTests(TestCase):
    def test_root_path_redirects_to_receipts(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(
            response.status_code,
            302,
            msg="Did not get a redirect",
        )
        self.assertTrue(
            response.has_header("Location"),
            msg="Response does not redirect to a new URL",
        )
        location = response.headers.get("Location")
        if not location.startswith("/accounts/login/"):
            self.assertEqual(
                location,
                "/receipts/",
                msg="Redirection does not point to /receipts/",
            )

    def test_root_resolves_from_home(self):
        path = reverse("home")
        self.assertEqual(
            path,
            "/receipts/",
            msg="'home' path does not resolve to /receipts/",
        )
