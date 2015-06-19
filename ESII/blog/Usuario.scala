package scala

import scala.collection.mutable.ArrayBuffer

class Usuario (name : String, emailA : String, usuarioA : String, senhaA : String, dataNascA : String) {
  private var nome      = name;
  private var email     = emailA;
  private var usuario   = usuarioA;
  private var senha     = senhaA;
  private var Coments   = new ArrayBuffer[Comentario];
  var         dataNasc  = dataNascA;
  
  
  def getName      = this.nome;
  def getEmail     = this.email;
  def getUsuario   = this.usuario;
  def getSenha     = this.senha;
  def getComents   = this.Coments;
  
  def setNome(name : String) = {
    this.nome = name;
  }
  
  def setEmail(email: String) = {
    this.email = email;
  }
  
  def setUsuario(usuario: String) = {
    this.usuario = usuario;
  }
  
  def setSenha(senh : String) = {
    this.senha = senh;
  }
  
  def addComments (comm : Comentario) = {
    this.Coments.append(comm);
  }
  
  def removeComment(comm : Comentario) = {
    this.Coments.-=(comm);
  }
}