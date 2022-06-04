<template>
  <div class= 'container mt-5'>
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
        get_db(){
            fetch('http://127.0.0.1:5000/get', {
                method: "GET",
                headers:{"Content-Type":"application/json"

                }
            })
            .then(resp => resp.json())
            .then(data => {
                this.relacaoans.push(...data),
                console.log(data)
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    created(){
        this.get_db()
    }

}
</script>

<style>

</style>