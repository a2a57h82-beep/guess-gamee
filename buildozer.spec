name: Build APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Install Android SDK
        uses: android-actions/setup-android@v3

      - name: Accept Android SDK Licenses
        run: |
          yes | sdkmanager --licenses

      - name: Install Android SDK Packages
        run: |
          sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install "buildozer @ git+https://github.com/kivy/buildozer.git"
          pip install Cython==0.29.37

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: APK
          path: bin/*.apk
        
