---
entity_id: "protein.P0A9E5"
entity_type: "protein"
name: "fnr"
source_database: "UniProt"
source_id: "P0A9E5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fnr nirR b1334 JW1328"
---

# fnr

`protein.P0A9E5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9E5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Global transcription factor that controls the expression of over 100 target genes in response to anoxia. It facilitates the adaptation to anaerobic growth conditions by regulating the expression of gene products that are involved in anaerobic energy metabolism. When the terminal electron acceptor, O(2), is no longer available, it represses the synthesis of enzymes involved in aerobic respiration and increases the synthesis of enzymes required for anaerobic respiration.

## Biological Role

Component of DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797).

## Annotation

FUNCTION: Global transcription factor that controls the expression of over 100 target genes in response to anoxia. It facilitates the adaptation to anaerobic growth conditions by regulating the expression of gene products that are involved in anaerobic energy metabolism. When the terminal electron acceptor, O(2), is no longer available, it represses the synthesis of enzymes involved in aerobic respiration and increases the synthesis of enzymes required for anaerobic respiration.

## Outgoing Edges (165)

- `activates` --> [[gene.b0002|gene.b0002]] `RegulonDB` `S` - regulator=FNR; target=thrA; function=+
- `activates` --> [[gene.b0034|gene.b0034]] `RegulonDB` `S` - regulator=FNR; target=caiF; function=+
- `activates` --> [[gene.b0112|gene.b0112]] `RegulonDB` `S` - regulator=FNR; target=aroP; function=+
- `activates` --> [[gene.b0113|gene.b0113]] `RegulonDB` `S` - regulator=FNR; target=pdhR; function=-+
- `activates` --> [[gene.b0114|gene.b0114]] `RegulonDB` `S` - regulator=FNR; target=aceE; function=-+
- `activates` --> [[gene.b0115|gene.b0115]] `RegulonDB` `S` - regulator=FNR; target=aceF; function=-+
- `activates` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=FNR; target=lpd; function=-+
- `activates` --> [[gene.b0585|gene.b0585]] `RegulonDB` `S` - regulator=FNR; target=fes; function=+
- `activates` --> [[gene.b0586|gene.b0586]] `RegulonDB` `S` - regulator=FNR; target=entF; function=+
- `activates` --> [[gene.b0587|gene.b0587]] `RegulonDB` `S` - regulator=FNR; target=fepE; function=+
- `activates` --> [[gene.b0621|gene.b0621]] `RegulonDB` `S` - regulator=FNR; target=dcuC; function=+
- `activates` --> [[gene.b0733|gene.b0733]] `RegulonDB` `C` - regulator=FNR; target=cydA; function=-+
- `activates` --> [[gene.b0734|gene.b0734]] `RegulonDB` `C` - regulator=FNR; target=cydB; function=-+
- `activates` --> [[gene.b0781|gene.b0781]] `RegulonDB` `S` - regulator=FNR; target=moaA; function=+
- `activates` --> [[gene.b0782|gene.b0782]] `RegulonDB` `S` - regulator=FNR; target=moaB; function=+
- `activates` --> [[gene.b0783|gene.b0783]] `RegulonDB` `S` - regulator=FNR; target=moaC; function=+
- `activates` --> [[gene.b0784|gene.b0784]] `RegulonDB` `S` - regulator=FNR; target=moaD; function=+
- `activates` --> [[gene.b0785|gene.b0785]] `RegulonDB` `S` - regulator=FNR; target=moaE; function=+
- `activates` --> [[gene.b0871|gene.b0871]] `RegulonDB` `C` - regulator=FNR; target=poxB; function=+
- `activates` --> [[gene.b0872|gene.b0872]] `RegulonDB` `C` - regulator=FNR; target=hcr; function=+
- `activates` --> [[gene.b0873|gene.b0873]] `RegulonDB` `C` - regulator=FNR; target=hcp; function=+
- `activates` --> [[gene.b0894|gene.b0894]] `RegulonDB` `C` - regulator=FNR; target=dmsA; function=+
- `activates` --> [[gene.b0895|gene.b0895]] `RegulonDB` `C` - regulator=FNR; target=dmsB; function=+
- `activates` --> [[gene.b0896|gene.b0896]] `RegulonDB` `C` - regulator=FNR; target=dmsC; function=+
- `activates` --> [[gene.b0903|gene.b0903]] `RegulonDB` `S` - regulator=FNR; target=pflB; function=+
- `activates` --> [[gene.b0904|gene.b0904]] `RegulonDB` `C` - regulator=FNR; target=focA; function=+
- `activates` --> [[gene.b1182|gene.b1182]] `RegulonDB` `S` - regulator=FNR; target=hlyE; function=+
- `activates` --> [[gene.b1223|gene.b1223]] `RegulonDB` `S` - regulator=FNR; target=narK; function=+
- `activates` --> [[gene.b1224|gene.b1224]] `RegulonDB` `C` - regulator=FNR; target=narG; function=+
- `activates` --> [[gene.b1225|gene.b1225]] `RegulonDB` `C` - regulator=FNR; target=narH; function=+
- `activates` --> [[gene.b1226|gene.b1226]] `RegulonDB` `C` - regulator=FNR; target=narJ; function=+
- `activates` --> [[gene.b1227|gene.b1227]] `RegulonDB` `C` - regulator=FNR; target=narI; function=+
- `activates` --> [[gene.b1241|gene.b1241]] `RegulonDB` `S` - regulator=FNR; target=adhE; function=+
- `activates` --> [[gene.b1256|gene.b1256]] `RegulonDB` `C` - regulator=FNR; target=ompW; function=-+
- `activates` --> [[gene.b1334|gene.b1334]] `RegulonDB` `S` - regulator=FNR; target=fnr; function=-+
- `activates` --> [[gene.b1445|gene.b1445]] `RegulonDB` `S` - regulator=FNR; target=ortT; function=+
- `activates` --> [[gene.b1474|gene.b1474]] `RegulonDB` `S` - regulator=FNR; target=fdnG; function=-+
- `activates` --> [[gene.b1475|gene.b1475]] `RegulonDB` `C` - regulator=FNR; target=fdnH; function=-+
- `activates` --> [[gene.b1476|gene.b1476]] `RegulonDB` `C` - regulator=FNR; target=fdnI; function=-+
- `activates` --> [[gene.b1541|gene.b1541]] `RegulonDB` `S` - regulator=FNR; target=ydfZ; function=+
- `activates` --> [[gene.b1549|gene.b1549]] `RegulonDB` `S` - regulator=FNR; target=ydfO; function=+
- `activates` --> [[gene.b1587|gene.b1587]] `RegulonDB` `C` - regulator=FNR; target=ynfE; function=+
- `activates` --> [[gene.b1588|gene.b1588]] `RegulonDB` `C` - regulator=FNR; target=ynfF; function=+
- `activates` --> [[gene.b1589|gene.b1589]] `RegulonDB` `C` - regulator=FNR; target=ynfG; function=+
- `activates` --> [[gene.b1590|gene.b1590]] `RegulonDB` `C` - regulator=FNR; target=ynfH; function=+
- `activates` --> [[gene.b1591|gene.b1591]] `RegulonDB` `C` - regulator=FNR; target=dmsD; function=+
- `activates` --> [[gene.b1593|gene.b1593]] `RegulonDB` `S` - regulator=FNR; target=bidA; function=+
- `activates` --> [[gene.b1669|gene.b1669]] `RegulonDB` `C` - regulator=FNR; target=ydhT; function=+
- `activates` --> [[gene.b1670|gene.b1670]] `RegulonDB` `C` - regulator=FNR; target=ydhU; function=+
- `activates` --> [[gene.b1671|gene.b1671]] `RegulonDB` `C` - regulator=FNR; target=ydhX; function=+
- `activates` --> [[gene.b1672|gene.b1672]] `RegulonDB` `C` - regulator=FNR; target=ydhW; function=+
- `activates` --> [[gene.b1673|gene.b1673]] `RegulonDB` `C` - regulator=FNR; target=ydhV; function=+
- `activates` --> [[gene.b1674|gene.b1674]] `RegulonDB` `C` - regulator=FNR; target=ydhY; function=+
- `activates` --> [[gene.b1854|gene.b1854]] `RegulonDB` `S` - regulator=FNR; target=pykA; function=+
- `activates` --> [[gene.b2194|gene.b2194]] `RegulonDB` `C` - regulator=FNR; target=ccmH; function=+
- `activates` --> [[gene.b2195|gene.b2195]] `RegulonDB` `C` - regulator=FNR; target=ccmG; function=+
- `activates` --> [[gene.b2196|gene.b2196]] `RegulonDB` `C` - regulator=FNR; target=ccmF; function=+
- `activates` --> [[gene.b2197|gene.b2197]] `RegulonDB` `C` - regulator=FNR; target=ccmE; function=+
- `activates` --> [[gene.b2198|gene.b2198]] `RegulonDB` `C` - regulator=FNR; target=ccmD; function=+
- `activates` --> [[gene.b2199|gene.b2199]] `RegulonDB` `C` - regulator=FNR; target=ccmC; function=+
- `activates` --> [[gene.b2200|gene.b2200]] `RegulonDB` `C` - regulator=FNR; target=ccmB; function=+
- `activates` --> [[gene.b2201|gene.b2201]] `RegulonDB` `C` - regulator=FNR; target=ccmA; function=+
- `activates` --> [[gene.b2202|gene.b2202]] `RegulonDB` `C` - regulator=FNR; target=napC; function=+
- `activates` --> [[gene.b2203|gene.b2203]] `RegulonDB` `C` - regulator=FNR; target=napB; function=+
- `activates` --> [[gene.b2204|gene.b2204]] `RegulonDB` `C` - regulator=FNR; target=napH; function=+
- `activates` --> [[gene.b2205|gene.b2205]] `RegulonDB` `C` - regulator=FNR; target=napG; function=+
- `activates` --> [[gene.b2206|gene.b2206]] `RegulonDB` `C` - regulator=FNR; target=napA; function=+
- `activates` --> [[gene.b2207|gene.b2207]] `RegulonDB` `C` - regulator=FNR; target=napD; function=+
- `activates` --> [[gene.b2208|gene.b2208]] `RegulonDB` `C` - regulator=FNR; target=napF; function=+
- `activates` --> [[gene.b2343|gene.b2343]] `RegulonDB` `S` - regulator=FNR; target=yfcZ; function=+
- `activates` --> [[gene.b2450|gene.b2450]] `RegulonDB` `S` - regulator=FNR; target=yffS; function=+
- `activates` --> [[gene.b2497|gene.b2497]] `RegulonDB` `S` - regulator=FNR; target=uraA; function=+
- `activates` --> [[gene.b2498|gene.b2498]] `RegulonDB` `S` - regulator=FNR; target=upp; function=+
- `activates` --> [[gene.b2503|gene.b2503]] `RegulonDB` `C` - regulator=FNR; target=pdeF; function=+
- `activates` --> [[gene.b2579|gene.b2579]] `RegulonDB` `C` - regulator=FNR; target=grcA; function=-+
- `activates` --> [[gene.b2580|gene.b2580]] `RegulonDB` `S` - regulator=FNR; target=ung; function=+
- `activates` --> [[gene.b2727|gene.b2727]] `RegulonDB` `S` - regulator=FNR; target=hypB; function=+
- `activates` --> [[gene.b2728|gene.b2728]] `RegulonDB` `S` - regulator=FNR; target=hypC; function=+
- `activates` --> [[gene.b2729|gene.b2729]] `RegulonDB` `S` - regulator=FNR; target=hypD; function=+
- `activates` --> [[gene.b2730|gene.b2730]] `RegulonDB` `S` - regulator=FNR; target=hypE; function=+
- `activates` --> [[gene.b2731|gene.b2731]] `RegulonDB` `S` - regulator=FNR; target=fhlA; function=+
- `activates` --> [[gene.b2813|gene.b2813]] `RegulonDB` `S` - regulator=FNR; target=mltA; function=+
- `activates` --> [[gene.b2816|gene.b2816]] `RegulonDB` `S` - regulator=FNR; target=metV; function=+
- `activates` --> [[gene.b2957|gene.b2957]] `RegulonDB` `S` - regulator=FNR; target=ansB; function=+
- `activates` --> [[gene.b3072|gene.b3072]] `RegulonDB` `S` - regulator=FNR; target=aer; function=+
- `activates` --> [[gene.b3128|gene.b3128]] `RegulonDB` `S` - regulator=FNR; target=garD; function=+
- `activates` --> [[gene.b3365|gene.b3365]] `RegulonDB` `C` - regulator=FNR; target=nirB; function=+
- `activates` --> [[gene.b3366|gene.b3366]] `RegulonDB` `C` - regulator=FNR; target=nirD; function=+
- `activates` --> [[gene.b3367|gene.b3367]] `RegulonDB` `C` - regulator=FNR; target=nirC; function=+
- `activates` --> [[gene.b3368|gene.b3368]] `RegulonDB` `C` - regulator=FNR; target=cysG; function=+
- `activates` --> [[gene.b3408|gene.b3408]] `RegulonDB` `S` - regulator=FNR; target=feoA; function=+
- `activates` --> [[gene.b3409|gene.b3409]] `RegulonDB` `S` - regulator=FNR; target=feoB; function=+
- `activates` --> [[gene.b3410|gene.b3410]] `RegulonDB` `S` - regulator=FNR; target=feoC; function=+
- `activates` --> [[gene.b3476|gene.b3476]] `RegulonDB` `C` - regulator=FNR; target=nikA; function=+
- `activates` --> [[gene.b3477|gene.b3477]] `RegulonDB` `C` - regulator=FNR; target=nikB; function=+
- `activates` --> [[gene.b3478|gene.b3478]] `RegulonDB` `C` - regulator=FNR; target=nikC; function=+
- `activates` --> [[gene.b3479|gene.b3479]] `RegulonDB` `C` - regulator=FNR; target=nikD; function=+
- `activates` --> [[gene.b3480|gene.b3480]] `RegulonDB` `C` - regulator=FNR; target=nikE; function=+
- `activates` --> [[gene.b3481|gene.b3481]] `RegulonDB` `C` - regulator=FNR; target=nikR; function=+
- `activates` --> [[gene.b3518|gene.b3518]] `RegulonDB` `S` - regulator=FNR; target=ccp; function=+
- `activates` --> [[gene.b3611|gene.b3611]] `RegulonDB` `S` - regulator=FNR; target=yibN; function=+
- `activates` --> [[gene.b3745|gene.b3745]] `RegulonDB` `C` - regulator=FNR; target=viaA; function=+
- `activates` --> [[gene.b3746|gene.b3746]] `RegulonDB` `C` - regulator=FNR; target=ravA; function=+
- `activates` --> [[gene.b3942|gene.b3942]] `RegulonDB` `S` - regulator=FNR; target=katG; function=+
- `activates` --> [[gene.b4070|gene.b4070]] `RegulonDB` `C` - regulator=FNR; target=nrfA; function=+
- `activates` --> [[gene.b4071|gene.b4071]] `RegulonDB` `C` - regulator=FNR; target=nrfB; function=+
- `activates` --> [[gene.b4072|gene.b4072]] `RegulonDB` `C` - regulator=FNR; target=nrfC; function=+
- `activates` --> [[gene.b4073|gene.b4073]] `RegulonDB` `C` - regulator=FNR; target=nrfD; function=+
- `activates` --> [[gene.b4074|gene.b4074]] `RegulonDB` `C` - regulator=FNR; target=nrfE; function=+
- `activates` --> [[gene.b4075|gene.b4075]] `RegulonDB` `C` - regulator=FNR; target=nrfF; function=+
- `activates` --> [[gene.b4076|gene.b4076]] `RegulonDB` `C` - regulator=FNR; target=nrfG; function=+
- `activates` --> [[gene.b4138|gene.b4138]] `RegulonDB` `S` - regulator=FNR; target=dcuA; function=+
- `activates` --> [[gene.b4139|gene.b4139]] `RegulonDB` `S` - regulator=FNR; target=aspA; function=+
- `activates` --> [[gene.b4151|gene.b4151]] `RegulonDB` `S` - regulator=FNR; target=frdD; function=+
- `activates` --> [[gene.b4152|gene.b4152]] `RegulonDB` `S` - regulator=FNR; target=frdC; function=+
- `activates` --> [[gene.b4153|gene.b4153]] `RegulonDB` `S` - regulator=FNR; target=frdB; function=+
- `activates` --> [[gene.b4154|gene.b4154]] `RegulonDB` `S` - regulator=FNR; target=frdA; function=+
- `activates` --> [[gene.b4237|gene.b4237]] `RegulonDB` `C` - regulator=FNR; target=nrdG; function=+
- `activates` --> [[gene.b4238|gene.b4238]] `RegulonDB` `C` - regulator=FNR; target=nrdD; function=+
- `activates` --> [[gene.b4401|gene.b4401]] `RegulonDB` `S` - regulator=FNR; target=arcA; function=-+
- `activates` --> [[gene.b4511|gene.b4511]] `RegulonDB` `S` - regulator=FNR; target=ybdZ; function=+
- `activates` --> [[gene.b4699|gene.b4699]] `RegulonDB` `C` - regulator=FNR; target=fnrS; function=+
- `activates` --> [[gene.b4813|gene.b4813]] `RegulonDB` `C` - regulator=FNR; target=narS; function=+
- `activates` --> [[gene.b4825|gene.b4825]] `RegulonDB` `S` - regulator=FNR; target=aspX; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0113|gene.b0113]] `RegulonDB` `S` - regulator=FNR; target=pdhR; function=-+
- `represses` --> [[gene.b0114|gene.b0114]] `RegulonDB` `S` - regulator=FNR; target=aceE; function=-+
- `represses` --> [[gene.b0115|gene.b0115]] `RegulonDB` `S` - regulator=FNR; target=aceF; function=-+
- `represses` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=FNR; target=lpd; function=-+
- `represses` --> [[gene.b0733|gene.b0733]] `RegulonDB` `C` - regulator=FNR; target=cydA; function=-+
- `represses` --> [[gene.b0734|gene.b0734]] `RegulonDB` `C` - regulator=FNR; target=cydB; function=-+
- `represses` --> [[gene.b0826|gene.b0826]] `RegulonDB` `S` - regulator=FNR; target=moeB; function=-
- `represses` --> [[gene.b0827|gene.b0827]] `RegulonDB` `S` - regulator=FNR; target=moeA; function=-
- `represses` --> [[gene.b1109|gene.b1109]] `RegulonDB` `C` - regulator=FNR; target=ndh; function=-
- `represses` --> [[gene.b1210|gene.b1210]] `RegulonDB` `S` - regulator=FNR; target=hemA; function=-
- `represses` --> [[gene.b1211|gene.b1211]] `RegulonDB` `S` - regulator=FNR; target=prfA; function=-
- `represses` --> [[gene.b1212|gene.b1212]] `RegulonDB` `S` - regulator=FNR; target=prmC; function=-
- `represses` --> [[gene.b1222|gene.b1222]] `RegulonDB` `S` - regulator=FNR; target=narX; function=-
- `represses` --> [[gene.b1256|gene.b1256]] `RegulonDB` `C` - regulator=FNR; target=ompW; function=-+
- `represses` --> [[gene.b1334|gene.b1334]] `RegulonDB` `S` - regulator=FNR; target=fnr; function=-+
- `represses` --> [[gene.b1474|gene.b1474]] `RegulonDB` `S` - regulator=FNR; target=fdnG; function=-+
- `represses` --> [[gene.b1475|gene.b1475]] `RegulonDB` `C` - regulator=FNR; target=fdnH; function=-+
- `represses` --> [[gene.b1476|gene.b1476]] `RegulonDB` `C` - regulator=FNR; target=fdnI; function=-+
- `represses` --> [[gene.b1778|gene.b1778]] `RegulonDB` `S` - regulator=FNR; target=msrB; function=-
- `represses` --> [[gene.b2276|gene.b2276]] `RegulonDB` `S` - regulator=FNR; target=nuoN; function=-
- `represses` --> [[gene.b2277|gene.b2277]] `RegulonDB` `S` - regulator=FNR; target=nuoM; function=-
- `represses` --> [[gene.b2278|gene.b2278]] `RegulonDB` `S` - regulator=FNR; target=nuoL; function=-
- `represses` --> [[gene.b2279|gene.b2279]] `RegulonDB` `S` - regulator=FNR; target=nuoK; function=-
- `represses` --> [[gene.b2280|gene.b2280]] `RegulonDB` `S` - regulator=FNR; target=nuoJ; function=-
- `represses` --> [[gene.b2281|gene.b2281]] `RegulonDB` `S` - regulator=FNR; target=nuoI; function=-
- `represses` --> [[gene.b2282|gene.b2282]] `RegulonDB` `S` - regulator=FNR; target=nuoH; function=-
- `represses` --> [[gene.b2283|gene.b2283]] `RegulonDB` `S` - regulator=FNR; target=nuoG; function=-
- `represses` --> [[gene.b2284|gene.b2284]] `RegulonDB` `S` - regulator=FNR; target=nuoF; function=-
- `represses` --> [[gene.b2285|gene.b2285]] `RegulonDB` `S` - regulator=FNR; target=nuoE; function=-
- `represses` --> [[gene.b2286|gene.b2286]] `RegulonDB` `S` - regulator=FNR; target=nuoC; function=-
- `represses` --> [[gene.b2287|gene.b2287]] `RegulonDB` `S` - regulator=FNR; target=nuoB; function=-
- `represses` --> [[gene.b2288|gene.b2288]] `RegulonDB` `S` - regulator=FNR; target=nuoA; function=-
- `represses` --> [[gene.b2499|gene.b2499]] `RegulonDB` `C` - regulator=FNR; target=purM; function=-
- `represses` --> [[gene.b2500|gene.b2500]] `RegulonDB` `C` - regulator=FNR; target=purN; function=-
- `represses` --> [[gene.b2552|gene.b2552]] `RegulonDB` `C` - regulator=FNR; target=hmp; function=-
- `represses` --> [[gene.b2579|gene.b2579]] `RegulonDB` `C` - regulator=FNR; target=grcA; function=-+
- `represses` --> [[gene.b3212|gene.b3212]] `RegulonDB` `S` - regulator=FNR; target=gltB; function=-
- `represses` --> [[gene.b3213|gene.b3213]] `RegulonDB` `S` - regulator=FNR; target=gltD; function=-
- `represses` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - regulator=FNR; target=gltF; function=-
- `represses` --> [[gene.b4401|gene.b4401]] `RegulonDB` `S` - regulator=FNR; target=arcA; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b1334|gene.b1334]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9E5`
- `KEGG:ecj:JW1328;eco:b1334;ecoc:C3026_07810;`
- `GeneID:86859858;93775469;945908;`
- `GO:GO:0000976; GO:0001216; GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0009061; GO:0032993; GO:0045893; GO:0046872; GO:0051536; GO:0051539; GO:0071731`

## Notes

Fumarate and nitrate reduction regulatory protein
