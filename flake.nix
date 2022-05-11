{
  outputs = { nixpkgs, ... }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in rec {
    devShell.${system} = (pkgs.mkShell {
      packages = with pkgs; [
        (python2.withPackages (pkgs: with pkgs; [
        ]))
        (python3.withPackages (pkgs: with pkgs; [
          pandas
          matplotlib
        ]))
      ];
    });
  };
}
