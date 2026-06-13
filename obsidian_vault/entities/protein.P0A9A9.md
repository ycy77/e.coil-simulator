---
entity_id: "protein.P0A9A9"
entity_type: "protein"
name: "fur"
source_database: "UniProt"
source_id: "P0A9A9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fur b0683 JW0669"
---

# fur

`protein.P0A9A9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9A9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Acts as a global negative controlling element, employing Fe(2+) as a cofactor to bind the operator of the repressed genes. Regulates the expression of several outer-membrane proteins including the iron transport operon. {ECO:0000269|PubMed:2823881}.

## Biological Role

Component of [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

FUNCTION: Acts as a global negative controlling element, employing Fe(2+) as a cofactor to bind the operator of the repressed genes. Regulates the expression of several outer-membrane proteins including the iron transport operon. {ECO:0000269|PubMed:2823881}.

## Outgoing Edges (181)

- `activates` --> [[gene.b0063|gene.b0063]] `RegulonDB` `S` - regulator=Fur; target=araB; function=+
- `activates` --> [[gene.b0272|gene.b0272]] `RegulonDB` `S` - regulator=Fur; target=xynR; function=+
- `activates` --> [[gene.b0273|gene.b0273]] `RegulonDB` `S` - regulator=Fur; target=argF; function=+
- `activates` --> [[gene.b0411|gene.b0411]] `RegulonDB` `S` - regulator=Fur; target=tsx; function=+
- `activates` --> [[gene.b0572|gene.b0572]] `RegulonDB` `S` - regulator=Fur; target=cusC; function=+
- `activates` --> [[gene.b0591|gene.b0591]] `RegulonDB` `C` - regulator=Fur; target=entS; function=-+
- `activates` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=Fur; target=sdhC; function=-+
- `activates` --> [[gene.b0722|gene.b0722]] `RegulonDB` `S` - regulator=Fur; target=sdhD; function=-+
- `activates` --> [[gene.b0723|gene.b0723]] `RegulonDB` `S` - regulator=Fur; target=sdhA; function=-+
- `activates` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - regulator=Fur; target=sucA; function=+
- `activates` --> [[gene.b0727|gene.b0727]] `RegulonDB` `S` - regulator=Fur; target=sucB; function=+
- `activates` --> [[gene.b0728|gene.b0728]] `RegulonDB` `S` - regulator=Fur; target=sucC; function=+
- `activates` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - regulator=Fur; target=sucD; function=+
- `activates` --> [[gene.b0836|gene.b0836]] `RegulonDB` `S` - regulator=Fur; target=bssR; function=+
- `activates` --> [[gene.b0893|gene.b0893]] `RegulonDB` `S` - regulator=Fur; target=serS; function=+
- `activates` --> [[gene.b0894|gene.b0894]] `RegulonDB` `S` - regulator=Fur; target=dmsA; function=+
- `activates` --> [[gene.b0895|gene.b0895]] `RegulonDB` `S` - regulator=Fur; target=dmsB; function=+
- `activates` --> [[gene.b0896|gene.b0896]] `RegulonDB` `S` - regulator=Fur; target=dmsC; function=+
- `activates` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=Fur; target=rmf; function=+
- `activates` --> [[gene.b1083|gene.b1083]] `RegulonDB` `S` - regulator=Fur; target=flgL; function=+
- `activates` --> [[gene.b1194|gene.b1194]] `RegulonDB` `S` - regulator=Fur; target=ycgR; function=+
- `activates` --> [[gene.b1247|gene.b1247]] `RegulonDB` `S` - regulator=Fur; target=oppF; function=-+
- `activates` --> [[gene.b1252|gene.b1252]] `RegulonDB` `S` - regulator=Fur; target=tonB; function=-+
- `activates` --> [[gene.b1276|gene.b1276]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1469|gene.b1469]] `RegulonDB` `S` - regulator=Fur; target=narU; function=+
- `activates` --> [[gene.b1521|gene.b1521]] `RegulonDB` `S` - regulator=Fur; target=uxaB; function=+
- `activates` --> [[gene.b1601|gene.b1601]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=tqsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1821|gene.b1821]] `RegulonDB` `S` - regulator=Fur; target=mntP; function=+
- `activates` --> [[gene.b1901|gene.b1901]] `RegulonDB` `S` - regulator=Fur; target=araF; function=+
- `activates` --> [[gene.b1902|gene.b1902]] `RegulonDB` `S` - regulator=Fur; target=ftnB; function=+
- `activates` --> [[gene.b1905|gene.b1905]] `RegulonDB` `C` - regulator=Fur; target=ftnA; function=+
- `activates` --> [[gene.b1916|gene.b1916]] `RegulonDB` `S` - regulator=Fur; target=sdiA; function=+
- `activates` --> [[gene.b2150|gene.b2150]] `RegulonDB` `S` - regulator=Fur; target=mglB; function=+
- `activates` --> [[gene.b2339|gene.b2339]] `RegulonDB` `S` - regulator=Fur; target=yfcV; function=+
- `activates` --> [[gene.b2503|gene.b2503]] `RegulonDB` `S` - regulator=Fur; target=pdeF; function=+
- `activates` --> [[gene.b2522|gene.b2522]] `RegulonDB` `S` - regulator=Fur; target=sseB; function=+
- `activates` --> [[gene.b2526|gene.b2526]] `RegulonDB` `S` - regulator=Fur; target=hscA; function=+
- `activates` --> [[gene.b2970|gene.b2970]] `RegulonDB` `S` - regulator=Fur; target=yghF; function=+
- `activates` --> [[gene.b2997|gene.b2997]] `RegulonDB` `S` - regulator=Fur; target=hybO; function=+
- `activates` --> [[gene.b3011|gene.b3011]] `RegulonDB` `S` - regulator=Fur; target=yqhD; function=+
- `activates` --> [[gene.b3012|gene.b3012]] `RegulonDB` `S` - regulator=Fur; target=dkgA; function=+
- `activates` --> [[gene.b3092|gene.b3092]] `RegulonDB` `S` - regulator=Fur; target=uxaC; function=+
- `activates` --> [[gene.b3336|gene.b3336]] `RegulonDB` `S` - regulator=Fur; target=bfr; function=+
- `activates` --> [[gene.b3441|gene.b3441]] `RegulonDB` `S` - regulator=Fur; target=yhhY; function=+
- `activates` --> [[gene.b3540|gene.b3540]] `RegulonDB` `S` - regulator=Fur; target=dppF; function=+
- `activates` --> [[gene.b3541|gene.b3541]] `RegulonDB` `S` - regulator=Fur; target=dppD; function=+
- `activates` --> [[gene.b3542|gene.b3542]] `RegulonDB` `S` - regulator=Fur; target=dppC; function=+
- `activates` --> [[gene.b3543|gene.b3543]] `RegulonDB` `S` - regulator=Fur; target=dppB; function=+
- `activates` --> [[gene.b3874|gene.b3874]] `RegulonDB` `S` - regulator=Fur; target=yihN; function=+
- `activates` --> [[gene.b3885|gene.b3885]] `RegulonDB` `S` - regulator=Fur; target=yihX; function=+
- `activates` --> [[gene.b3926|gene.b3926]] `RegulonDB` `S` - regulator=Fur; target=glpK; function=+
- `activates` --> [[gene.b3927|gene.b3927]] `RegulonDB` `S` - regulator=Fur; target=glpF; function=+
- `activates` --> [[gene.b3928|gene.b3928]] `RegulonDB` `S` - regulator=Fur; target=zapB; function=+
- `activates` --> [[gene.b4133|gene.b4133]] `RegulonDB` `S` - regulator=Fur; target=cadC; function=+
- `activates` --> [[gene.b4705|gene.b4705]] `RegulonDB` `S` - regulator=Fur; target=mntS; function=+
- `activates` --> [[gene.b4707|gene.b4707]] `RegulonDB` `S` - regulator=Fur; target=esrE; function=+
- `activates` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=Fur; target=sdhX; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `represses` --> [[gene.b0031|gene.b0031]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=dapB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0150|gene.b0150]] `RegulonDB` `S` - regulator=Fur; target=fhuA; function=-
- `represses` --> [[gene.b0151|gene.b0151]] `RegulonDB` `C` - regulator=Fur; target=fhuC; function=-
- `represses` --> [[gene.b0152|gene.b0152]] `RegulonDB` `C` - regulator=Fur; target=fhuD; function=-
- `represses` --> [[gene.b0156|gene.b0156]] `RegulonDB` `S` - regulator=Fur; target=erpA; function=-
- `represses` --> [[gene.b0168|gene.b0168]] `RegulonDB` `S` - regulator=Fur; target=map; function=-
- `represses` --> [[gene.b0468|gene.b0468]] `RegulonDB` `S` - regulator=Fur; target=ybaN; function=-
- `represses` --> [[gene.b0583|gene.b0583]] `RegulonDB` `C` - regulator=Fur; target=entD; function=-
- `represses` --> [[gene.b0584|gene.b0584]] `RegulonDB` `S` - regulator=Fur; target=fepA; function=-
- `represses` --> [[gene.b0585|gene.b0585]] `RegulonDB` `C` - regulator=Fur; target=fes; function=-
- `represses` --> [[gene.b0586|gene.b0586]] `RegulonDB` `C` - regulator=Fur; target=entF; function=-
- `represses` --> [[gene.b0587|gene.b0587]] `RegulonDB` `C` - regulator=Fur; target=fepE; function=-
- `represses` --> [[gene.b0588|gene.b0588]] `RegulonDB` `C` - regulator=Fur; target=fepC; function=-
- `represses` --> [[gene.b0589|gene.b0589]] `RegulonDB` `C` - regulator=Fur; target=fepG; function=-
- `represses` --> [[gene.b0590|gene.b0590]] `RegulonDB` `C` - regulator=Fur; target=fepD; function=-
- `represses` --> [[gene.b0591|gene.b0591]] `RegulonDB` `C` - regulator=Fur; target=entS; function=-+
- `represses` --> [[gene.b0592|gene.b0592]] `RegulonDB` `C` - regulator=Fur; target=fepB; function=-
- `represses` --> [[gene.b0593|gene.b0593]] `RegulonDB` `C` - regulator=Fur; target=entC; function=-
- `represses` --> [[gene.b0594|gene.b0594]] `RegulonDB` `C` - regulator=Fur; target=entE; function=-
- `represses` --> [[gene.b0595|gene.b0595]] `RegulonDB` `S` - regulator=Fur; target=entB; function=-
- `represses` --> [[gene.b0596|gene.b0596]] `RegulonDB` `S` - regulator=Fur; target=entA; function=-
- `represses` --> [[gene.b0683|gene.b0683]] `RegulonDB` `S` - regulator=Fur; target=fur; function=-
- `represses` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=Fur; target=sdhC; function=-+
- `represses` --> [[gene.b0722|gene.b0722]] `RegulonDB` `S` - regulator=Fur; target=sdhD; function=-+
- `represses` --> [[gene.b0723|gene.b0723]] `RegulonDB` `S` - regulator=Fur; target=sdhA; function=-+
- `represses` --> [[gene.b0755|gene.b0755]] `RegulonDB` `C` - regulator=Fur; target=gpmA; function=-
- `represses` --> [[gene.b0781|gene.b0781]] `RegulonDB` `S` - regulator=Fur; target=moaA; function=-
- `represses` --> [[gene.b0804|gene.b0804]] `RegulonDB` `S` - regulator=Fur; target=ybiX; function=-
- `represses` --> [[gene.b0805|gene.b0805]] `RegulonDB` `S` - regulator=Fur; target=fiu; function=-
- `represses` --> [[gene.b0958|gene.b0958]] `RegulonDB` `S` - regulator=Fur; target=sulA; function=-
- `represses` --> [[gene.b1018|gene.b1018]] `RegulonDB` `S` - regulator=Fur; target=efeO; function=-
- `represses` --> [[gene.b1019|gene.b1019]] `RegulonDB` `S` - regulator=Fur; target=efeB; function=-
- `represses` --> [[gene.b1020|gene.b1020]] `RegulonDB` `S` - regulator=Fur; target=phoH; function=-
- `represses` --> [[gene.b1062|gene.b1062]] `RegulonDB` `S` - regulator=Fur; target=pyrC; function=-
- `represses` --> [[gene.b1102|gene.b1102]] `RegulonDB` `S` - regulator=Fur; target=fhuE; function=-
- `represses` --> [[gene.b1243|gene.b1243]] `RegulonDB` `S` - regulator=Fur; target=oppA; function=-
- `represses` --> [[gene.b1244|gene.b1244]] `RegulonDB` `S` - regulator=Fur; target=oppB; function=-
- `represses` --> [[gene.b1245|gene.b1245]] `RegulonDB` `S` - regulator=Fur; target=oppC; function=-
- `represses` --> [[gene.b1246|gene.b1246]] `RegulonDB` `S` - regulator=Fur; target=oppD; function=-
- `represses` --> [[gene.b1247|gene.b1247]] `RegulonDB` `S` - regulator=Fur; target=oppF; function=-+
- `represses` --> [[gene.b1251|gene.b1251]] `RegulonDB` `C` - regulator=Fur; target=yciI; function=-
- `represses` --> [[gene.b1252|gene.b1252]] `RegulonDB` `S` - regulator=Fur; target=tonB; function=-+
- `represses` --> [[gene.b1414|gene.b1414]] `RegulonDB` `S` - regulator=Fur; target=ydcF; function=-
- `represses` --> [[gene.b1445|gene.b1445]] `RegulonDB` `S` - regulator=Fur; target=ortT; function=-
- `represses` --> [[gene.b1451|gene.b1451]] `RegulonDB` `S` - regulator=Fur; target=pqqU; function=-
- `represses` --> [[gene.b1452|gene.b1452]] `RegulonDB` `S` - regulator=Fur; target=yncE; function=-
- `represses` --> [[gene.b1478|gene.b1478]] `RegulonDB` `S` - regulator=Fur; target=adhP; function=-
- `represses` --> [[gene.b1495|gene.b1495]] `RegulonDB` `S` - regulator=Fur; target=yddB; function=-
- `represses` --> [[gene.b1496|gene.b1496]] `RegulonDB` `S` - regulator=Fur; target=yddA; function=-
- `represses` --> [[gene.b1498|gene.b1498]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=ydeN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1533|gene.b1533]] `RegulonDB` `S` - regulator=Fur; target=eamA; function=-
- `represses` --> [[gene.b1546|gene.b1546]] `RegulonDB` `S` - regulator=Fur; target=tfaQ; function=-
- `represses` --> [[gene.b1547|gene.b1547]] `RegulonDB` `C` - regulator=Fur; target=stfQ; function=-
- `represses` --> [[gene.b1548|gene.b1548]] `RegulonDB` `C` - regulator=Fur; target=nohA; function=-
- `represses` --> [[gene.b1633|gene.b1633]] `RegulonDB` `S` - regulator=Fur; target=nth; function=-
- `represses` --> [[gene.b1679|gene.b1679]] `RegulonDB` `C` - regulator=Fur; target=sufE; function=-
- `represses` --> [[gene.b1680|gene.b1680]] `RegulonDB` `C` - regulator=Fur; target=sufS; function=-
- `represses` --> [[gene.b1681|gene.b1681]] `RegulonDB` `C` - regulator=Fur; target=sufD; function=-
- `represses` --> [[gene.b1682|gene.b1682]] `RegulonDB` `C` - regulator=Fur; target=sufC; function=-
- `represses` --> [[gene.b1683|gene.b1683]] `RegulonDB` `C` - regulator=Fur; target=sufB; function=-
- `represses` --> [[gene.b1684|gene.b1684]] `RegulonDB` `C` - regulator=Fur; target=sufA; function=-
- `represses` --> [[gene.b1705|gene.b1705]] `RegulonDB` `S` - regulator=Fur; target=ydiE; function=-
- `represses` --> [[gene.b1706|gene.b1706]] `RegulonDB` `S` - regulator=Fur; target=selO; function=-
- `represses` --> [[gene.b2155|gene.b2155]] `RegulonDB` `C` - regulator=Fur; target=cirA; function=-
- `represses` --> [[gene.b2156|gene.b2156]] `RegulonDB` `S` - regulator=Fur; target=lysP; function=-
- `represses` --> [[gene.b2181|gene.b2181]] `RegulonDB` `S` - regulator=Fur; target=yejG; function=-
- `represses` --> [[gene.b2210|gene.b2210]] `RegulonDB` `S` - regulator=Fur; target=mqo; function=-
- `represses` --> [[gene.b2211|gene.b2211]] `RegulonDB` `S` - regulator=Fur; target=yojI; function=-
- `represses` --> [[gene.b2392|gene.b2392]] `RegulonDB` `S` - regulator=Fur; target=mntH; function=-
- `represses` --> [[gene.b2463|gene.b2463]] `RegulonDB` `S` - regulator=Fur; target=maeB; function=-
- `represses` --> [[gene.b2537|gene.b2537]] `RegulonDB` `S` - regulator=Fur; target=hcaR; function=-
- `represses` --> [[gene.b2616|gene.b2616]] `RegulonDB` `S` - regulator=Fur; target=recN; function=-
- `represses` --> [[gene.b2671|gene.b2671]] `RegulonDB` `S` - regulator=Fur; target=ygaC; function=-
- `represses` --> [[gene.b2673|gene.b2673]] `RegulonDB` `S` - regulator=Fur; target=nrdH; function=-
- `represses` --> [[gene.b2674|gene.b2674]] `RegulonDB` `S` - regulator=Fur; target=nrdI; function=-
- `represses` --> [[gene.b2675|gene.b2675]] `RegulonDB` `S` - regulator=Fur; target=nrdE; function=-
- `represses` --> [[gene.b2676|gene.b2676]] `RegulonDB` `S` - regulator=Fur; target=nrdF; function=-
- `represses` --> [[gene.b3005|gene.b3005]] `RegulonDB` `S` - regulator=Fur; target=exbD; function=-
- `represses` --> [[gene.b3006|gene.b3006]] `RegulonDB` `C` - regulator=Fur; target=exbB; function=-
- `represses` --> [[gene.b3070|gene.b3070]] `RegulonDB` `S` - regulator=Fur; target=nfeF; function=-
- `represses` --> [[gene.b3071|gene.b3071]] `RegulonDB` `S` - regulator=Fur; target=nfeR; function=-
- `represses` --> [[gene.b3123|gene.b3123]] `RegulonDB` `S` - regulator=Fur; target=rnpB; function=-
- `represses` --> [[gene.b3124|gene.b3124]] `RegulonDB` `S` - regulator=Fur; target=garK; function=-
- `represses` --> [[gene.b3125|gene.b3125]] `RegulonDB` `S` - regulator=Fur; target=garR; function=-
- `represses` --> [[gene.b3126|gene.b3126]] `RegulonDB` `S` - regulator=Fur; target=garL; function=-
- `represses` --> [[gene.b3127|gene.b3127]] `RegulonDB` `S` - regulator=Fur; target=garP; function=-
- `represses` --> [[gene.b3172|gene.b3172]] `RegulonDB` `S` - regulator=Fur; target=argG; function=-
- `represses` --> [[gene.b3207|gene.b3207]] `RegulonDB` `S` - regulator=Fur; target=yrbL; function=-
- `represses` --> [[gene.b3236|gene.b3236]] `RegulonDB` `S` - regulator=Fur; target=mdh; function=-
- `represses` --> [[gene.b3237|gene.b3237]] `RegulonDB` `S` - regulator=Fur; target=argR; function=-
- `represses` --> [[gene.b3324|gene.b3324]] `RegulonDB` `S` - regulator=Fur; target=gspC; function=-
- `represses` --> [[gene.b3325|gene.b3325]] `RegulonDB` `S` - regulator=Fur; target=gspD; function=-
- `represses` --> [[gene.b3326|gene.b3326]] `RegulonDB` `S` - regulator=Fur; target=gspE; function=-
- `represses` --> [[gene.b3327|gene.b3327]] `RegulonDB` `S` - regulator=Fur; target=gspF; function=-
- `represses` --> [[gene.b3328|gene.b3328]] `RegulonDB` `S` - regulator=Fur; target=gspG; function=-
- `represses` --> [[gene.b3329|gene.b3329]] `RegulonDB` `S` - regulator=Fur; target=gspH; function=-
- `represses` --> [[gene.b3330|gene.b3330]] `RegulonDB` `S` - regulator=Fur; target=gspI; function=-
- `represses` --> [[gene.b3331|gene.b3331]] `RegulonDB` `S` - regulator=Fur; target=gspJ; function=-
- `represses` --> [[gene.b3332|gene.b3332]] `RegulonDB` `S` - regulator=Fur; target=gspK; function=-
- `represses` --> [[gene.b3333|gene.b3333]] `RegulonDB` `S` - regulator=Fur; target=gspL; function=-
- `represses` --> [[gene.b3334|gene.b3334]] `RegulonDB` `S` - regulator=Fur; target=gspM; function=-
- `represses` --> [[gene.b3335|gene.b3335]] `RegulonDB` `S` - regulator=Fur; target=gspO; function=-
- `represses` --> [[gene.b3337|gene.b3337]] `RegulonDB` `S` - regulator=Fur; target=bfd; function=-
- `represses` --> [[gene.b3408|gene.b3408]] `RegulonDB` `S` - regulator=Fur; target=feoA; function=-
- `represses` --> [[gene.b3409|gene.b3409]] `RegulonDB` `S` - regulator=Fur; target=feoB; function=-
- `represses` --> [[gene.b3410|gene.b3410]] `RegulonDB` `S` - regulator=Fur; target=feoC; function=-
- `represses` --> [[gene.b3451|gene.b3451]] `RegulonDB` `S` - regulator=Fur; target=ugpE; function=-
- `represses` --> [[gene.b3710|gene.b3710]] `RegulonDB` `S` - regulator=Fur; target=mdtL; function=-
- `represses` --> [[gene.b3908|gene.b3908]] `RegulonDB` `C` - regulator=Fur; target=sodA; function=-
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=Fur; target=rsd; function=-
- `represses` --> [[gene.b4287|gene.b4287]] `RegulonDB` `C` - regulator=Fur; target=fecE; function=-
- `represses` --> [[gene.b4288|gene.b4288]] `RegulonDB` `C` - regulator=Fur; target=fecD; function=-
- `represses` --> [[gene.b4289|gene.b4289]] `RegulonDB` `C` - regulator=Fur; target=fecC; function=-
- `represses` --> [[gene.b4290|gene.b4290]] `RegulonDB` `C` - regulator=Fur; target=fecB; function=-
- `represses` --> [[gene.b4291|gene.b4291]] `RegulonDB` `C` - regulator=Fur; target=fecA; function=-
- `represses` --> [[gene.b4292|gene.b4292]] `RegulonDB` `C` - regulator=Fur; target=fecR; function=-
- `represses` --> [[gene.b4293|gene.b4293]] `RegulonDB` `C` - regulator=Fur; target=fecI; function=-
- `represses` --> [[gene.b4340|gene.b4340]] `RegulonDB` `S` - regulator=Fur; target=yjiR; function=-
- `represses` --> [[gene.b4367|gene.b4367]] `RegulonDB` `C` - regulator=Fur; target=fhuF; function=-
- `represses` --> [[gene.b4451|gene.b4451]] `RegulonDB` `C` - regulator=Fur; target=ryhB; function=-
- `represses` --> [[gene.b4511|gene.b4511]] `RegulonDB` `C` - regulator=Fur; target=ybdZ; function=-
- `represses` --> [[gene.b4567|gene.b4567]] `RegulonDB` `S` - regulator=Fur; target=yjjZ; function=-
- `represses` --> [[gene.b4618|gene.b4618]] `RegulonDB` `S` - regulator=Fur; target=tisB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0683|gene.b0683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9A9`
- `KEGG:ecj:JW0669;eco:b0683;ecoc:C3026_03395;`
- `GeneID:89519983;93776802;945295;`
- `GO:GO:0000166; GO:0000976; GO:0001216; GO:0001217; GO:0003700; GO:0005829; GO:0008270; GO:0032993; GO:0043565; GO:0045892; GO:0045893; GO:1900705`

## Notes

Ferric uptake regulation protein (Ferric uptake regulator)
