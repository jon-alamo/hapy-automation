import hapy.models as models


class Light(models.Domain):

    def turn_on(self, transition: str = None, rgb_color: str = None, rgbw_color: str = None, rgbww_color: str = None, color_name: str = None, hs_color: str = None, xy_color: str = None, color_temp: str = None, kelvin: str = None, brightness: str = None, brightness_pct: str = None, brightness_step: str = None, brightness_step_pct: str = None, white: str = None, profile: str = None, flash: str = None, effect: str = None):
        """ Turn on one or more lights and adjust properties of the light, even when they are turned on already.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example:

        :rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
            {'color_rgb': None}
            Example:

        :rgbw_color: The color in RGBW format. A list of four integers between 0 and 255 representing the values of red, green, blue, and white.
            {'object': None}
            Example: [255, 100, 100, 50]

        :rgbww_color: The color in RGBWW format. A list of five integers between 0 and 255 representing the values of red, green, blue, cold white, and warm white.
            {'object': None}
            Example: [255, 100, 100, 50, 70]

        :color_name: A human-readable color name.
            {'select': {'translation_key': 'color_name', 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}
            Example:

        :hs_color: Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.
            {'object': None}
            Example: [300, 70]

        :xy_color: Color in XY-format. A list of two decimal numbers between 0 and 1.
            {'object': None}
            Example: [0.52, 0.43]

        :color_temp: Color temperature in mireds.
            {'color_temp': {'min_mireds': 153, 'max_mireds': 500}}
            Example:

        :kelvin: Color temperature in Kelvin.
            {'number': {'min': 2000, 'max': 6500, 'step': 100, 'unit_of_measurement': 'K'}}
            Example:

        :brightness: Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.
            {'number': {'min': 0, 'max': 255}}
            Example:

        :brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example:

        :brightness_step: Change brightness by an amount.
            {'number': {'min': -225, 'max': 255}}
            Example:

        :brightness_step_pct: Change brightness by a percentage.
            {'number': {'min': -100, 'max': 100, 'unit_of_measurement': '%'}}
            Example:

        :white: Set the light to white mode.
            {'constant': {'value': True, 'label': 'Enabled'}}
            Example:

        :profile: Name of a light profile to use.
            {'text': None}
            Example: relax

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example:

        :effect: Light effect.
            {'text': None}
            Example:
        """

    def turn_off(self, transition: str = None, flash: str = None):
        """ Turn off one or more lights.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example:

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example:
        """

    def toggle(self, transition: str = None, rgb_color: str = None, color_name: str = None, hs_color: str = None, xy_color: str = None, color_temp: str = None, kelvin: str = None, brightness: str = None, brightness_pct: str = None, white: str = None, profile: str = None, flash: str = None, effect: str = None):
        """ Toggles one or more lights, from on to off, or, off to on, based on their current state.

        :transition: Duration it takes to get to next state.
            {'number': {'min': 0, 'max': 300, 'unit_of_measurement': 'seconds'}}
            Example:

        :rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
            {'color_rgb': None}
            Example: [255, 100, 100]

        :color_name: A human-readable color name.
            {'select': {'translation_key': 'color_name', 'options': ['homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']}}
            Example:

        :hs_color: Color in hue/sat format. A list of two integers. Hue is 0-360 and Sat is 0-100.
            {'object': None}
            Example: [300, 70]

        :xy_color: Color in XY-format. A list of two decimal numbers between 0 and 1.
            {'object': None}
            Example: [0.52, 0.43]

        :color_temp: Color temperature in mireds.
            {'color_temp': None}
            Example:

        :kelvin: Color temperature in Kelvin.
            {'number': {'min': 2000, 'max': 6500, 'step': 100, 'unit_of_measurement': 'K'}}
            Example:

        :brightness: Number indicating brightness, where 0 turns the light off, 1 is the minimum brightness, and 255 is the maximum brightness.
            {'number': {'min': 0, 'max': 255}}
            Example:

        :brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
            {'number': {'min': 0, 'max': 100, 'unit_of_measurement': '%'}}
            Example:

        :white: Set the light to white mode.
            {'constant': {'value': True, 'label': 'Enabled'}}
            Example:

        :profile: Name of a light profile to use.
            {'text': None}
            Example: relax

        :flash: Tell light to flash, can be either value short or long.
            {'select': {'options': [{'label': 'Long', 'value': 'long'}, {'label': 'Short', 'value': 'short'}]}}
            Example:

        :effect: Light effect.
            {'text': None}
            Example:
        """


class Button(models.Domain):

    def press(self):
        """ Press the button entity.
        """
