package scala

class Post () {
  private var titulo : String = "";
  private var data   : String = "";
  private var texto  : String = "";
  
  def getTitulo() : String = {
    return this.titulo;
  }
  
  def getData() : String = {
    return this.data;
  }
  
  def getText() : String = {
    return this.texto;
  }
  
  def setTitulo(newTi : String) {
    this.titulo = newTi;
  }
  
  def setData(newData : String) {
    this.data = newData;
  }
  
  def setText(newTx : String) {
    this.texto = newTx;
  }
}