def function(a, b):
    print a, b

apply(function, ("whither",), {"b": "frog"})
apply(function, (), {"a": "crunchy", "b": "frog"})