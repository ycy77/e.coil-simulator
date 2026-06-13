---
entity_id: "protein.P0AF28"
entity_type: "protein"
name: "narL"
source_database: "UniProt"
source_id: "P0AF28"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narL frdR b1221 JW1212"
---

# narL

`protein.P0AF28`

## Static

- Type: `protein`
- Source: `UniProt:P0AF28`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins. NarL, "nitrate/nitrite response regulator NarL," is a transcriptional dual regulator of many anaerobic electron transport and fermentation-related genes in the response to the availability of high concentrations of nitrate or nitrite . NarL activates expression of 51 operons in response to nitrate, mostly genes needed for nitrate respiration. NarL represses 41 operons involved in alternative respiratory pathways, such as fumarate reduction or fermentation of simple sugars . The response regulator NarL belongs to the LuxR/UhpA family and is part of the two-component system NarX-NarL. There is intensive cross-regulation with the paralogous two-component system NarQ-NarP . Each of the sensors, NarX and NarQ, is able to phosphorylate NarL and NarP, leading to the activation of both proteins. In the absence of nitrate and nitrite, NarX and NarQ stimulate the dephosphorylation of NarL-P and NarP-P . This reaction is specific, that is, NarL-P is only desphosphorylated by NarX. The system discriminates between nitrate and nitrite...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (72)

- `activates` --> [[gene.b0871|gene.b0871]] `RegulonDB` `S` - regulator=NarL; target=poxB; function=+
- `activates` --> [[gene.b0872|gene.b0872]] `RegulonDB` `S` - regulator=NarL; target=hcr; function=+
- `activates` --> [[gene.b0873|gene.b0873]] `RegulonDB` `S` - regulator=NarL; target=hcp; function=+
- `activates` --> [[gene.b1223|gene.b1223]] `RegulonDB` `S` - regulator=NarL; target=narK; function=+
- `activates` --> [[gene.b1224|gene.b1224]] `RegulonDB` `S` - regulator=NarL; target=narG; function=+
- `activates` --> [[gene.b1225|gene.b1225]] `RegulonDB` `S` - regulator=NarL; target=narH; function=+
- `activates` --> [[gene.b1226|gene.b1226]] `RegulonDB` `C` - regulator=NarL; target=narJ; function=+
- `activates` --> [[gene.b1227|gene.b1227]] `RegulonDB` `C` - regulator=NarL; target=narI; function=+
- `activates` --> [[gene.b1335|gene.b1335]] `RegulonDB` `C` - regulator=NarL; target=ogt; function=+
- `activates` --> [[gene.b1474|gene.b1474]] `RegulonDB` `S` - regulator=NarL; target=fdnG; function=+
- `activates` --> [[gene.b1475|gene.b1475]] `RegulonDB` `C` - regulator=NarL; target=fdnH; function=+
- `activates` --> [[gene.b1476|gene.b1476]] `RegulonDB` `S` - regulator=NarL; target=fdnI; function=+
- `activates` --> [[gene.b1501|gene.b1501]] `RegulonDB` `S` - regulator=NarL; target=ydeP; function=+
- `activates` --> [[gene.b1796|gene.b1796]] `RegulonDB` `S` - regulator=NarL; target=yoaG; function=+
- `activates` --> [[gene.b1797|gene.b1797]] `RegulonDB` `S` - regulator=NarL; target=yeaR; function=+
- `activates` --> [[gene.b3365|gene.b3365]] `RegulonDB` `C` - regulator=NarL; target=nirB; function=+
- `activates` --> [[gene.b3366|gene.b3366]] `RegulonDB` `C` - regulator=NarL; target=nirD; function=+
- `activates` --> [[gene.b3367|gene.b3367]] `RegulonDB` `C` - regulator=NarL; target=nirC; function=+
- `activates` --> [[gene.b3368|gene.b3368]] `RegulonDB` `C` - regulator=NarL; target=cysG; function=+
- `activates` --> [[gene.b4070|gene.b4070]] `RegulonDB` `C` - regulator=NarL; target=nrfA; function=-+
- `activates` --> [[gene.b4071|gene.b4071]] `RegulonDB` `C` - regulator=NarL; target=nrfB; function=-+
- `activates` --> [[gene.b4072|gene.b4072]] `RegulonDB` `C` - regulator=NarL; target=nrfC; function=-+
- `activates` --> [[gene.b4073|gene.b4073]] `RegulonDB` `C` - regulator=NarL; target=nrfD; function=-+
- `activates` --> [[gene.b4074|gene.b4074]] `RegulonDB` `C` - regulator=NarL; target=nrfE; function=-+
- `activates` --> [[gene.b4075|gene.b4075]] `RegulonDB` `C` - regulator=NarL; target=nrfF; function=-+
- `activates` --> [[gene.b4076|gene.b4076]] `RegulonDB` `C` - regulator=NarL; target=nrfG; function=-+
- `activates` --> [[gene.b4813|gene.b4813]] `RegulonDB` `S` - regulator=NarL; target=narS; function=+
- `represses` --> [[gene.b0894|gene.b0894]] `RegulonDB` `S` - regulator=NarL; target=dmsA; function=-
- `represses` --> [[gene.b0895|gene.b0895]] `RegulonDB` `S` - regulator=NarL; target=dmsB; function=-
- `represses` --> [[gene.b0896|gene.b0896]] `RegulonDB` `S` - regulator=NarL; target=dmsC; function=-
- `represses` --> [[gene.b0903|gene.b0903]] `RegulonDB` `S` - regulator=NarL; target=pflB; function=-
- `represses` --> [[gene.b0904|gene.b0904]] `RegulonDB` `S` - regulator=NarL; target=focA; function=-
- `represses` --> [[gene.b1256|gene.b1256]] `RegulonDB` `S` - regulator=NarL; target=ompW; function=-
- `represses` --> [[gene.b1587|gene.b1587]] `RegulonDB` `S` - regulator=NarL; target=ynfE; function=-
- `represses` --> [[gene.b1588|gene.b1588]] `RegulonDB` `S` - regulator=NarL; target=ynfF; function=-
- `represses` --> [[gene.b1589|gene.b1589]] `RegulonDB` `S` - regulator=NarL; target=ynfG; function=-
- `represses` --> [[gene.b1590|gene.b1590]] `RegulonDB` `S` - regulator=NarL; target=ynfH; function=-
- `represses` --> [[gene.b1591|gene.b1591]] `RegulonDB` `S` - regulator=NarL; target=dmsD; function=-
- `represses` --> [[gene.b1670|gene.b1670]] `RegulonDB` `C` - regulator=NarL; target=ydhU; function=-
- `represses` --> [[gene.b1673|gene.b1673]] `RegulonDB` `C` - regulator=NarL; target=ydhV; function=-
- `represses` --> [[gene.b2194|gene.b2194]] `RegulonDB` `S` - regulator=NarL; target=ccmH; function=-
- `represses` --> [[gene.b2195|gene.b2195]] `RegulonDB` `S` - regulator=NarL; target=ccmG; function=-
- `represses` --> [[gene.b2196|gene.b2196]] `RegulonDB` `S` - regulator=NarL; target=ccmF; function=-
- `represses` --> [[gene.b2197|gene.b2197]] `RegulonDB` `S` - regulator=NarL; target=ccmE; function=-
- `represses` --> [[gene.b2198|gene.b2198]] `RegulonDB` `S` - regulator=NarL; target=ccmD; function=-
- `represses` --> [[gene.b2199|gene.b2199]] `RegulonDB` `S` - regulator=NarL; target=ccmC; function=-
- `represses` --> [[gene.b2200|gene.b2200]] `RegulonDB` `S` - regulator=NarL; target=ccmB; function=-
- `represses` --> [[gene.b2201|gene.b2201]] `RegulonDB` `S` - regulator=NarL; target=ccmA; function=-
- `represses` --> [[gene.b2202|gene.b2202]] `RegulonDB` `S` - regulator=NarL; target=napC; function=-
- `represses` --> [[gene.b2203|gene.b2203]] `RegulonDB` `S` - regulator=NarL; target=napB; function=-
- `represses` --> [[gene.b2204|gene.b2204]] `RegulonDB` `S` - regulator=NarL; target=napH; function=-
- `represses` --> [[gene.b2205|gene.b2205]] `RegulonDB` `S` - regulator=NarL; target=napG; function=-
- `represses` --> [[gene.b2206|gene.b2206]] `RegulonDB` `S` - regulator=NarL; target=napA; function=-
- `represses` --> [[gene.b2207|gene.b2207]] `RegulonDB` `S` - regulator=NarL; target=napD; function=-
- `represses` --> [[gene.b2208|gene.b2208]] `RegulonDB` `S` - regulator=NarL; target=napF; function=-
- `represses` --> [[gene.b4070|gene.b4070]] `RegulonDB` `C` - regulator=NarL; target=nrfA; function=-+
- `represses` --> [[gene.b4071|gene.b4071]] `RegulonDB` `C` - regulator=NarL; target=nrfB; function=-+
- `represses` --> [[gene.b4072|gene.b4072]] `RegulonDB` `C` - regulator=NarL; target=nrfC; function=-+
- `represses` --> [[gene.b4073|gene.b4073]] `RegulonDB` `C` - regulator=NarL; target=nrfD; function=-+
- `represses` --> [[gene.b4074|gene.b4074]] `RegulonDB` `C` - regulator=NarL; target=nrfE; function=-+
- `represses` --> [[gene.b4075|gene.b4075]] `RegulonDB` `C` - regulator=NarL; target=nrfF; function=-+
- `represses` --> [[gene.b4076|gene.b4076]] `RegulonDB` `C` - regulator=NarL; target=nrfG; function=-+
- `represses` --> [[gene.b4079|gene.b4079]] `RegulonDB` `S` - regulator=NarL; target=fdhF; function=-
- `represses` --> [[gene.b4124|gene.b4124]] `RegulonDB` `S` - regulator=NarL; target=dcuR; function=-
- `represses` --> [[gene.b4125|gene.b4125]] `RegulonDB` `S` - regulator=NarL; target=dcuS; function=-
- `represses` --> [[gene.b4138|gene.b4138]] `RegulonDB` `S` - regulator=NarL; target=dcuA; function=-
- `represses` --> [[gene.b4139|gene.b4139]] `RegulonDB` `S` - regulator=NarL; target=aspA; function=-
- `represses` --> [[gene.b4151|gene.b4151]] `RegulonDB` `S` - regulator=NarL; target=frdD; function=-
- `represses` --> [[gene.b4152|gene.b4152]] `RegulonDB` `S` - regulator=NarL; target=frdC; function=-
- `represses` --> [[gene.b4153|gene.b4153]] `RegulonDB` `S` - regulator=NarL; target=frdB; function=-
- `represses` --> [[gene.b4154|gene.b4154]] `RegulonDB` `S` - regulator=NarL; target=frdA; function=-
- `represses` --> [[gene.b4825|gene.b4825]] `RegulonDB` `S` - regulator=NarL; target=aspX; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1221|gene.b1221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF28`
- `KEGG:ecj:JW1212;eco:b1221;ecoc:C3026_07180;`
- `GeneID:86946678;93775289;945795;`
- `GO:GO:0000160; GO:0000976; GO:0001217; GO:0003677; GO:0003700; GO:0005524; GO:0005829; GO:0006355; GO:0032993; GO:0042128; GO:0042802`

## Notes

Nitrate/nitrite response regulator protein NarL
