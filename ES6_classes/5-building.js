export default class Building { 
	contructor(sqft) { 
		this.sqft = sqft; 
	}

	get sqft() { 
		return this._sqft; 
	}

	if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') { 
		throw new Error('Class extending Building must override evacuationWarningMessage'); 
	}
}
