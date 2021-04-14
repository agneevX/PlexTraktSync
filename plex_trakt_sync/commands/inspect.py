import click
from plexapi.server import PlexServer
from plex_trakt_sync.config import CONFIG
from plex_trakt_sync.plex_api import PlexApi


@click.command()
@click.argument('input')
def inspect(input):
    """
    Inspect details of an object
    """

    url = CONFIG["PLEX_BASEURL"]
    token = CONFIG["PLEX_TOKEN"]
    server = PlexServer(url, token)
    plex = PlexApi(server)

    if input.isnumeric():
        input = int(input)

    m = plex.fetch_item(input)
    media = m.item

    print(f"Guid: '{media.guid}'")
    print(f"Guids: {media.guids}")

    audio = media.media[0].parts[0].audioStreams()[0]
    print(f"Audio: '{audio.audioChannelLayout}', '{audio.displayTitle}'")

    video = media.media[0].parts[0].videoStreams()[0]
    print(f"Video: '{video.codec}'")
