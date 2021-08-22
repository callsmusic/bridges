# Bridge 2

This bridges audio of a Telegram call to OBS Studio.

## Requirements

-   Python
-   Ffmpeg
-   A Unix OS

## Setting up

1. Start [recorder](../recorder).

2. Copy `example.env` to `.env` and add your credentials.

## Running

```bash
bash bridge.sh
```

## Using on OBS Studio

1. Add a Media Source.
2. Uncheck "Local File".
3. Set "Input" to the path of the FIFO that Ffmpeg is writing to.
4. Set "Input Format" to mp3.

## Authors

-   [@rojserbest](https://github.com/rojserbest)
