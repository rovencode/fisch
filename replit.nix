{ pkgs }: {
  deps = [
    pkgs.cairo
    pkgs.pkg-config
    pkgs.glib
    pkgs.gobject-introspection
  ];
}