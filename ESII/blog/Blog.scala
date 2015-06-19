package scala
import scala.collection.mutable.ArrayBuffer

class Blog (name : String, user : Usuario){
  var data : String     = ""; 
  private var nome      = name;
  private var dono      = user;
  private var Usuarios  = new ArrayBuffer[Usuario];
  private var Notas     = new ArrayBuffer[Notas];
  
  /* getName method */
  def getName     = this.nome;
  
  /* getDonoName method */
  def getDonoName = this.dono.getName;
  
  /* addUsuario method */
  def addUsuario (usuario : Usuario) {
    this.Usuarios.append(usuario);
  }
  
  /* getUsuarios method */
  def getUsuarios() : ArrayBuffer[Usuario] = {
    return this.Usuarios;
  }
  
  /* removeUsuario method */
  def removeUsuario(usuario : Usuario) = {
    this.Usuarios.-=(usuario);
  }
  
  def addNota(nota : Notas) = {
    this.Notas.append(nota);
  }
  
  def removeNota(nota : Notas) = {
    this.Notas.-=(nota);
  }
}