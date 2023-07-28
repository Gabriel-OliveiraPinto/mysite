import json

import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status.code == 200
    
    import pdb; pdb.set_trace()

    response = json.loads(response.content)
    assert response.content == 'Hello'