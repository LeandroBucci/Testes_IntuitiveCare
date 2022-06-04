select relacao_ans.razao_social, sum(vl_saldo) from custo_2021
inner join relacao_ans on relacao_ans.registro_ans = custo_2021.registro_ans
group by custo_2021.registro_ans
order by sum(vl_saldo) desc limit 10