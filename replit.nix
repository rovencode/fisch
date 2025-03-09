{ pkgs }: {
  deps = [
    pkgs.portmidi
    pkgs.libpng
    pkgs.libjpeg
    pkgs.freetype
    pkgs.fontconfig
    pkgs.SDL2_ttf
    pkgs.SDL2_mixer
    pkgs.SDL2_image
    pkgs.SDL2
    pkgs.cairo
    pkgs.pkg-config
    pkgs.glib
    pkgs.gobject-introspection
  ];
}