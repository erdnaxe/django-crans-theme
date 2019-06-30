# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.test import TestCase


class TagModelTests(TestCase):
    def test_login_page(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

