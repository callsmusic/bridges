export $(cat .env | xargs)

ffmpeg \
  -f \
  s16le \
  -ac \
  2 \
  -ar \
  48K \
  -i \
  "$FIFO" \
  -f \
  mp3 \
  "$OUTPUT"
