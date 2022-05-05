from searchapp.resources.models import Post, Posts, db, es
from searchapp.tools.db.sql import sqlorder


class PostsRepo:

    def get_all(self, order_desc=False):
        query = Posts.query
        result_query = sqlorder(query, Posts.created_date, order_desc).slice(1, 20)

        return [
            Post(
                post.id,
                post.rubrics,
                post.text,
                post.created_date,
            )
            for post in result_query
        ]

    def find_any_inclusions(self, order_desc=False, search_str: str = None):
        q = {"query": {"match_phrase": {"text": search_str}}, "size": 20}

        ids = [int(post['_id']) for post in es.search(index='post-index', body=q)['hits']['hits']]

        result_query = sqlorder(
            Posts.query, 
            Posts.created_date, 
            order_desc
        ).filter(Posts.id.in_(ids)).all()

        return [
            Post(
                post.id,
                post.rubrics,
                post.text,
                post.created_date,
            )
            for post in result_query
        ]

    def delete(self, post_id):
        post_to_delete = Posts.query.filter(Posts.id == post_id).first()
        db.session.delete(post_to_delete)
        db.session.commit()
        es.delete(index='post-index', id=post_id)

    def check_by_id(self, post_id) -> bool:
        return Posts.query.filter(Posts.id == post_id).count() > 0
