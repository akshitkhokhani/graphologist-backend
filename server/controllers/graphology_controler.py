from typing import Optional

from pydantic import BaseModel

class Output(BaseModel):  # serializer
    emotional_stability: Optional[str]
    mental_energy_or_will_power: Optional[str]
    modesty: Optional[str]
    personal_harmony_and_flexibility: Optional[str]
    lack_of_discipline: Optional[str]
    poor_concentration: Optional[str]
    non_communicativeness: Optional[str]
    social_isolation: Optional[str]
    
