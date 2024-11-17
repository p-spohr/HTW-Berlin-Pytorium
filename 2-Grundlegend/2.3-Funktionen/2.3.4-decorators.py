# %%

def mittelwert(*args):
    return round(sum(args) / len(args),2)

mittelwert(12,23,54)

# %%

def prettier(func):
	def wrapper(*args):
		print('From prettier...')
		output = func(*args)
		print(f'Der {func.__name__.capitalize()} ist {str(output).replace('.', ',')}!')
		return output
	return wrapper

# %%

@prettier
def mittelwert(*args):
    return round(sum(args) / len(args),2)

mittelwert(12,23,54)

# %%
import time 
def log_time(func): 
	def wrapper(*args, **kwargs): 
		start_time = time.time() 
		result = func(*args, **kwargs) 
		end_time = time.time() 
		print(f"{func.__name__} dauerte {round(end_time - start_time,3)} Sekunden") 
		return result 
	return wrapper 

@log_time 
def slow_function(): 
	time.sleep(2)
	print("Funktion beendet") 

slow_function()
