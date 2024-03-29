// Casa.java
package inmobiliarias;

public class Casa extends Inmueble {

	private boolean garage;
	private boolean jardin;
	private boolean pileta;
	private int superficieTerreno;

	public Casa(String domicilio, double superficie, int cantidadAmbientes, int precio, boolean garage, boolean jardin,
			boolean pileta, int superficieTerreno) {
		super(domicilio, superficie, cantidadAmbientes, precio);
		this.garage = garage;
		this.jardin = jardin;
		this.pileta = pileta;
		this.superficieTerreno = superficieTerreno;
	}

	public boolean getGarage() {
		return garage;
	}

	public boolean getJardin() {
		return jardin;
	}

	public boolean getPileta() {
		return pileta;
	}

	public int getSuperficieTerreno() {
		return superficieTerreno;
	}

	public String imprimirDatos() {
		String salida = String.format("\nGarage: %b.\nJardin: %b.\nPileta: %b.\nSuperficie terreno: %d.\n",
				this.getGarage(), this.getJardin(), this.getPileta(), this.getSuperficieTerreno());
		return super.imprimirDatos() + salida;
	}

	// nuevo m�todo:
	public double comisionVendedor() {
		if (getJardin() && getPileta())
			return 0.008 * getPrecio();
		if (getJardin())
			return 0.010 * getPrecio();
		return 0.012 * getPrecio();
	}
}
