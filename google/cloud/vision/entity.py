# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Entity class for holding information returned from annotating an image."""


from google.cloud.vision.geometry import Bounds


class EntityAnnotation(object):
    """Representation of an entity returned from the Vision API.

    :type bounds: dict
    :param bounds: Dictionary of bounary information of detected entity.

    :type description: str
    :param description: Description of entity detected in an image.

    :type mid: str
    :param mid: Opaque entity ID.

    :type score: float
    :param score: Overall score of the result. Range [0, 1].
    """
    def __init__(self, bounds, description, mid, score):
        self._bounds = bounds
        self._description = description
        self._mid = mid
        self._score = score

    @classmethod
    def from_api_repr(cls, response):
        """Factory: construct entity from Vision API response.

        :type response: dict
        :param response: Dictionary response from Vision API with entity data.

        :rtype: :class:`~google.cloud.vision.entiy.EntityAnnotation`
        :returns: Instance of ``EntityAnnotation``.
        """
        bounds = Bounds.from_api_repr(response['boundingPoly'])
        description = response['description']
        mid = response['mid']
        score = response['score']

        return cls(bounds, description, mid, score)

    @property
    def bounds(self):
        """Bounding polygon of detected image feature.

        :rtype: :class:`~google.cloud.vision.geometry.Bounds`
        :returns: Instance of ``Bounds`` with populated vertices.
        """
        return self._bounds

    @property
    def description(self):
        """Description of feature detected in image.

        :rtype: str
        :returns: String description of feature detected in image.
        """
        return self._description

    @property
    def mid(self):
        """MID of feature detected in image.

        :rtype: str
        :returns: String MID of feature detected in image.
        """
        return self._mid

    @property
    def score(self):
        """Overall score of the result. Range [0, 1].

        :rtype: float
        :returns: Overall score of the result. Range [0, 1].
        """
        return self._score
