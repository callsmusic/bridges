export $(cat .env | xargs)

ffmpeg \
  -loop \
  1 \
  -i \
  "$BACKGROUND" \
  -c:v \
  libx264 \
  -preset \
  veryfast \
  -b:v \
  1984k \
  -maxrate 1984k \
  -bufsize 3968k \
  -vf \
  "format=yuv420p" \
  -g \
  60 \
  -c:a \
  aac \
  -b:a \
  128k \
  -ar \
  44100 \
  -f \
  flv \
  "$STREAM_URL"
