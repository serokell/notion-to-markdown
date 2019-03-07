{ pkgs ? import <nixpkgs> {} }:

let
  inherit (pkgs.lib) concatStringsSep init last splitString;

  notionToPdf = {token, url}:
    pkgs.stdenv.mkDerivation rec {
      fname = last (splitString "/" url);
      title = concatStringsSep "-" (init (splitString "-" fname));
      name = "${title}.md.zip";

      nativeBuildInputs = with pkgs; [
        python3
        python3Packages.requests
        curl
        cacert
      ];

      NOTION_TOKEN = token;
      buildCommand = ''
        zipurl=$(${./notion.py} "${url}")
        curl "$zipurl" > "$out"
      '';
    };
in

{ inherit notionToPdf; }
