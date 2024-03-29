// Departamento.java
package inmobiliarias;

public class Departamento extends Inmueble {

	private boolean cochera;
	private boolean baulera;

	public Departamento(String domicilio, double superficie, int cantidadAmbientes, int precio, boolean cochera,
			boolean baulera) {
		super(domicilio, superficie, cantidadAmbientes, precio);
		this.cochera = cochera;
		this.baulera = baulera;
	}

	public boolean getCochera() {
		return cochera;
	}

	public boolean getBaulera() {
		return baulera;
	}

	public String imprimirDatos() {
		String strDepartamento = String.format("\nCochera: %b.\nCochera: %b.\n", this.getCochera(), this.getBaulera());
		return super.imprimirDatos() + strDepartamento;
	}

	// nuevo m�todo:
	public double comisionVendedor() {
		if (getCochera())
			return 0.009 * getPrecio();
		else
			return 0.011 * getPrecio();
	}
}
