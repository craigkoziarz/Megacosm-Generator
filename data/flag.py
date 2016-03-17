#

self.redis.lpush('flagcolor', 'verylightred       ')
self.redis.lpush('flagcolor', 'lightred           ')
self.redis.lpush('flagcolor', 'red                ')
self.redis.lpush('flagcolor', 'darkred            ')
self.redis.lpush('flagcolor', 'verydarkred        ')
self.redis.lpush('flagcolor', 'verylightblue      ')
self.redis.lpush('flagcolor', 'lightblue          ')
self.redis.lpush('flagcolor', 'blue               ')
self.redis.lpush('flagcolor', 'darkblue           ')
self.redis.lpush('flagcolor', 'verydarkblue       ')
self.redis.lpush('flagcolor', 'verylightgreen     ')
self.redis.lpush('flagcolor', 'lightgreen         ')
self.redis.lpush('flagcolor', 'green              ')
self.redis.lpush('flagcolor', 'darkgreen          ')
self.redis.lpush('flagcolor', 'verydarkgreen      ')
self.redis.lpush('flagcolor', 'verylightyellow    ')
self.redis.lpush('flagcolor', 'lightyellow        ')
self.redis.lpush('flagcolor', 'yellow             ')
self.redis.lpush('flagcolor', 'darkyellow         ')
self.redis.lpush('flagcolor', 'lightorange        ')
self.redis.lpush('flagcolor', 'orange             ')
self.redis.lpush('flagcolor', 'gold               ')
self.redis.lpush('flagcolor', 'lightgrey          ')
self.redis.lpush('flagcolor', 'grey               ')
self.redis.lpush('flagcolor', 'darkgrey           ')
self.redis.lpush('flagcolor', 'verydarkgrey       ')
self.redis.lpush('flagcolor', 'lightbrown         ')
self.redis.lpush('flagcolor', 'brown              ')
self.redis.lpush('flagcolor', 'darkbrown          ')
self.redis.lpush('flagcolor', 'purple             ')
self.redis.lpush('flagcolor', 'black              ')
self.redis.lpush('flagcolor', 'white              ')

# colors are taken from vexology standards
HSET flagcolor_description verylightred       {"name":"very light red",    "hex":"#ff6666",  "verb":"love",       "adverb":"lovingly"         }
HSET flagcolor_description lightred           {"name":"light red",         "hex":"#ff3333",  "verb":"cherish",    "adverb":"peacefully"       }
HSET flagcolor_description red                {"name":"red",               "hex":"#ff0000",  "verb":"expand",     "adverb":"gracefully"       }
HSET flagcolor_description darkred            {"name":"dark red",          "hex":"#cc0000",  "verb":"enforce",    "adverb":"defiantly"        }
HSET flagcolor_description verydarkred        {"name":"very dark red",     "hex":"#990000",  "verb":"march",      "adverb":"passionately"     }
HSET flagcolor_description verylightblue      {"name":"very light blue",   "hex":"#33ccff",  "verb":"protect",    "adverb":"faithfully"       }
HSET flagcolor_description lightblue          {"name":"light blue",        "hex":"#3399ff",  "verb":"inspire",    "adverb":"freely"           }
HSET flagcolor_description blue               {"name":"blue",              "hex":"#0000ff",  "verb":"enjoy",      "adverb":"openly"           }
HSET flagcolor_description darkblue           {"name":"dark blue",         "hex":"#0000cc",  "verb":"devote",     "adverb":"fully"            }
HSET flagcolor_description verydarkblue       {"name":"very dark blue",    "hex":"#000099",  "verb":"honor",      "adverb":"justly"           }
HSET flagcolor_description verylightgreen     {"name":"very light green",  "hex":"#00ff33",  "verb":"accelerate", "adverb":"tomorrow"         }
HSET flagcolor_description lightgreen         {"name":"light green",       "hex":"#00cc00",  "verb":"grow",       "adverb":"quickly"          }
HSET flagcolor_description green              {"name":"green",             "hex":"#009900",  "verb":"prosper",    "adverb":"always"           }
HSET flagcolor_description darkgreen          {"name":"dark green",        "hex":"#006600",  "verb":"hope",       "adverb":"appropriately"    }
HSET flagcolor_description verydarkgreen      {"name":"very dark green",   "hex":"#003300",  "verb":"cultivate",  "adverb":"brightly"         }
HSET flagcolor_description verylightyellow    {"name":"very light yellow", "hex":"#ffffcc",  "verb":"strengthen", "adverb":"joyfully"         }
HSET flagcolor_description lightyellow        {"name":"light yellow",      "hex":"#ffff99",  "verb":"surpass",    "adverb":"happily"          }
HSET flagcolor_description yellow             {"name":"yellow",            "hex":"#ffff00",  "verb":"entertain",  "adverb":"cheerfully"       }
HSET flagcolor_description darkyellow         {"name":"dark yellow",       "hex":"#ffcc00",  "verb":"relish",     "adverb":"gracefully"       }
HSET flagcolor_description lightorange        {"name":"light orange",      "hex":"#ff9900",  "verb":"distrust",   "adverb":"enthusiastically" }
HSET flagcolor_description orange             {"name":"orange",            "hex":"#ff6600",  "verb":"desire",     "adverb":"ambitiously"      }
HSET flagcolor_description gold               {"name":"gold",              "hex":"#ffcc33",  "verb":"purchase",   "adverb":"wisely"           }
HSET flagcolor_description lightgrey          {"name":"light grey",        "hex":"#cccccc",  "verb":"wonder",     "adverb":"cautiously"       }
HSET flagcolor_description grey               {"name":"grey",              "hex":"#999999",  "verb":"compromise", "adverb":"patiently"        }
HSET flagcolor_description darkgrey           {"name":"dark grey",         "hex":"#666666",  "verb":"conform",    "adverb":"impartially"      }
HSET flagcolor_description verydarkgrey       {"name":"very dark grey",    "hex":"#333333",  "verb":"control",    "adverb":"reliably"         }
HSET flagcolor_description lightbrown         {"name":"light brown",       "hex":"#996600",  "verb":"endure",     "adverb":"safely"           }
HSET flagcolor_description brown              {"name":"brown",             "hex":"#663300",  "verb":"withstand",  "adverb":"solidly"          }
HSET flagcolor_description darkbrown          {"name":"dark brown",        "hex":"#330000",  "verb":"balance",    "adverb":"naturally"        }
HSET flagcolor_description purple             {"name":"purple",            "hex":"#660099",  "verb":"rule",       "adverb":"majestically"     }
HSET flagcolor_description black              {"name":"black",             "hex":"#000000",  "verb":"destroy",    "adverb":"purposefully"     }
HSET flagcolor_description white              {"name":"white",             "hex":"#ffffff",  "verb":"perfect",    "adverb":"peacefully"       }

ZADD  flag_shape  50 {"name":"square",      "score":50    }
ZADD  flag_shape  60 {"name":"para",        "score":60    }
ZADD  flag_shape  70 {"name":"pennant",     "score":70    }
ZADD  flag_shape  80 {"name":"tri",         "score":80    }
ZADD  flag_shape  90 {"name":"swallow",     "score":90    }
ZADD  flag_shape 100 {"name":"tongued",     "score":100   }

self.redis.lpush('flag_shape_swallow_depth', '10')
self.redis.lpush('flag_shape_swallow_depth', '20')
self.redis.lpush('flag_shape_swallow_depth', '30')

self.redis.lpush('flag_shape_tongued_shape', 'square')
self.redis.lpush('flag_shape_tongued_shape', 'triangle')
self.redis.lpush('flag_shape_tongued_shape', 'sine')
self.redis.lpush('flag_shape_tongued_shape', 'scallop')
self.redis.lpush('flag_shape_tongued_count', '3')
self.redis.lpush('flag_shape_tongued_count', '5')
self.redis.lpush('flag_shape_tongued_count', '7')
self.redis.lpush('flag_shape_tongued_count', '9')
self.redis.lpush('flag_shape_tongued_count', '11')
self.redis.lpush('flag_shape_tongued_depth', '0.3')
self.redis.lpush('flag_shape_tongued_depth', '0.1')
self.redis.lpush('flag_shape_tongued_depth', '0.2')

ZADD  flag_ratio  10  { "name":"1", "score":10  }
ZADD  flag_ratio  20  { "name":"1.15", "score":20  }
ZADD  flag_ratio  30  { "name":"1.25", "score":30  }
ZADD  flag_ratio  40  { "name":"1.33", "score":40  }
ZADD  flag_ratio  50  { "name":"1.32", "score":50  }
ZADD  flag_ratio  55  { "name":"1.38", "score":55  }
ZADD  flag_ratio  60  { "name":"1.39", "score":60  }
ZADD  flag_ratio  65  { "name":"1.50", "score":65  }
ZADD  flag_ratio  70  { "name":"1.6", "score":70  }
ZADD  flag_ratio  75  { "name":"1.67", "score":75  }
ZADD  flag_ratio  80  { "name":"1.9", "score":80  }
ZADD  flag_ratio  90  { "name":"2.0", "score":90  }
ZADD  flag_ratio  100  { "name":"2.55", "score":100  }
    
ZADD  flag_division  20  { "name":"none", "score":20  }
ZADD  flag_division  40  { "name":"quads", "score":40  }
ZADD  flag_division  60  { "name":"diagquads", "score":60  }
ZADD  flag_division  80  { "name":"diagonal", "score":80  }
ZADD  flag_division  100  { "name":"stripes", "score":100  }

self.redis.lpush('flag_division_diagonal_direction', 'right-to-left')
self.redis.lpush('flag_division_diagonal_direction', 'left-to-right')

self.redis.lpush('flag_division_stripes_side', 'vertical')
self.redis.lpush('flag_division_stripes_side', 'horizontal')
self.redis.lpush('flag_division_stripes_count', '2')
self.redis.lpush('flag_division_stripes_count', '3')
self.redis.lpush('flag_division_stripes_count', '5')
self.redis.lpush('flag_division_stripes_count', '9')
self.redis.lpush('flag_division_stripes_count', '13')
self.redis.lpush('flag_division_stripes_colorcount', '2')
self.redis.lpush('flag_division_stripes_colorcount', '3')
   
ZADD  flag_overlay   5  { "name":"none", "score":5  }
ZADD  flag_overlay  10  { "name":"quaddiag", "score":10  }
ZADD  flag_overlay  20  { "name":"quad", "score":20  }
ZADD  flag_overlay  30  { "name":"stripe", "score":30  }
ZADD  flag_overlay  40  { "name":"slash", "score":40  }
#ZADD  flag_overlay  50  { "name":"asterisk", "score":50  }
ZADD  flag_overlay  60  { "name":"x", "score":60  }
#ZADD  flag_overlay  70  { "name":"jack", "score":70  }
ZADD  flag_overlay  80  { "name":"cross", "score":80  }
ZADD  flag_overlay  90  { "name":"diamond", "score":90  }
ZADD  flag_overlay  95  { "name":"circle", "score":95  }
ZADD  flag_overlay  100  { "name":"rays", "score":100  }

self.redis.lpush('flag_overlay_quaddiag_side', 'north')
self.redis.lpush('flag_overlay_quaddiag_side', 'south')
self.redis.lpush('flag_overlay_quaddiag_side', 'east')
self.redis.lpush('flag_overlay_quaddiag_side', 'west')
self.redis.lpush('flag_overlay_quad_side', 'ne')
self.redis.lpush('flag_overlay_quad_side', 'nw')
self.redis.lpush('flag_overlay_quad_side', 'se')
self.redis.lpush('flag_overlay_quad_side', 'sw')
self.redis.lpush('flag_overlay_stripe_side', 'vertical')
self.redis.lpush('flag_overlay_stripe_side', 'horizontal')
self.redis.lpush('flag_overlay_stripe_count', '2')
self.redis.lpush('flag_overlay_stripe_count', '3')
self.redis.lpush('flag_overlay_stripe_count', '5')
self.redis.lpush('flag_overlay_stripe_count', '9')
self.redis.lpush('flag_overlay_stripe_count', '13')
self.redis.lpush('flag_overlay_slash_direction', 'right-to-left')
self.redis.lpush('flag_overlay_slash_direction', 'left-to-right')
self.redis.lpush('flag_overlay_slash_width', '0.2')
self.redis.lpush('flag_overlay_slash_width', '0.15')
self.redis.lpush('flag_overlay_slash_width', '0.1')
self.redis.lpush('flag_overlay_slash_width', '0.05')
#LPUSH flag_overlay_asterisk_outline true
#LPUSH flag_overlay_asterisk_outline false
self.redis.lpush('flag_overlay_x_outline', 'true')
self.redis.lpush('flag_overlay_x_outline', 'false')
self.redis.lpush('flag_overlay_x_width', '0.2')
self.redis.lpush('flag_overlay_x_width', '0.15')
self.redis.lpush('flag_overlay_x_width', '0.1')
self.redis.lpush('flag_overlay_x_width', '0.05')
#LPUSH flag_overlay_jack_width 0.2
#LPUSH flag_overlay_jack_width 0.15
#LPUSH flag_overlay_jack_width 0.1
#LPUSH flag_overlay_jack_width 0.05
#LPUSH flag_overlay_jack_outline true
#LPUSH flag_overlay_jack_outline false
#LPUSH flag_overlay_jack_horlength 1
#LPUSH flag_overlay_jack_vertlength 1
#LPUSH flag_overlay_jack_horwidth 0.2
#LPUSH flag_overlay_jack_horwidth 0.15
#LPUSH flag_overlay_jack_horwidth 0.10
#LPUSH flag_overlay_jack_vertwidth 0.2
#LPUSH flag_overlay_jack_vertwidth 0.15
#LPUSH flag_overlay_jack_vertwidth 0.1
#LPUSH flag_overlay_jack_vertwidth 0.075
#LPUSH flag_overlay_jack_vertwidth 0.05
#LPUSH flag_overlay_jack_horpos 0.5
self.redis.lpush('flag_overlay_cross_vertlength', '1')
self.redis.lpush('flag_overlay_cross_vertlength', '0.8')
self.redis.lpush('flag_overlay_cross_vertwidth', '0.2')
self.redis.lpush('flag_overlay_cross_vertwidth', '0.15')
self.redis.lpush('flag_overlay_cross_vertwidth', '0.1')
self.redis.lpush('flag_overlay_cross_vertwidth', '0.075')
self.redis.lpush('flag_overlay_cross_vertwidth', '0.05')
self.redis.lpush('flag_overlay_cross_horwidth', '0.3')
self.redis.lpush('flag_overlay_cross_horwidth', '0.2')
self.redis.lpush('flag_overlay_cross_horlength', '0.3')
self.redis.lpush('flag_overlay_cross_horlength', '0.5')
self.redis.lpush('flag_overlay_cross_horlength', '0.8')
self.redis.lpush('flag_overlay_cross_horlength', '0.9')
self.redis.lpush('flag_overlay_cross_horlength', '1')
self.redis.lpush('flag_overlay_cross_horpos', '0.33')
self.redis.lpush('flag_overlay_cross_horpos', '0.5')
self.redis.lpush('flag_overlay_diamond_outline', 'true')
self.redis.lpush('flag_overlay_diamond_outline', 'false')
self.redis.lpush('flag_overlay_circle_outlinewidth', '1')
self.redis.lpush('flag_overlay_circle_outlinewidth', '2')
self.redis.lpush('flag_overlay_circle_outlinewidth', '5')
self.redis.lpush('flag_overlay_circle_outlinewidth', '10')
self.redis.lpush('flag_overlay_circle_outlinewidth', '20')
self.redis.lpush('flag_overlay_circle_outlinewidth', '30')
self.redis.lpush('flag_overlay_circle_outline', 'true')
self.redis.lpush('flag_overlay_circle_outline', 'false')
self.redis.lpush('flag_overlay_circle_radiusdirection', 'horizontal')
self.redis.lpush('flag_overlay_circle_radiusdirection', 'vertical')
self.redis.lpush('flag_overlay_circle_x', '-1')
self.redis.lpush('flag_overlay_circle_x', '-.5')
self.redis.lpush('flag_overlay_circle_x', '0')
self.redis.lpush('flag_overlay_circle_x', '.25')
self.redis.lpush('flag_overlay_circle_x', '.333')
self.redis.lpush('flag_overlay_circle_x', '.5')
self.redis.lpush('flag_overlay_circle_x', '.666')
self.redis.lpush('flag_overlay_circle_x', '.75')
self.redis.lpush('flag_overlay_circle_x', '1')
self.redis.lpush('flag_overlay_circle_x', '1.5')
self.redis.lpush('flag_overlay_circle_x', '2')
self.redis.lpush('flag_overlay_circle_y', '-1')
self.redis.lpush('flag_overlay_circle_y', '0')
self.redis.lpush('flag_overlay_circle_y', '.25')
self.redis.lpush('flag_overlay_circle_y', '.5')
self.redis.lpush('flag_overlay_circle_y', '.75')
self.redis.lpush('flag_overlay_circle_y', '1')
self.redis.lpush('flag_overlay_circle_y', '2')
self.redis.lpush('flag_overlay_circle_radius', '.25')
self.redis.lpush('flag_overlay_circle_radius', '.333')
self.redis.lpush('flag_overlay_circle_radius', '.5')
self.redis.lpush('flag_overlay_circle_radius', '.666')
self.redis.lpush('flag_overlay_circle_radius', '.75')
self.redis.lpush('flag_overlay_circle_radius', '1')
self.redis.lpush('flag_overlay_circle_radius', '1.5')
self.redis.lpush('flag_overlay_circle_radius', '2')
self.redis.lpush('flag_overlay_rays_offset', '0')
self.redis.lpush('flag_overlay_rays_offset', '.05')
self.redis.lpush('flag_overlay_rays_offset', '.15')
self.redis.lpush('flag_overlay_rays_offset', '.25')
self.redis.lpush('flag_overlay_rays_offset', '.33')
self.redis.lpush('flag_overlay_rays_count', '3')
self.redis.lpush('flag_overlay_rays_count', '4')
self.redis.lpush('flag_overlay_rays_count', '5')
self.redis.lpush('flag_overlay_rays_count', '6')
self.redis.lpush('flag_overlay_rays_count', '7')
self.redis.lpush('flag_overlay_rays_count', '8')
self.redis.lpush('flag_overlay_rays_count', '9')
self.redis.lpush('flag_overlay_rays_count', '10')
self.redis.lpush('flag_overlay_rays_count', '12')
self.redis.lpush('flag_overlay_rays_count', '15')
self.redis.lpush('flag_overlay_rays_count', '20')
self.redis.lpush('flag_overlay_rays_x', '-1')
self.redis.lpush('flag_overlay_rays_x', '-.5')
self.redis.lpush('flag_overlay_rays_x', '0')
self.redis.lpush('flag_overlay_rays_x', '.25')
self.redis.lpush('flag_overlay_rays_x', '.333')
self.redis.lpush('flag_overlay_rays_x', '.5')
self.redis.lpush('flag_overlay_rays_x', '.666')
self.redis.lpush('flag_overlay_rays_x', '.75')
self.redis.lpush('flag_overlay_rays_x', '1')
self.redis.lpush('flag_overlay_rays_x', '1.5')
self.redis.lpush('flag_overlay_rays_x', '2')
self.redis.lpush('flag_overlay_rays_y', '-1')
self.redis.lpush('flag_overlay_rays_y', '0')
self.redis.lpush('flag_overlay_rays_y', '.25')
self.redis.lpush('flag_overlay_rays_y', '.5')
self.redis.lpush('flag_overlay_rays_y', '.75')
self.redis.lpush('flag_overlay_rays_y', '1')
self.redis.lpush('flag_overlay_rays_y', '2')
                
ZADD  flag_symbol  25 { "name":"none", "score":25  }
ZADD  flag_symbol  50 { "name":"circle", "score":50  }
ZADD  flag_symbol  75 { "name":"star", "score":75  }
ZADD  flag_symbol 100 { "name":"letter", "score":100  }
self.redis.lpush('flag_symbol_circle_outline', 'true')
self.redis.lpush('flag_symbol_circle_outline', 'false')
self.redis.lpush('flag_symbol_circle_radiusdirection', 'horizontal')
self.redis.lpush('flag_symbol_circle_radiusdirection', 'vertical')
self.redis.lpush('flag_symbol_circle_x', '.25')
self.redis.lpush('flag_symbol_circle_x', '.5')
self.redis.lpush('flag_symbol_circle_y', '.25')
self.redis.lpush('flag_symbol_circle_y', '.5')
self.redis.lpush('flag_symbol_circle_radius', '.10')
self.redis.lpush('flag_symbol_circle_radius', '.15')
self.redis.lpush('flag_symbol_circle_radius', '.20')
self.redis.lpush('flag_symbol_circle_radius', '.25')
               
self.redis.lpush('flag_symbol_star_points', '4')
self.redis.lpush('flag_symbol_star_points', '5')
self.redis.lpush('flag_symbol_star_points', '6')
self.redis.lpush('flag_symbol_star_points', '8')
self.redis.lpush('flag_symbol_star_points', '12')
self.redis.lpush('flag_symbol_star_points', '20')
self.redis.lpush('flag_symbol_star_inset', '.25')
self.redis.lpush('flag_symbol_star_inset', '.33')
self.redis.lpush('flag_symbol_star_inset', '.5')
self.redis.lpush('flag_symbol_star_x', '.25')
self.redis.lpush('flag_symbol_star_x', '.5')
self.redis.lpush('flag_symbol_star_y', '.25')
self.redis.lpush('flag_symbol_star_y', '.5')
        
self.redis.lpush('flag_symbol_letter_fontfamily', 'Arial Black')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Comic Sans MS Bold')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Courier New Bold')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Courier New Bold Italic')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Impact')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Lucida Console')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Trebuchet MS')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Trebuchet MS Bold')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Trebuchet MS Italic')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Trebuchet MS Bold Italic')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Verdana')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Verdana Bold')
self.redis.lpush('flag_symbol_letter_fontfamily', 'Verdana Bold Italic')
self.redis.lpush('flag_symbol_letter_fontfamily', 'sans serif')
               
self.redis.lpush('flag_symbol_letter_size', '.40')
self.redis.lpush('flag_symbol_letter_size', '.30')
self.redis.lpush('flag_symbol_letter_size', '.25')
               
self.redis.lpush('flag_symbol_letter_x', '.25')
self.redis.lpush('flag_symbol_letter_x', '.5')
               
self.redis.lpush('flag_symbol_letter_y', '.25')
self.redis.lpush('flag_symbol_letter_y', '.5')
               
ZADD  flag_border  50  { "name":"none", "score":50  }       
ZADD  flag_border  100  { "name":"solid", "score":100  }
self.redis.lpush('flag_border_solid_size', '.08')
self.redis.lpush('flag_border_solid_size', '.05')
self.redis.lpush('flag_border_solid_size', '.01')
                
            
        
    




