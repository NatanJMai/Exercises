package scala

import scala.collection.mutable.ArrayBuffer

class Notas (autA : String) extends Post {
  private var Comentarios = new ArrayBuffer[Comentario]
  var         autor       = autA;
  
  def addComentario(comm : Comentario) = {
    this.Comentarios.append(comm);
  }
  
  def removeComentario(comm : Comentario) = {
    this.Comentarios.-=(comm);
  }
  
  def getComentarios() : ArrayBuffer[Comentario] = {
    return this.Comentarios;
  } 
  
}