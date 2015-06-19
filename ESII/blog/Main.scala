package scala

import scala.collection.mutable.ArrayBuffer

object Main {
  def main(Args:Array[String]){
    var dono = new Usuario("natan", "nat.mai", "natanjmai", "123", "18/06/2015");
    var blog = new Blog("Engenharia de Software II", dono)
    
    var usuario = new Usuario("user1", "user", "usr", "usus", "18/06/2015")
    
    blog.addUsuario(usuario);
    
    for (x <- blog.getUsuarios())
      println(x.getName);
    
    var nota = new Notas(usuario.getName);
    nota.setTitulo("Trabalho II");
    
    println(nota.getTitulo);
  }
}