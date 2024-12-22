import enum
from typing import Annotated
from livekit.agents import llm
import logging
logger = logging.getLogger("cosmos-management")
logger.setLevel(logging.INFO)
class CosmosRegion(enum.Enum):
    MILKY_WAY = "milky_way"
    ANDROMEDA = "andromeda"
    SOMBRERO = "sombrero"
class GalaxyAssistant(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()
        self._galaxy_details = {
            CosmosRegion.MILKY_WAY: {"stars": 100_000_000_000, "age": 13.6},
            CosmosRegion.ANDROMEDA: {"stars": 1_000_000_000_000, "age": 10},
            CosmosRegion.SOMBRERO: {"stars": 800_000_000_000, "age": 9},
        }

@llm.ai_callable(description="Get details about a specific galaxy")
def get_galaxy_details(
        self, region: Annotated[CosmosRegion, llm.TypeInfo(description="The specific cosmos region")]
    ):
        logger.info("get galaxy details - region %s", region)
        details = self._galaxy_details[CosmosRegion(region)]
        return (f"The {region} galaxy has approximately {details['stars']} stars "
                f"and is {details['age']} billion years old.")

@llm.ai_callable(description="Set details for a specific galaxy")
def set_galaxy_details(
        self,
        region: Annotated[CosmosRegion, llm.TypeInfo(description="The specific cosmos region")],
        stars: Annotated[int, llm.TypeInfo(description="The number of stars in the galaxy")],
        age: Annotated[float, llm.TypeInfo(description="The age of the galaxy in billions of years")],
    ):
        logger.info("set galaxy details - region %s, stars: %s, age: %s", region, stars, age)
        self._galaxy_details[CosmosRegion(region)] = {"stars": stars, "age": age}
        return (f"The {region} galaxy now has approximately {stars} stars "
                f"and is {age} billion years old.")
