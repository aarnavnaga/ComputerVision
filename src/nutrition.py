from dataclasses import dataclass


@dataclass
class NutritionInfo:
    calories: float
    protein_g: float
    carbs_g: float
    fat_g: float
    serving_desc: str = ""


# Approximate nutrition per typical serving (USDA estimates)
NUTRITION_DB: dict[str, NutritionInfo] = {
    "banana":   NutritionInfo(calories=105, protein_g=1.3, carbs_g=27.0, fat_g=0.4, serving_desc="1 medium"),
    "apple":    NutritionInfo(calories=95,  protein_g=0.5, carbs_g=25.0, fat_g=0.3, serving_desc="1 medium"),
    "orange":   NutritionInfo(calories=62,  protein_g=1.2, carbs_g=15.4, fat_g=0.2, serving_desc="1 medium"),
    "broccoli": NutritionInfo(calories=55,  protein_g=3.7, carbs_g=11.2, fat_g=0.6, serving_desc="1 cup"),
    "carrot":   NutritionInfo(calories=25,  protein_g=0.6, carbs_g=6.0,  fat_g=0.1, serving_desc="1 medium"),
    "hot dog":  NutritionInfo(calories=150, protein_g=5.0, carbs_g=2.0,  fat_g=13.0, serving_desc="1 frank"),
    "pizza":    NutritionInfo(calories=285, protein_g=12.0, carbs_g=36.0, fat_g=10.0, serving_desc="1 slice"),
    "donut":    NutritionInfo(calories=250, protein_g=3.0, carbs_g=31.0, fat_g=12.0, serving_desc="1 donut"),
    "cake":     NutritionInfo(calories=350, protein_g=4.0, carbs_g=52.0, fat_g=14.0, serving_desc="1 slice"),
    "sandwich": NutritionInfo(calories=300, protein_g=15.0, carbs_g=35.0, fat_g=10.0, serving_desc="1 sandwich"),
    "bottle":     NutritionInfo(calories=0,   protein_g=0.0,  carbs_g=0.0,  fat_g=0.0,  serving_desc="water bottle"),
    "wine glass": NutritionInfo(calories=125, protein_g=0.1,  carbs_g=3.8,  fat_g=0.0,  serving_desc="5 oz wine"),
    "cup":        NutritionInfo(calories=2,   protein_g=0.3,  carbs_g=0.0,  fat_g=0.0,  serving_desc="1 cup coffee/tea"),
    "bowl":       NutritionInfo(calories=150, protein_g=5.0,  carbs_g=25.0, fat_g=3.0,  serving_desc="1 bowl cereal"),
    "grape":      NutritionInfo(calories=62,  protein_g=0.6,  carbs_g=16.0, fat_g=0.3,  serving_desc="1 cup"),
    "strawberry": NutritionInfo(calories=49,  protein_g=1.0,  carbs_g=11.7, fat_g=0.5,  serving_desc="1 cup"),
    "blueberry":  NutritionInfo(calories=84,  protein_g=1.1,  carbs_g=21.4, fat_g=0.5,  serving_desc="1 cup"),
    "watermelon": NutritionInfo(calories=46,  protein_g=0.9,  carbs_g=11.5, fat_g=0.2,  serving_desc="1 cup diced"),
    "pear":       NutritionInfo(calories=101, protein_g=0.6,  carbs_g=27.0, fat_g=0.3,  serving_desc="1 medium"),
    "peach":      NutritionInfo(calories=59,  protein_g=1.4,  carbs_g=14.0, fat_g=0.4,  serving_desc="1 medium"),
    "pineapple":  NutritionInfo(calories=82,  protein_g=0.9,  carbs_g=21.6, fat_g=0.2,  serving_desc="1 cup chunks"),
    "mango":      NutritionInfo(calories=99,  protein_g=1.4,  carbs_g=24.7, fat_g=0.6,  serving_desc="1 cup"),
    "avocado":    NutritionInfo(calories=240, protein_g=3.0,  carbs_g=12.8, fat_g=22.0, serving_desc="1 medium"),
    "tomato":     NutritionInfo(calories=22,  protein_g=1.1,  carbs_g=4.8,  fat_g=0.2,  serving_desc="1 medium"),
    "cucumber":   NutritionInfo(calories=16,  protein_g=0.7,  carbs_g=3.8,  fat_g=0.1,  serving_desc="1 cup sliced"),
    "lettuce":    NutritionInfo(calories=8,   protein_g=0.6,  carbs_g=1.5,  fat_g=0.1,  serving_desc="1 cup shredded"),
    "spinach":    NutritionInfo(calories=7,   protein_g=0.9,  carbs_g=1.1,  fat_g=0.1,  serving_desc="1 cup raw"),
    "potato":     NutritionInfo(calories=161, protein_g=4.3,  carbs_g=36.6, fat_g=0.2,  serving_desc="1 medium baked"),
    "rice":       NutritionInfo(calories=206, protein_g=4.3,  carbs_g=45.0, fat_g=0.4,  serving_desc="1 cup cooked"),
    "pasta":      NutritionInfo(calories=221, protein_g=8.1,  carbs_g=43.0, fat_g=1.3,  serving_desc="1 cup cooked"),
    "bread":      NutritionInfo(calories=79,  protein_g=3.6,  carbs_g=14.0, fat_g=1.0,  serving_desc="1 slice"),
    "bagel":      NutritionInfo(calories=277, protein_g=11.0, carbs_g=55.0, fat_g=1.7,  serving_desc="1 bagel"),
    "egg":        NutritionInfo(calories=72,  protein_g=6.3,  carbs_g=0.4,  fat_g=4.8,  serving_desc="1 large"),
    "cheese":     NutritionInfo(calories=113, protein_g=7.0,  carbs_g=0.9,  fat_g=9.0,  serving_desc="1 oz cheddar"),
    "yogurt":     NutritionInfo(calories=149, protein_g=8.5,  carbs_g=11.4, fat_g=8.0,  serving_desc="1 cup whole milk"),
    "milk":       NutritionInfo(calories=149, protein_g=7.7,  carbs_g=11.7, fat_g=8.0,  serving_desc="1 cup whole"),
    "chicken":    NutritionInfo(calories=231, protein_g=43.4, carbs_g=0.0,  fat_g=5.0,  serving_desc="1 cup cooked"),
    "beef":       NutritionInfo(calories=213, protein_g=22.0, carbs_g=0.0,  fat_g=13.0, serving_desc="3 oz cooked"),
    "salmon":     NutritionInfo(calories=206, protein_g=22.0, carbs_g=0.0,  fat_g=12.0, serving_desc="3 oz cooked"),
    "tuna":       NutritionInfo(calories=99,  protein_g=22.0, carbs_g=0.0,  fat_g=0.7,  serving_desc="3 oz canned in water"),
    "shrimp":     NutritionInfo(calories=84,  protein_g=18.0, carbs_g=0.2,  fat_g=1.2,  serving_desc="3 oz cooked"),
    "hamburger":  NutritionInfo(calories=354, protein_g=20.0, carbs_g=29.0, fat_g=17.0, serving_desc="1 burger"),
    "fries":      NutritionInfo(calories=365, protein_g=4.0,  carbs_g=48.0, fat_g=17.0, serving_desc="medium order"),
    "taco":       NutritionInfo(calories=210, protein_g=10.0, carbs_g=20.0, fat_g=10.0, serving_desc="1 taco"),
    "burrito":    NutritionInfo(calories=445, protein_g=20.0, carbs_g=55.0, fat_g=15.0, serving_desc="1 burrito"),
    "sushi":      NutritionInfo(calories=200, protein_g=9.0,  carbs_g=38.0, fat_g=0.7,  serving_desc="6 pieces"),
    "soup":       NutritionInfo(calories=120, protein_g=6.0,  carbs_g=18.0, fat_g=3.0,  serving_desc="1 cup"),
    "salad":      NutritionInfo(calories=150, protein_g=3.0,  carbs_g=10.0, fat_g=11.0, serving_desc="1 bowl with dressing"),
    "cookie":     NutritionInfo(calories=148, protein_g=1.5,  carbs_g=20.0, fat_g=7.0,  serving_desc="1 medium"),
    "ice cream":  NutritionInfo(calories=273, protein_g=4.6,  carbs_g=31.0, fat_g=15.0, serving_desc="1 cup"),
    "chocolate":  NutritionInfo(calories=155, protein_g=2.2,  carbs_g=17.0, fat_g=9.0,  serving_desc="1 oz milk chocolate"),
    "coffee":     NutritionInfo(calories=2,   protein_g=0.3,  carbs_g=0.0,  fat_g=0.0,  serving_desc="1 cup black"),
    "tea":        NutritionInfo(calories=2,   protein_g=0.0,  carbs_g=0.7,  fat_g=0.0,  serving_desc="1 cup plain"),
    "soda":       NutritionInfo(calories=140, protein_g=0.0,  carbs_g=39.0, fat_g=0.0,  serving_desc="12 oz can"),
    "beer":       NutritionInfo(calories=153, protein_g=1.6,  carbs_g=13.0, fat_g=0.0,  serving_desc="12 oz regular"),
    "juice":      NutritionInfo(calories=112, protein_g=1.7,  carbs_g=26.0, fat_g=0.5,  serving_desc="1 cup orange"),
    "pancake":    NutritionInfo(calories=175, protein_g=5.0,  carbs_g=22.0, fat_g=7.0,  serving_desc="1 pancake"),
    "waffle":     NutritionInfo(calories=218, protein_g=6.0,  carbs_g=25.0, fat_g=10.6, serving_desc="1 waffle"),
    "bacon":      NutritionInfo(calories=43,  protein_g=3.0,  carbs_g=0.1,  fat_g=3.3,  serving_desc="1 slice cooked"),
    "oatmeal":    NutritionInfo(calories=158, protein_g=6.0,  carbs_g=27.0, fat_g=3.2,  serving_desc="1 cup cooked"),
    "popcorn":    NutritionInfo(calories=31,  protein_g=1.0,  carbs_g=6.2,  fat_g=0.4,  serving_desc="1 cup air-popped"),
    "almond":     NutritionInfo(calories=164, protein_g=6.0,  carbs_g=6.1,  fat_g=14.0, serving_desc="1 oz (23 nuts)"),
    "peanut butter": NutritionInfo(calories=188, protein_g=8.0, carbs_g=6.0, fat_g=16.0, serving_desc="2 tbsp"),
    "hummus":     NutritionInfo(calories=166, protein_g=7.9,  carbs_g=14.3, fat_g=9.6,  serving_desc="1/2 cup"),
    "tofu":       NutritionInfo(calories=94,  protein_g=10.0, carbs_g=2.3,  fat_g=6.0,  serving_desc="1/2 cup firm"),
    "corn":       NutritionInfo(calories=125, protein_g=4.7,  carbs_g=27.0, fat_g=2.0,  serving_desc="1 medium ear"),
    "lemon":      NutritionInfo(calories=17,  protein_g=0.6,  carbs_g=5.4,  fat_g=0.2,  serving_desc="1 medium"),
    "pumpkin":    NutritionInfo(calories=49,  protein_g=1.8,  carbs_g=12.0, fat_g=0.2,  serving_desc="1 cup cooked"),
    "mushroom":   NutritionInfo(calories=15,  protein_g=2.2,  carbs_g=2.3,  fat_g=0.2,  serving_desc="1 cup sliced"),
    "onion":      NutritionInfo(calories=44,  protein_g=1.2,  carbs_g=10.3, fat_g=0.1,  serving_desc="1 medium"),
    "pepper":     NutritionInfo(calories=37,  protein_g=1.2,  carbs_g=7.0,  fat_g=0.4,  serving_desc="1 medium bell"),
    "kiwi":       NutritionInfo(calories=42,  protein_g=0.8,  carbs_g=10.1, fat_g=0.4,  serving_desc="1 medium"),
    "cherry":     NutritionInfo(calories=87,  protein_g=1.5,  carbs_g=22.0, fat_g=0.3,  serving_desc="1 cup pitted"),
    "raspberry":  NutritionInfo(calories=64,  protein_g=1.5,  carbs_g=14.7, fat_g=0.8,  serving_desc="1 cup"),
    "zucchini":   NutritionInfo(calories=21,  protein_g=1.5,  carbs_g=3.9,  fat_g=0.4,  serving_desc="1 medium"),
    "cauliflower": NutritionInfo(calories=27, protein_g=2.1,  carbs_g=5.3,  fat_g=0.3,  serving_desc="1 cup chopped"),
    "asparagus":  NutritionInfo(calories=27,  protein_g=3.0,  carbs_g=5.2,  fat_g=0.2,  serving_desc="1 cup cooked"),
    "cabbage":    NutritionInfo(calories=22,  protein_g=1.1,  carbs_g=5.2,  fat_g=0.1,  serving_desc="1 cup shredded"),
    "sweet potato": NutritionInfo(calories=112, protein_g=2.0, carbs_g=26.0, fat_g=0.1, serving_desc="1 medium baked"),
    "lentils":    NutritionInfo(calories=230, protein_g=18.0, carbs_g=40.0, fat_g=0.8,  serving_desc="1 cup cooked"),
    "quinoa":     NutritionInfo(calories=222, protein_g=8.1,  carbs_g=39.0, fat_g=3.6,  serving_desc="1 cup cooked"),
}


def lookup(label: str) -> NutritionInfo | None:
    return NUTRITION_DB.get(label)


def sum_nutrition(items: list[NutritionInfo]) -> NutritionInfo:
    total = NutritionInfo(calories=0, protein_g=0, carbs_g=0, fat_g=0)
    for item in items:
        total.calories += item.calories
        total.protein_g += item.protein_g
        total.carbs_g += item.carbs_g
        total.fat_g += item.fat_g
    return total
