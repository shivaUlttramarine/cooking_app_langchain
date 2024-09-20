from pydantic import BaseModel, Field
from typing import List

class reciept(BaseModel):
    ingredients: List[str]  
    instructions: List[str]  

    # ingredients: List[str] = Field(..., description="list of ingredients")
    # instructions: List[str] = Field(..., description="list of cooking instructions to do by ingriedients")

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "ingredients": ["2 medium eggplants", "1 onion, chopped", "2 cloves of garlic, minced"],
    #             "instructions": ['1. Start by peeling strips of the eggplant skin lengthwise, leaving some skin on to create a striped effect. Cut the eggplants into cubes.',
    #                             '2. In a large pan, heat some olive oil over medium heat. Add the chopped onion and minced garlic, and sauté until the onion is translucent.',
    #                             '3. Add the cubed eggplant to the pan and cook until they start to soften, stirring occasionally.',
    #                             '4. Add the diced tomatoes, turmeric, cumin, cinnamon, salt, and pepper to the pan. Stir well to combine all the ingredients.',
    #                             '5. Cover the pan and let the stew simmer for about 20-25 minutes, or until the eggplant is fully cooked and the flavors have melded together.',
    #                             '6. Taste and adjust the seasoning if needed.',
    #                             '7. Serve the Eggplant Stew hot, garnished with fresh parsley. This dish goes well with rice or bread.'
    #                             ]
    #         }
    #     }