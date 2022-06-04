<template>
    
  <div class= 'container mt-5'>
      <h1>Digite o que deseja pesquisar no Banco de dados</h1>
      <div>
          <form @submit="post_consulta" >
              <input type="text"
              class="form-control"
              placeholder="Digite o que deseja pesquisar:"
              v-model="consulta"
              >
              <button class="button-3" role="button">Pesquisar</button>           
          </form>
      </div>
      <div v-for="relacao in relacaoans" v-bind:key="relacao.registro_ans">
      <p>Registro Ans da empresa: {{relacao.registro_ans}}</p>
      <p>CNPJ da empresa: {{relacao.cnpj}}</p>
      <p>Razao Social: {{relacao.razao_social}}</p>
      <p>Nome Fantasia: {{relacao.nome_fantasia}}</p>
      <p>Modalidade: {{relacao.modalidade}}</p>
      <p>Logradouro: {{relacao.logradouro}}</p>
      <p>Numero: {{relacao.numero}}</p>
      <p>Complemento: {{relacao.complemento}}</p>
      <p>Bairro: {{relacao.bairro}}</p>
      <p>Cidade: {{relacao.cidade}}</p>
      <p>UF: {{relacao.uf}}</p>
      <p>CEP: {{relacao.cep}}</p>
      <p>DDD: {{relacao.ddd}}</p>
      <p>Telefone: {{relacao.telefone}}</p>
      <p>Fax: {{relacao.fax}}</p>
      <p>Endereco Eletronico: {{relacao.endereco_eletronico}}</p>
      <p>Representante: {{relacao.representante}}</p>
      <p>Cargo do Representante: {{relacao.representante_cargo}}</p>
      <p>Data do Registro na ANS: {{relacao.data_registroans}}</p>
      <p>**************************</p>

      
      </div>
  </div>
</template>

<script>
export default {

    data(){
        return {
            relacaoans:[],
            }

    },

    methods:{
        post_consulta(){
            fetch('http://127.0.0.1:5000/postconsulta', {
                method: "POST",
                headers:{"Content-Type":"application/json"
                },
                body: JSON.stringify({consulta:this.consulta})
                
            })
            .then(resp => resp.json())
            .then(data => {
                this.relacaoans.length = 0
                this.relacaoans.push(...data)
                this.$router.push({
                    name:'query'
                })
            })
            .catch(error => {
                console.log(error)
            })
        },
        

     
       
    },
    created(){
    },
    

}


</script>

<style>


/* CSS */
.button-3 {
  appearance: none;
  background-color: #2ea44f;
  border: 1px solid rgba(27, 31, 35, .15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  padding: 6px 16px;
  position: relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
}

.button-3:focus:not(:focus-visible):not(.focus-visible) {
  box-shadow: none;
  outline: none;
}

.button-3:hover {
  background-color: #2c974b;
}

.button-3:focus {
  box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
  outline: none;
}

.button-3:disabled {
  background-color: #94d3a2;
  border-color: rgba(27, 31, 35, .1);
  color: rgba(255, 255, 255, .8);
  cursor: default;
}

.button-3:active {
  background-color: #298e46;
  box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
</style>