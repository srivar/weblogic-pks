Files to build a base Java8 image, required when building other WLS images.

1. Download JRE 8 installer from Oracle http://www.oracle.com/technetwork/java/javase/downloads/server-jre8-downloads-2133154.html

2. Place the JRE archive (example "server-jre-8u144-linux-x64.tar.gz") in same directory as the Dockerfile

3. Run the command "docker build -t java8 ."
