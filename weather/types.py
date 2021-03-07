import json

class Result:
	def __init__(self, data):
		self.res = {}
		self.data = data
		for k,v in self.data.items():
			if( isinstance(v, dict) ):
				self.res[k] = Result(self.data[k])
				
			elif( isinstance(v, list) ):
				self.res[k] = Result(self.data[k][0])
				
			else: self.res[k] = v
	
	def __str__(self):
		return json.dumps(self.data, indent=4)
	
	def __repr__(self):
		return json.dumps(self.data, indent=4)
	
	def __getitem__(self, item):
		try: return self.res[item]
		except KeyError: return None
	
	def __setitem__(self, key, value):
		self.res[key] = value
	
	def __getattr__(self, item):
		try: return self.res[item]
		except KeyError: return None
	
	def __missing__(self, item):
		return None
	
	def __delitem__(self, item):
		del self.res[item]
	
	def __delattr__(self, item):
		del self.res[item]
	
	def __rshift__(self, item):
		try:
			f = open(item, "w")
		except TypeError:
			f = item
		
		f.write( json.dumps(self.data) )
		f.close()
