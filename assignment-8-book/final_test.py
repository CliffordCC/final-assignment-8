import pandas as pd
from its_the_final_function import custom_count_mean

def test_one():
    raw = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
                    'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
                    'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
                    'Evergreen Oak'], 
            'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
                              'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
                              'West end','Kitsilano', 'Arbutus-ridge'],
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
                         6.5, 12.0, 18.0, 8.5, 23.0]}
    helper_data = pd.DataFrame.from_dict(raw)
    
    # Tests that the expected count and mean are returned
    assert custom_count_mean(helper_data, 'neighbourhood', 'Sunset','diameter') == (2, 15.5)
    return

def test_two():
    raw = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
                    'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
                    'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
                    'Evergreen Oak'], 
            'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
                              'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
                              'West end','Kitsilano', 'Arbutus-ridge'],
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
                         6.5, 12.0, 18.0, 8.5, 23.0]}
    helper_data = pd.DataFrame.from_dict(raw)
    
    # Tests that the expected count and mean are returned
    assert custom_count_mean(helper_data, 'type', 'Cherry','diameter') == (4, 18.875)
    return