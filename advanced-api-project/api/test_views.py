from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create some test books
        self.book1 = Book.objects.create(title="Book One", author="Author A")
        self.book2 = Book.objects.create(title="Book Two", author="Author B")

        self.create_url = reverse("book-list")  # Assuming you use DRF's DefaultRouter
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})

    # -------------------
    # TEST CREATE BOOK
    # -------------------
    def test_create_book(self):
        data = {"title": "New Book", "author": "Author C"}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

    # -------------------
    # TEST LIST BOOKS
    # -------------------
    def test_list_books(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------
    # TEST RETRIEVE BOOK
    # -------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -------------------
    # TEST UPDATE BOOK
    # -------------------
    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Author A"}
        response = self.client.put(self.detail_url(self.book1.id), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # -------------------
    # TEST DELETE BOOK
    # -------------------
    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    # -------------------
    # TEST PERMISSIONS / AUTH
    # -------------------
    def test_unauthenticated_cannot_create(self):
        self.client.logout()
        data = {"title": "No Auth Book", "author": "Author X"}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
