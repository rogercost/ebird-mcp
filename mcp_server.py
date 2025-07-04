import os
from fastmcp import FastMCP
from ebird.api import (
    get_observations, get_hotspots, get_nearby_hotspots, get_hotspot,
    get_species_observations, get_nearby_observations, get_notable_observations,
    get_nearest_species, get_nearby_species, get_visits, get_checklist,
    get_regions, get_adjacent_regions, get_region, get_taxonomy,
    get_top_100, get_totals
)

# Get eBird API key from environment variable
api_key = os.environ.get("EBIRD_API_KEY")

if not api_key:
    raise ValueError("EBIRD_API_KEY environment variable not set.")

# Create a server instance with a descriptive name
mcp = FastMCP(name="eBird-API-MCP")

@mcp.tool
def get_ebird_observations(region_code: str, back: int = 7, detail: str = 'full') -> list:
    """
    Get bird observations for a specific region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :param back: The number of days to look back for observations (1-30).
    :param detail: The level of detail for the observations ('full' or 'simple').
    :return: A list of observations.
    """
    return get_observations(api_key, region_code, back=back, detail=detail)

@mcp.tool
def get_ebird_hotspots(region_code: str, back: int = 7) -> list:
    """
    Get birding hotspots for a specific region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :param back: The number of days to look back for visits (1-30).
    :return: A list of hotspots.
    """
    return get_hotspots(api_key, region_code, back=back)


@mcp.tool
def get_nearby_ebird_hotspots(lat: float, lng: float, dist: int = 10) -> list:
    """
    Get birding hotspots near a specific location.

    :param lat: Latitude.
    :param lng: Longitude.
    :param dist: The search radius in kilometers (0-50).
    :return: A list of nearby hotspots.
    """
    return get_nearby_hotspots(api_key, lat, lng, dist=dist)


@mcp.tool
def get_ebird_hotspot_info(loc_id: str) -> dict:
    """
    Get information about a specific hotspot.

    :param loc_id: The location ID of the hotspot.
    :return: A dictionary containing hotspot information.
    """
    return get_hotspot(api_key, loc_id)


@mcp.tool
def get_ebird_species_observations(species_code: str, region_code: str) -> list:
    """
    Get observations of a specific species in a region.

    :param species_code: The species code (e.g., 'horlar').
    :param region_code: The code for the region (e.g., 'US-NY').
    :return: A list of observations.
    """
    return get_species_observations(api_key, species_code, region_code)


@mcp.tool
def get_nearby_ebird_observations(lat: float, lng: float, dist: int = 10, back: int = 7) -> list:
    """
    Get bird observations near a specific location.

    :param lat: Latitude.
    :param lng: Longitude.
    :param dist: The search radius in kilometers (0-50).
    :param back: The number of days to look back for observations (1-30).
    :return: A list of nearby observations.
    """
    return get_nearby_observations(api_key, lat, lng, dist=dist, back=back)


@mcp.tool
def get_notable_ebird_observations(region_code: str, detail: str = 'full') -> list:
    """
    Get notable bird observations for a specific region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :param detail: The level of detail for the observations ('full' or 'simple').
    :return: A list of notable observations.
    """
    return get_notable_observations(api_key, region_code, detail=detail)


@mcp.tool
def get_nearest_ebird_species(species_code: str, lat: float, lng: float) -> list:
    """
    Find the nearest location where a species has been observed.

    :param species_code: The species code (e.g., 'tenwar').
    :param lat: Latitude.
    :param lng: Longitude.
    :return: A list of nearest locations.
    """
    return get_nearest_species(api_key, species_code, lat, lng)


@mcp.tool
def get_nearby_ebird_species(species_code: str, lat: float, lng: float, back: int = 10) -> list:
    """
    Get recent sightings of a species near a location.

    :param species_code: The species code (e.g., 'barswa').
    :param lat: Latitude.
    :param lng: Longitude.
    :param back: The number of days to look back for observations (1-30).
    :return: A list of nearby species sightings.
    """
    return get_nearby_species(api_key, species_code, lat, lng, back=back)


@mcp.tool
def get_ebird_visits(region_code: str, date: str = None) -> list:
    """
    Get a list of visits for a given region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :param date: The date of the visits (YYYY-MM-DD).
    :return: A list of visits.
    """
    return get_visits(api_key, region_code, date)


@mcp.tool
def get_ebird_checklist(sub_id: str) -> dict:
    """
    Get the details of a specific checklist.

    :param sub_id: The submission ID of the checklist.
    :return: A dictionary containing checklist details.
    """
    return get_checklist(api_key, sub_id)


@mcp.tool
def get_ebird_regions(region_type: str, parent_region_code: str) -> list:
    """
    Get a list of sub-regions for a given parent region.

    :param region_type: The type of region ('country', 'subnational1', 'subnational2').
    :param parent_region_code: The code for the parent region (e.g., 'world', 'US', 'US-NY').
    :return: A list of regions.
    """
    return get_regions(api_key, region_type, parent_region_code)


@mcp.tool
def get_adjacent_ebird_regions(region_code: str) -> list:
    """
    Get a list of regions adjacent to a given region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :return: A list of adjacent regions.
    """
    return get_adjacent_regions(api_key, region_code)


@mcp.tool
def get_ebird_region_info(region_code: str) -> dict:
    """
    Get information about a specific region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :return: A dictionary containing region information.
    """
    return get_region(api_key, region_code)


@mcp.tool
def get_ebird_taxonomy(locale: str = 'en') -> list:
    """
    Get the eBird taxonomy.

    :param locale: The locale for the common names (e.g., 'es', 'fr').
    :return: A list of species in the taxonomy.
    """
    return get_taxonomy(api_key, locale=locale)


@mcp.tool
def get_ebird_top_100(region_code: str, ymd: str) -> list:
    """
    Get the top 100 observers for a region on a specific date.

    :param region_code: The code for the region (e.g., 'US-NY').
    :param ymd: The date in 'YYYY-MM-DD' format.
    :return: A list of the top 100 observers.
    """
    return get_top_100(api_key, region_code, ymd)


@mcp.tool
def get_ebird_totals(region_code: str) -> dict:
    """
    Get daily totals for a region.

    :param region_code: The code for the region (e.g., 'US-NY').
    :return: A dictionary containing daily totals.
    """
    from datetime import date
    return get_totals(api_key, region_code, date.today())


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
