from dataclasses import asdict
from typing import Optional
import logging
from flask import Blueprint, abort, jsonify, make_response, request
from marshmallow import ValidationError 

from searchapp.repositories.posts import PostsRepo
from searchapp.resources.schemas import PostSchema

routes = Blueprint('routes', __name__)

repo = PostsRepo()
validator = PostSchema()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@routes.route('', methods=['GET'])
def search():
    order: Optional[str] = request.args.get('order', type=str, default='asc')
    search_str: Optional[str] = request.args.get('search', type=str, default='')
    desc = order == 'desc'
    if search_str:
        posts = repo.find_any_inclusions(desc, search_str)
    else:
        posts = repo.get_all(desc)
    return jsonify(posts)


@routes.route('<uid>', methods=['DELETE'])
def delete(uid: int):
    if not repo.check_by_id(uid):
        abort(make_response(jsonify(message=f"Post with id {uid} doesn\'t exist."), 400))

    repo.delete(uid)
    return '', 204
