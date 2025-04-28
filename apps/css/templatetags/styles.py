from django import template

register = template.Library()


@register.simple_tag
def sub_nav_button_link():
    return "bg-gradient-to-r from-green-500/20 via-gray-800 to-green-500/20 p-4 rounded-xl shadow-2xl hover:bg-green-700/20 border border-green-400 hover:border-green-500 transition transform hover:scale-105"
