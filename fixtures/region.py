#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.lpush('regionname_fullname_template',
                     '{{params.title}} {{params.pre}}{{params.root}}{{params.post}} {{params.trailer}}')
    self.redis.lpush('regionname_shortname_template', '{{params.fullname}}')
    self.redis.lpush('regionname_formalname_template', '{{params.fullname}}')
    self.redis.zadd('region_corruption', '{ "name":"incorruptible",   "score":100    }', 100)
    self.redis.zadd('region_countryapproval', '{ "name":"revere",         "score":100   }', 100)
    self.redis.zadd('region_economic', '{"name":"conservative",     "score":100   }', 100)
    self.redis.zadd('region_efficiency', '{ "name":"ruthlessly effective",               "score":100   }', 100)
    self.redis.zadd('region_influence', '{ "name":"thriving",              "score":100   }', 100)
    self.redis.zadd('region_size', '{"name":"large",    "mincities":5,   "maxcities":20,      "score":100   }', 100)
    self.redis.zadd('region_social', '{"name":"authoritarian",       "score":100   }', 100)
    self.redis.zadd('region_theology', '{ "name":"is used to control the populace",     "score":100    }', 100)
    self.redis.zadd('region_unity', '{ "name":"rallies behind its leaders",             "score":100   }', 100)
    self.redis.lpush('regionname_title', 'New')
    self.redis.lpush('regionname_pre', 'Lom')
    self.redis.lpush('regionname_root', 'bar')
    self.redis.lpush('regionname_post', 'dy')

