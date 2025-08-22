export default class Building { 
	contructor(sqft) { 
		this.sqft = sqft; 
	}


	if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') { 
		throw new Error('Class extending Building must override evacuationWarningMessage'); 
	}

	get sqft() { 
		return this._sqft; 
	}
}
