
import sys

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    OptionProperty,
    ListProperty,
    ObjectProperty,
)
from kivy.metrics import dp
from kivy.metrics import sp

from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDIcon

Builder.load_string(
    """
#:import images_path kivymd.images_path


<NumInput>

    canvas.before:
        Clear

        # Disabled line.
        Color:
            rgba: self.line_color_normal if root.mode == "line" else (0, 0, 0, 0)
        Line:
            points: self.x, self.y + dp(16), self.x + self.width, self.y + dp(16)
            width: 1
            dash_length: dp(3)
            dash_offset: 2 if self.disabled else 0

        # Active line.
        Color:
            rgba: self._current_line_color if root.mode in ("line", "fill") and root.active_line else (0, 0, 0, 0)
        Rectangle:
            size: self._line_width, dp(2)
            pos: self.center_x - (self._line_width / 2), self.y + (dp(16) if root.mode != "fill" else 0)

        # Helper text.
        Color:
            rgba: self._current_error_color
        Rectangle:
            texture: self._msg_lbl.texture
            size:
                self._msg_lbl.texture_size[0] - (dp(3) if root.mode in ("fill", "rectangle") else 0), \
                self._msg_lbl.texture_size[1] - (dp(3) if root.mode in ("fill", "rectangle") else 0)
            pos: self.x + (dp(8) if root.mode == "fill" else 0), self.y + (dp(3) if root.mode in ("fill", "rectangle") else 0)

        # Texture of right Icon.
        Color:
            rgba: self.icon_right_color
        Rectangle:
            texture: self._lbl_icon_right.texture
            size: self._lbl_icon_right.texture_size if self.icon_right else (0, 0)
            pos:
                (self.width + self.x) - (self._lbl_icon_right.texture_size[1]) - dp(8), \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2 + (dp(8) if root.mode != "fill" else 0) \
                if root.mode != "rectangle" else \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2 - dp(4)

        Color:
            rgba: self._current_right_lbl_color
        Rectangle:
            texture: self._right_msg_lbl.texture
            size: self._right_msg_lbl.texture_size
            pos: self.width-self._right_msg_lbl.texture_size[0] + dp(45), self.y

        Color:
            rgba:
                (self._current_line_color if self.focus and not \
                self._cursor_blink else (0, 0, 0, 0))
        Rectangle:
            pos: (int(x) for x in self.cursor_pos)
            size: 1, -self.line_height

        # Hint text.
        Color:
            rgba: self._current_hint_text_color if not self.current_hint_text_color else self.current_hint_text_color
        Rectangle:
            texture: self._hint_lbl.texture
            size: self._hint_lbl.texture_size
            pos: self.x + (dp(8) if root.mode == "fill" else 0), self.y + self.height - self._hint_y

        Color:
            rgba:
                self.disabled_foreground_color if self.disabled else\
                (self.hint_text_color if not self.text and not\
                self.focus else self.foreground_color)

        # "rectangle" mode
        Color:
            rgba: self._current_line_color
        Line:
            width: dp(1) if root.mode == "rectangle" else dp(0.00001)
            points:
                (
                self.x + root._line_blank_space_right_hint_text, self.top - self._hint_lbl.texture_size[1] // 2,
                self.right + dp(12), self.top - self._hint_lbl.texture_size[1] // 2,
                self.right + dp(12), self.y,
                self.x - dp(12), self.y,
                self.x - dp(12), self.top - self._hint_lbl.texture_size[1] // 2,
                self.x + root._line_blank_space_left_hint_text, self.top - self._hint_lbl.texture_size[1] // 2
                )

    # "fill" mode.
    canvas.after:
        Color:
            rgba: root.fill_color if root.mode == "fill" else (0, 0, 0, 0)
        RoundedRectangle:
            pos: self.x, self.y
            size: self.width, self.height + dp(8)
            radius: [10, 10, 0, 0, 0]

    font_name: "Roboto" if not root.font_name else root.font_name
    foreground_color: app.theme_cls.text_color
    font_size: "16sp"
    bold: False
    padding:
        0 if root.mode != "fill" else "8dp", \
        "16dp" if root.mode != "fill" else "24dp", \
        0 if root.mode != "fill" and not root.icon_right else ("14dp" if not root.icon_right else self._lbl_icon_right.texture_size[1] + dp(20)), \
        "16dp" if root.mode == "fill" else "10dp"
    multiline: False
    size_hint_y: None
    height: self.minimum_height + (dp(8) if root.mode != "fill" else 0)


<TextfieldLabel>
    size_hint_x: None
    width: self.texture_size[0]
    shorten: True
    shorten_from: "right"

"""
)


class FixedHintTextInput(TextInput):
    hint_text = StringProperty("")

    def on__hint_text(self, instance, value):
        pass

    def _refresh_hint_text(self):
        pass


class TextfieldLabel(ThemableBehavior, Label):
    field = ObjectProperty()
    font_style = OptionProperty("Body1", options=theme_font_styles)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = sp(self.theme_cls.font_styles[self.font_style][1])


class NumInput(ThemableBehavior, FixedHintTextInput):
    min_value = NumericProperty()
    max_value = NumericProperty()


    helper_text = StringProperty("This field is required")
    """
    Text for ``helper_text`` mode.

    :attr:`helper_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'This field is required'`.
    """

    helper_text_mode = OptionProperty(
        "none", options=["none", "on_error", "persistent", "on_focus"]
    )
    """
    Helper text mode. Available options are: `'on_error'`, `'persistent'`,
    `'on_focus'`.

    :attr:`helper_text_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'none'`.
    """

    max_text_length = NumericProperty(None)
    """
    Maximum allowed value of characters in a text field.

    :attr:`max_text_length` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    required = BooleanProperty(False)
    """
    Required text. If True then the text field requires text.

    :attr:`required` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    color_mode = OptionProperty(
        "primary", options=["primary", "accent", "custom"]
    )
    """
    Color text mode. Available options are: `'primary'`, `'accent'`,
    `'custom'`.

    :attr:`color_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'primary'`.
    """

    mode = OptionProperty("line", options=["rectangle", "fill"])
    """
    Text field mode. Available options are: `'line'`, `'rectangle'`, `'fill'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    line_color_normal = ListProperty()
    """
    Line color normal in ``rgba`` format.

    :attr:`line_color_normal` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    line_color_focus = ListProperty()
    """
    Line color focus in ``rgba`` format.

    :attr:`line_color_focus` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    error_color = ListProperty()
    """
    Error color in ``rgba`` format for ``required = True``.

    :attr:`error_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    fill_color = ListProperty([0, 0, 0, 0])
    """
    The background color of the fill in rgba format when the ``mode`` parameter 
    is "fill".

    :attr:`fill_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    active_line = BooleanProperty(True)
    """
    Show active line or not.

    :attr:`active_line` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    error = BooleanProperty(False)
    """
    If True, then the text field goes into ``error`` mode.

    :attr:`error` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    current_hint_text_color = ListProperty()
    """
    ``hint_text`` text color.

    :attr:`current_hint_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    icon_right = StringProperty()
    """Right icon.

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right_color = ListProperty([0, 0, 0, 1])
    """Color of right icon in ``rgba`` format.

    :attr:`icon_right_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    _text_len_error = BooleanProperty(False)
    _hint_lbl_font_size = NumericProperty("16sp")
    _line_blank_space_right_hint_text = NumericProperty(0)
    _line_blank_space_left_hint_text = NumericProperty(0)
    _hint_y = NumericProperty("38dp")
    _line_width = NumericProperty(0)
    _current_line_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_error_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_hint_text_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_right_lbl_color = ListProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self._msg_lbl = TextfieldLabel(
            font_style="Caption",
            halign="left",
            valign="middle",
            text=self.helper_text,
            field=self,
        )
        self._right_msg_lbl = TextfieldLabel(
            font_style="Caption",
            halign="right",
            valign="middle",
            text="",
            field=self,
        )
        self._hint_lbl = TextfieldLabel(
            font_style="Subtitle1", halign="left", valign="middle", field=self
        )
        self._lbl_icon_right = MDIcon(theme_text_color="Custom")
        super().__init__(**kwargs)
        self.line_color_normal = self.theme_cls.divider_color
        self.line_color_focus = self.theme_cls.primary_color
        self.error_color = self.theme_cls.error_color

        self._current_hint_text_color = self.theme_cls.disabled_hint_text_color
        self._current_line_color = self.theme_cls.primary_color

        self.bind(
            helper_text=self._set_msg,
            hint_text=self._set_hint,
            _hint_lbl_font_size=self._hint_lbl.setter("font_size"),
            helper_text_mode=self._set_message_mode,
            max_text_length=self._set_max_text_length,
            text=self.on_text,
        )
        self.theme_cls.bind(
            primary_color=self._update_primary_color,
            theme_style=self._update_theme_style,
            accent_color=self._update_accent_color,
        )
        self.has_had_text = False

    def _update_colors(self, color):
        self.line_color_focus = color
        if not self.error and not self._text_len_error:
            self._current_line_color = color
            if self.focus:
                self._current_line_color = color

    def _update_accent_color(self, *args):
        if self.color_mode == "accent":
            self._update_colors(self.theme_cls.accent_color)

    def _update_primary_color(self, *args):
        if self.color_mode == "primary":
            self._update_colors(self.theme_cls.primary_color)

    def _update_theme_style(self, *args):
        self.line_color_normal = self.theme_cls.divider_color
        if not any([self.error, self._text_len_error]):
            if not self.focus:
                self._current_hint_text_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                self._current_right_lbl_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                if self.helper_text_mode == "persistent":
                    self._current_error_color = (
                        self.theme_cls.disabled_hint_text_color
                    )

    def on_icon_right(self, instance, value):
        self._lbl_icon_right.icon = value

    def on_icon_right_color(self, instance, value):
        self._lbl_icon_right.text_color = value

    def on_width(self, instance, width):
        if (
            any([self.focus, self.error, self._text_len_error])
            and instance is not None
        ):
            self._line_width = width
        self._msg_lbl.width = self.width
        self._right_msg_lbl.width = self.width

    def on_focus(self, *args):
        disabled_hint_text_color = self.theme_cls.disabled_hint_text_color
        Animation.cancel_all(
            self, "_line_width", "_hint_y", "_hint_lbl_font_size"
        )
        if self.max_text_length is None:
            max_text_length = sys.maxsize
        else:
            max_text_length = self.max_text_length
        if len(self.text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True
        if self.error or all(
            [
                self.max_text_length is not None
                and len(self.text) > self.max_text_length
            ]
        ):
            has_error = True
        else:
            if all([self.required, len(self.text) == 0, self.has_had_text]):
                has_error = True
            else:
                has_error = False

        if self.focus:
            if not self._line_blank_space_right_hint_text:
                self._line_blank_space_right_hint_text = self._hint_lbl.texture_size[
                    0
                ] - dp(
                    25
                )
            _fill_color = self.fill_color
            _fill_color[3] = self.fill_color[3] - 0.1
            Animation(
                _line_blank_space_right_hint_text=self._line_blank_space_right_hint_text,
                _line_blank_space_left_hint_text=self._hint_lbl.x - dp(5),
                _current_hint_text_color=self.line_color_focus,
                fill_color=_fill_color,
                duration=0.2,
                t="out_quad",
            ).start(self)
            self.has_had_text = True
            Animation.cancel_all(
                self, "_line_width", "_hint_y", "_hint_lbl_font_size"
            )
            if not self.text:
                Animation(
                    _hint_y=dp(14),
                    _hint_lbl_font_size=sp(12),
                    duration=0.2,
                    t="out_quad",
                ).start(self)
            Animation(_line_width=self.width, duration=0.2, t="out_quad").start(
                self
            )
            if has_error:
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.error_color,
                    _current_right_lbl_color=self.error_color,
                    _current_line_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                elif (
                    self.helper_text_mode == "on_error"
                    and not self.error
                    and not self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
            else:
                Animation(
                    duration=0.2,
                    _current_right_lbl_color=disabled_hint_text_color,
                ).start(self)
                Animation(duration=0.2, color=self.line_color_focus).start(
                    self._hint_lbl
                )
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                if self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
        else:
            _fill_color = self.fill_color
            _fill_color[3] = self.fill_color[3] + 0.1
            Animation(
                fill_color=_fill_color, duration=0.2, t="out_quad",
            ).start(self)
            if not self.text:
                Animation(
                    _hint_y=dp(38),
                    _hint_lbl_font_size=sp(16),
                    duration=0.2,
                    t="out_quad",
                ).start(self)
                Animation(
                    _line_blank_space_right_hint_text=0,
                    _line_blank_space_left_hint_text=0,
                    duration=0.2,
                    t="out_quad",
                ).start(self)
            if has_error:
                Animation(
                    duration=0.2,
                    _current_line_color=self.error_color,
                    _current_hint_text_color=self.error_color,
                    _current_right_lbl_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                elif (
                    self.helper_text_mode == "on_error"
                    and not self.error
                    and not self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
            else:
                Animation(duration=0.2, color=(1, 1, 1, 1)).start(
                    self._hint_lbl
                )
                Animation(
                    duration=0.2,
                    _current_line_color=self.line_color_focus,
                    _current_hint_text_color=disabled_hint_text_color,
                    _current_right_lbl_color=(0, 0, 0, 0),
                ).start(self)
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                Animation(_line_width=0, duration=0.2, t="out_quad").start(self)

    def on_text(self, instance, text):
        if len(text) > 0:
            self.has_had_text = True
        if self.max_text_length is not None:
            self._right_msg_lbl.text = f"{len(text)}/{self.max_text_length}"
            max_text_length = self.max_text_length
        else:
            max_text_length = sys.maxsize
        if len(text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True
        else:
            self._text_len_error = False
        if self.error or self._text_len_error:
            if self.focus:
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.error_color,
                    _current_line_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                if self._text_len_error:
                    Animation(
                        duration=0.2, _current_right_lbl_color=self.error_color
                    ).start(self)
        else:
            if self.focus:
                disabled_hint_text_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                Animation(
                    duration=0.2,
                    _current_right_lbl_color=disabled_hint_text_color,
                ).start(self)
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.line_color_focus,
                    _current_line_color=self.line_color_focus,
                ).start(self)
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
        if len(self.text) != 0 and not self.focus:
            self._hint_y = dp(14)
            self._hint_lbl_font_size = sp(12)

    def on_text_validate(self):
        self.has_had_text = True
        if self.max_text_length is None:
            max_text_length = sys.maxsize
        else:
            max_text_length = self.max_text_length
        if len(self.text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True

    def _set_hint(self, instance, text):
        self._hint_lbl.text = text

    def _set_msg(self, instance, text):
        self._msg_lbl.text = text
        self.helper_text = text

    def _set_message_mode(self, instance, text):
        self.helper_text_mode = text
        if self.helper_text_mode == "persistent":
            disabled_hint_text_color = self.theme_cls.disabled_hint_text_color
            Animation(
                duration=0.1, _current_error_color=disabled_hint_text_color
            ).start(self)

    def _set_max_text_length(self, instance, length):
        self.max_text_length = length
        self._right_msg_lbl.text = f"{len(self.text)}/{length}"

    def on_color_mode(self, instance, mode):
        if mode == "primary":
            self._update_primary_color()
        elif mode == "accent":
            self._update_accent_color()
        elif mode == "custom":
            self._update_colors(self.line_color_focus)

    def on_line_color_focus(self, *args):
        if self.color_mode == "custom":
            self._update_colors(self.line_color_focus)


    def insert_text(self, string, from_undo=False):
        new_text = self.text + string
        if new_text != "":
            if self.min_value <= float(new_text) <= self.max_value:
                FixedHintTextInput.insert_text(self, string, from_undo=from_undo)

