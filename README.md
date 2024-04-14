![image](https://github.com/masukuapi/masuku-docs/assets/55801439/d2db1808-2394-45ba-abe9-bbd3d1281788)


# Masuku - Face Detection ML Model

Masuku is a API service that utilizes a custom trained YOLO V5 object detection model to detect human faces and determine the presence of face coverings. It provides an API which can be used for web or mobile applications. This application is intended to assist in environments where face coverings are required for safety and compliance purposes.

The application works by capturing images in real-time using the device's camera. These images are then analyzed using the YOLO V5 object detection model to detect human faces and identify whether the face is covered, partially covered, or not covered. The application also logs detection events with timestamps and generates reports summarizing the detection events.

A Rust version of this project is currently in development. You can follow its progress [here](<https://github.com/masukuapi/masuku-rs>).

## Features

- Real-time face detection
- Identification of face coverings
- User-friendly interface for non-technical users
- Reporting and logging of detection events

## Prerequisites

- Python 3.11+
- Node.js
- Docker

## Try it out yourself

1. Clone the repository:

    ```sh
    git clone https://github.com/masukuapi/masuku-docs/
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the server:

    ```sh
    gunicorn -b 0.0.0.0:8000 main:app
    ```

Alternatively, you can run the server using the Flask development server:

```sh
python main.py
```

You can also pull the Docker image from Docker Hub and run it:

```sh
docker pull glitchyi/masuku:latest
docker run -p 8000:8000 glitchyi/masuku:latest
```

## Usage

Navigate to `http://localhost:8000` on your browser. You should see a form where you can upload an image file. After uploading, the server will process the image.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## References

- YOLO V5 Official Documentation: <https://github.com/ultralytics/yolov5>
