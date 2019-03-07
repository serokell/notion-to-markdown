_Given a [Notion.so](https://www.notion.so/) URL fetches it as zipped markdown._


Use
====

First of all you need to obtain a token. Currently the only known way of doing
this is to grab it from your browser’s cookies (it is called `token_v2` there).

Raw Python
-----------

* Install Python 3 and `requests`
* Set the `NOTION_TOKEN` environment variable to your token
* Execute `./notion.py "<url>"`

Nix
-----

* `nix-build default.nix --argstr token "<token>" --argstr url "<url>" -A notionToPdf`

Keep in mind that the derivation is impure and non-deterministic, so, um,
it is not entirely clear how to force a rebuild of the same URL...
