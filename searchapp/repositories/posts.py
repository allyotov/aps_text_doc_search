from searchapp.resources.models import Post, Posts, db
from searchapp.tools.db.sql import field_contains, sqlfilter, sqlorder


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
        query = Posts.query
        text_query = field_contains(query, Posts.text, search_str)
        result_query = sqlorder(text_query, Posts.created_date, order_desc).slice(1, 20)

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

    def check_by_id(self, post_id) -> bool:
        return Posts.query.filter(Posts.id == post_id).count() > 0
