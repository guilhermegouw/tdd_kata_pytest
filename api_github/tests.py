from json import loads

from api_github import github

_resp_renzon = loads('''{
  "login": "renzon",
  "id": 3457115,
  "node_id": "MDQ6VXNlcjM0NTcxMTU=",
  "avatar_url": "https://avatars3.githubusercontent.com/u/3457115?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/renzon",
  "html_url": "https://github.com/renzon",
  "followers_url": "https://api.github.com/users/renzon/followers",
  "following_url": "https://api.github.com/users/renzon/following{/other_user}",
  "gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
  "organizations_url": "https://api.github.com/users/renzon/orgs",
  "repos_url": "https://api.github.com/users/renzon/repos",
  "events_url": "https://api.github.com/users/renzon/events{/privacy}",
  "received_events_url": "https://api.github.com/users/renzon/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Renzo Nuccitelli",
  "company": "Python Pro",
  "blog": "https://www.python.pro.br",
  "location": "Brazil",
  "email": null,
  "hireable": true,
  "bio": null,
  "public_repos": 159,
  "public_gists": 58,
  "followers": 487,
  "following": 3,
  "created_at": "2013-02-02T14:15:53Z",
  "updated_at": "2020-04-14T00:05:19Z"
}
''')


class ResponseMock:
    def json(self):
        return _resp_renzon


def get_mock(user):
    return ResponseMock()


def test_avatar():
    # Setup
    github.requests.get = get_mock
    # Test
    assert "https://avatars3.githubusercontent.com/u/3457115?v=4" == github.get_avatar('renzon')


def test_avatar_guilherme():
    # Setup
    github.requests.get = get_mock
    # Test
    assert "https://avatars3.githubusercontent.com/u/3457115?v=4" == github.get_avatar('renzon')
