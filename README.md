# msheiny.gnomeshell

[![CircleCI](https://circleci.com/gh/msheiny/ansible-role-gnomeshell.svg?style=svg)](https://circleci.com/gh/msheiny/ansible-role-gnomeshell)

A role to handle two gnome-shell tasks:
* installing gnome-shell tweak extensions
* manipulate gnome dconf settings with a nicely organized dictionary

## Dependencies

* Requires ansible 2.4+ for the `dconf` module
* Utilizes external submodule for the `gnome_shell_extension` module

Make sure you run `git submodule update --init` to bring in the mentioned
submodule above.


## Default Vars

```
---
gnomeshell_dconf_reqs:
  - python2-psutil

# Here is an example of feeding in dconf settings. The underlying
# module is a little weird and below is an example of quoting formats.
# Notice strings are double quoted - "'string'" but booleans and other
# types only need a single quote
#
# gnomeshell_dconf_settings:
#   /org/gnome/terminal/legacy:
#     mnemonics-enabled: "true"
#     menu-accelerator-enabled: "true"
#     schema-version: "uint32 3"
#     default-show-menubar: "false"
#     theme-variant: "'dark'"
gnomeshell_dconf_settings: {}

gnomeshell_user: "{{ ansible_user_id }}"
gnomeshell_extension_path: ".local/share/gnome-shell/extensions/"

# Set shell extensions, required to at least put the numberic id.
# See the following guide for reference on grabbing that info:
# http://bernaerts.dyndns.org/linux/76-gnome/345-gnome-shell-install-remove-extension-command-line-script
#
# gnomeshell_extension_list:
#  - num: 442
#    gnome_ver: 3.22
gnomeshell_extension_list: []
```
