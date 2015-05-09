# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries
myquery = None

# Get the brand with the **id** of 8.
myquery = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
myquery = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
myquery = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
myquery = Brand.query.filter(Brand.year > 1920).all()

# Get all models with names that begin with "Cor".
myquery = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
myquery = Brand.query.filter_by(founded=1903, discontinued=None).all()

# Get all brands with that are either discontinued or founded before 1950.
myquery = Brand.query.filter(db.or_(Brand.discontinued != None, Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
myquery = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """ 
    Search brands by name. How is it possible to use something like ('%Jane%') with the variable mystr? 
    """
    myquery = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()
     
    for brand in myquery:
        print brand.id, brand.name, brand.founded


def get_models_between(start_year, end_year):
    myquery = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return myquery

# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# Nothing returns except a query object! Potential once returned will be all brand objects with the name 'Ford'. I think only one object will return.

# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?
# Association table is where the data stored within is never displayed, or returned. It is simply in place to connect one table to another, as a middle man.