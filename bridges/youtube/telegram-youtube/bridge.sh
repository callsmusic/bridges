export $(cat .env | xargs)

ffmpeg \
  -loop \
  1 \
  -i \
  "$BACKGROUND" \
  -f \
  s16le \
  -ac \
  2 \
  -ar \
  48K \
  -i \
  "$OUTPUT" \
  -deinterlace \
  -vcodec \
  libx264 \
  -pix_fmt \
  yuv420p \
  -preset \
  medium \
  -r 30 -g 60 -b:v 2500K \
  -acodec libmp3lame -ar 44100 \
  -threads 6 -qscale 3 -b:a 712K -bufsize 512k \
  -f flv "$STREAM_URL"
