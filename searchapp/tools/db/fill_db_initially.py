import csv
import logging
from datetime import datetime

from searchapp import create_app
from searchapp.resources.models import Post, Posts, db

logger = logging.getLogger(__name__)


def read_posts_from_csv(csv_path='posts.csv'):
    posts_list = []
    with open(csv_path, mode='r') as input_file:
        reader = csv.reader(input_file)
        next(reader)
        for i, (text, created_date_str, rubrics) in enumerate(reader, start=1): 
            created_date = datetime.strptime(created_date_str, '%Y-%m-%d %H:%M:%S')
            post = Post(
                id=i,
                rubrics=rubrics,
                text=text,
                created_date=created_date
            )
            posts_list.append(post)
    return posts_list


def fill(posts_list):
    total_posts = len(posts_list)
    for post_num, post in enumerate(posts_list, start=1):
        try:
            post_raw = Posts(
                id=post.id,
                rubrics=post.rubrics,
                text=post.text,
                created_date=post.created_date
            )
            db.session.add(post_raw)
            db.session.commit()
            logger.info(f'Post added: {post_num} of {total_posts}')
        except Exception as exc:
            logger.exception("The post with text '%s' wasn't added into db. The reason is: \n%s" % (
                post.text[:10],
                exc,
            ))
            db.session.rollback()

    logger.info('Post search database population is complete.')


def fill_db_from_given_csv(csv_path='posts.csv'):
    posts_list = read_posts_from_csv(csv_path=csv_path)
    app = create_app()
    with app.app_context():
        fill(posts_list)
    logger.info('Population of the db ended.')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s | %(levelname)s: %(message)s',  # noqa: WPS323
    )
    fill_db_from_given_csv()