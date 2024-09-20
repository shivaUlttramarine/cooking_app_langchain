from flask import Flask, render_template, request, jsonify
 
import process.model as process





# Initialize the LangChain LLM (make sure to replace with your actual OpenAI API key)
# with open('openaikey.txt', 'r') as file:
#     api_key = file.read().strip()
# f = open('openaikey.txt', 'r')
# os.environ["OPENAI_API_KEY"]=f.read()


# Carbohydrates
list_cooking_time =['15','30','45','60','90','120','180 or more']
list_ingredients_carbohydrates = [
    'rice', 'pasta', 'bread', 'potatoes', 'oats', 'quinoa', 'barley',  'couscous', 'bulgur',
    'sweet potatoes', 'tortillas', 'polenta', 'farro', 'soba noodles', 'ramen noodles', 'grits', 'buckwheat',
    'muesli', 'granola', 'crackers', 'pita bread', 'bagels', 'english muffins', 'croutons', 'sorghum',
    'teff', 'amaranth', 'spelt', 'rye', 'millet', 'tapioca', 'sago', 'wheat germ', 'bread crumbs',
    'semolina', 'tapioca pearls',   'rice noodles', 'udon noodles', 'rice cakes', 'puffed rice',
    'puffed quinoa', 'puffed wheat',   'instant noodles', 'wild rice', 'bean sprouts', 'chickpeas',
    'lentils',   'split peas',
]

# Meat
list_ingredients_meat = [
    'chicken breast','egg', 'beef steak', 'pork chops', 'ground beef', 'chicken thighs', 'lamb chops', 'turkey', 
    'salmon','tuna','ground turkey', 'pork belly', 'sausages', 'bacon', 'veal', 'duck', 'ham', 'salami', 'prosciutto', 
    'chorizo', 'pork ribs', 'beef ribs', 'beef brisket', 'chicken wings', 'chicken drumsticks', 
    'meatballs', 'roast beef', 'steak', 'short ribs', 'pork tenderloin', 'chicken liver', 'beef liver',
    'beef stew meat', 'chicken sausage', 'turkey bacon', 'duck breast', 'oxtail', 'liverwurst', 'chuck roast',
    'ribs', 'pork shoulder', 'lamb shank', 'kielbasa', 'corned beef', 'beef tenderloin', 'beef chuck',
    'veal cutlets', 'turkey legs', 'pork sausages', 'beef short ribs', 'roast lamb', 
    'chicken gizzards', 'turkey breast', 'ground lamb',  'rabbit',
]

# Vegetables
list_ingredients_vegetables = [
    'carrots',   'onions', 'garlic', 'bell peppers', 'broccoli', 'spinach', 'tomatoes', 'zucchini',
    'cucumbers', 'mushrooms', 'corn', 'peas', 'celery', 'cauliflower', 'green beans', 'kale', 'asparagus',
     'eggplant', 'beets', 'brussels sprouts', 'lettuce', 'radishes', 'squash', 'artichokes',
    'turnips', 'pumpkin', 'butternut squash', 'leeks', 'chard', 'fennel', 'basil', 'cilantro', 'parsley',
    'green onions', 'shallots', 'ginger', 'jalapenos', 'dandelion greens', 'beet greens', 'watercress',
    'daikon radish', 'cabbage', 'okra', 'yams', 'rhubarb', 'chili peppers', 'endive', 'snow peas',
    'arugula', 'miso', 'seaweed', 'sauerkraut',
]


list_ingredients_dairy = [
    'milk', 'butter', 'cheese', 'yogurt', 'cream', 'cottage cheese', 'sour cream', 'mozzarella', 'cheddar',
    'parmesan', 'swiss cheese', 'feta', 'ricotta', 'cream cheese', 'kefir', 'buttermilk', 'gouda',
    'blue cheese', 'goat cheese', 'gruyere', 'fontina', 'provolone', 'brie', 'mascarpone', 'evaporated milk',
    'condensed milk', 'milk powder', 'clotted cream', 'half-and-half', 'skyr', 'queso fresco', 'paneer',
    'string cheese', 'dubliner', 'aged cheddar', 'neufchâtel', 'emmental', 'teleme', 'burrata',  
    'chèvre', 'queso blanco', 'creme fraiche',
]

# Others
list_ingredients_others = [
    'olive oil', 'vinegar', 'salt', 'black pepper',  'honey', 'mustard', 'ketchup', 'hot sauce',
    'sriracha', 'balsamic vinegar', 'lemon juice', 'lime juice', 'coconut milk',   'sugar', 'maple syrup',
    'sesame oil', 'chili flakes', 'baking powder', 'baking soda', 'worcestershire sauce',  'cornstarch',
    'tomato paste', 'curry powder', 'paprika', 'cumin', 'oregano', 'thyme', 'rosemary', 'dill', 'sage',
    'bay leaves', 'tarragon' , 'garlic powder', 'onion powder', 'five-spice powder', 'nutmeg', 'allspice',
    'cardamom', 'cinnamon', 'cloves', 'vanilla extract', 'almond extract', 'cocoa powder', 'nutritional yeast',
    'fish sauce', 'soy sauce', 'truffle oil',   'molasses', 'chili paste', 'hoisin sauce', 'miso paste',
    'tahini',     'rice vinegar'
]
 
app = Flask(__name__)
@app.route('/generate', methods=['POST'])
def generate():
    print('************I am in generate')
    my_recept = None 
    selected_ingredients  = []  
    selected_cooking_time   = []   
    print(f'request: {request.form}')
    selected_ingredients = request.form.getlist('selected_items')
    selected_cooking_times = request.form.getlist('selected_cooking_time')
    # # Do something with the selected items (e.g., print or save them)
    print("Selected items:", selected_ingredients)
    print(f'selected_cooking_times:{selected_cooking_times}')

    my_recept = process.func_ai_create_recept(selected_ingredients,selected_cooking_time)
    my_recept.visualize()  
    images_with_descriptions = my_recept.get_images()
    # images_with_descriptions = [{'filename': 'step_1.png', 'description': '1. In a large bowl, mix together the grated potatoes and oats.'}]
    print(f'------- in images_with_descriptions={images_with_descriptions}')    
  
    print(f'------***- type of images_with_descriptions:{type(images_with_descriptions)}')
    print(f'------- in images_with_descriptions={images_with_descriptions}')    
    return jsonify(generated_images =  images_with_descriptions   )

    # return render_template('index.html'
    #                        , generated_images =  'hello Mehrdad')

@app.route('/', methods=['GET', 'POST'])
def index():
    my_recept = None 
    selected_ingredients  = []  
    selected_cooking_time   = []   
    images_with_descriptions =  []
    if request.method == 'POST':
        print('I am in post')
        selected_ingredients    = []
        selected_cooking_time   = []
        
        selected_ingredients = request.form.getlist('selected_items')
        selected_cooking_times = request.form.getlist('selected_cooking_time')
        # # Do something with the selected items (e.g., print or save them)
        print("Selected items:", selected_ingredients)
        print(f'selected_cooking_times:{selected_cooking_times}')
    
        my_recept = process.func_ai_create_recept(selected_ingredients,selected_cooking_time)
        my_recept.visualize()  
        images_with_descriptions = my_recept.get_images()
        print(f'------- in images_with_descriptions={images_with_descriptions}')    
        
    print(f'type of images_with_descriptions:{type(images_with_descriptions)}')
    print(f'------- in images_with_descriptions={images_with_descriptions}')    
    return render_template('index.html'
                           , generated_images =  images_with_descriptions
                           , items_carbohydrates= list_ingredients_carbohydrates
                           , items_dairy        = list_ingredients_dairy
                           , items_meat         = list_ingredients_meat
                           , items_others       = list_ingredients_others
                           , items_vegetables   = list_ingredients_vegetables
                           , items_cooking_time = list_cooking_time

                           , selected_ingredients   = selected_ingredients                                           
                           , selected_cooking_time  = selected_cooking_time
                           , result =   my_recept
                           
                             )


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    return jsonify(list_cooking_time)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)