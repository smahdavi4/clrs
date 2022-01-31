# Copyright 2021 DeepMind Technologies Limited. All Rights Reserved.
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
# ==============================================================================

"""Encoder utilities."""

from clrs._src import specs
import haiku as hk


_Location = specs.Location
_Spec = specs.Spec
_Type = specs.Type


def construct_encoder(loc: str, t: str, hidden_dim: int):
  """Constructs an encoder."""
  encoder = [hk.Linear(hidden_dim)]
  if loc == _Location.EDGE and t == _Type.POINTER:
    # Edge pointers need two-way encoders.
    encoder.append(hk.Linear(hidden_dim))

  return encoder
