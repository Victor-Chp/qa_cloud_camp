import requests

url = "https://jsonplaceholder.typicode.com/"
url_posts = url + "posts"


def test_get_all_posts():
    response = requests.get(url_posts)

    assert response.status_code == 200
    assert response.json()[-1]["id"] > 0


def test_get_one_post_id():
    id_post = 55
    response = requests.get(f"{url_posts}/{id_post}")

    assert response.status_code == 200
    assert response.json()["id"] == id_post


def test_get_all_comments_for_post_id():
    id_post = 44
    response = requests.get(f"{url_posts}/{id_post}/comments")

    assert response.status_code == 200
    assert response.json()[-1]["postId"] == id_post


def test_get_all_posts_from_user_id():
    id_user = 2
    response = requests.get(url_posts, params={"userId": id_user})

    assert response.status_code == 200
    assert response.json()[-1]["userId"] == id_user


def test_get_all_posts_from_incorrect_user_id():
    params = {"userId": -1}
    response = requests.get(url_posts, params)

    assert response.status_code == 200
    assert response.json() == []

def test_send_post():
    json_post = {"userID": 3, "title": "Hello World!", "body": "It's a beautiful day!"}
    headers_post = {"Content-type": "application/json; charset=UTF-8"}
    response = requests.post(url_posts, json=json_post, headers=headers_post)
    json_post["id"] = response.json()["id"]

    assert response.status_code == 201
    assert json_post == response.json()


def test_delete_post():
    id_post = 1
    response = requests.delete(f"{url_posts}/{id_post}")

    assert response.status_code == 200

