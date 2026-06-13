---
entity_id: "protein.P31802"
entity_type: "protein"
name: "narP"
source_database: "UniProt"
source_id: "P31802"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narP b2193 JW2181"
---

# narP

`protein.P31802`

## Static

- Type: `protein`
- Source: `UniProt:P31802`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins. NarP, "nitrate/nitrite response regulator NarP," is a transcriptional dual regulator of many anaerobic electron transport and fermentation-related genes in the response to the availability of high concentrations of nitrate or nitrite . A microarray analysis suggests that NarP activates 14 operons and represses 37 operons . The response regulator NarP belongs to the LuxR/UhpA family and is part of the two-component system NarQ-NarP. There is intensive cross-regulation with the paralogous two-component system NarX-NarL . Each of the sensors, NarQ and NarX, phosphorylates both NarP and NarL, leading to the activation of both proteins. In the absence of nitrate and nitrite, NarX and NarQ stimulate the dephosphorylation of NarL-P and NarP-P . This reaction is specific, that is, NarP-P is only dephosphorylated by NarQ. The system discriminates between nitrate and nitrite. In the presence of nitrate both sensors phosphorylate NarL and NarP to the same extent. In the presence of nitrite, autophosphorylation of NarX is low and NarX acts primarily as a phosphatase for NarL-P...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (51)

- `activates` --> [[gene.b2194|gene.b2194]] `RegulonDB` `S` - regulator=NarP; target=ccmH; function=-+
- `activates` --> [[gene.b2195|gene.b2195]] `RegulonDB` `S` - regulator=NarP; target=ccmG; function=-+
- `activates` --> [[gene.b2196|gene.b2196]] `RegulonDB` `S` - regulator=NarP; target=ccmF; function=-+
- `activates` --> [[gene.b2197|gene.b2197]] `RegulonDB` `S` - regulator=NarP; target=ccmE; function=-+
- `activates` --> [[gene.b2198|gene.b2198]] `RegulonDB` `S` - regulator=NarP; target=ccmD; function=-+
- `activates` --> [[gene.b2199|gene.b2199]] `RegulonDB` `S` - regulator=NarP; target=ccmC; function=-+
- `activates` --> [[gene.b2200|gene.b2200]] `RegulonDB` `S` - regulator=NarP; target=ccmB; function=-+
- `activates` --> [[gene.b2201|gene.b2201]] `RegulonDB` `S` - regulator=NarP; target=ccmA; function=-+
- `activates` --> [[gene.b2202|gene.b2202]] `RegulonDB` `S` - regulator=NarP; target=napC; function=-+
- `activates` --> [[gene.b2203|gene.b2203]] `RegulonDB` `S` - regulator=NarP; target=napB; function=-+
- `activates` --> [[gene.b2204|gene.b2204]] `RegulonDB` `S` - regulator=NarP; target=napH; function=-+
- `activates` --> [[gene.b2205|gene.b2205]] `RegulonDB` `S` - regulator=NarP; target=napG; function=-+
- `activates` --> [[gene.b2206|gene.b2206]] `RegulonDB` `S` - regulator=NarP; target=napA; function=-+
- `activates` --> [[gene.b2207|gene.b2207]] `RegulonDB` `S` - regulator=NarP; target=napD; function=-+
- `activates` --> [[gene.b2208|gene.b2208]] `RegulonDB` `S` - regulator=NarP; target=napF; function=-+
- `activates` --> [[gene.b3365|gene.b3365]] `RegulonDB` `C` - regulator=NarP; target=nirB; function=+
- `activates` --> [[gene.b3366|gene.b3366]] `RegulonDB` `C` - regulator=NarP; target=nirD; function=+
- `activates` --> [[gene.b3367|gene.b3367]] `RegulonDB` `C` - regulator=NarP; target=nirC; function=+
- `activates` --> [[gene.b3368|gene.b3368]] `RegulonDB` `C` - regulator=NarP; target=cysG; function=+
- `activates` --> [[gene.b4070|gene.b4070]] `RegulonDB` `C` - regulator=NarP; target=nrfA; function=+
- `activates` --> [[gene.b4071|gene.b4071]] `RegulonDB` `C` - regulator=NarP; target=nrfB; function=+
- `activates` --> [[gene.b4072|gene.b4072]] `RegulonDB` `C` - regulator=NarP; target=nrfC; function=+
- `activates` --> [[gene.b4073|gene.b4073]] `RegulonDB` `C` - regulator=NarP; target=nrfD; function=+
- `activates` --> [[gene.b4074|gene.b4074]] `RegulonDB` `C` - regulator=NarP; target=nrfE; function=+
- `activates` --> [[gene.b4075|gene.b4075]] `RegulonDB` `C` - regulator=NarP; target=nrfF; function=+
- `activates` --> [[gene.b4076|gene.b4076]] `RegulonDB` `C` - regulator=NarP; target=nrfG; function=+
- `represses` --> [[gene.b1474|gene.b1474]] `RegulonDB` `S` - regulator=NarP; target=fdnG; function=-
- `represses` --> [[gene.b1475|gene.b1475]] `RegulonDB` `S` - regulator=NarP; target=fdnH; function=-
- `represses` --> [[gene.b1476|gene.b1476]] `RegulonDB` `S` - regulator=NarP; target=fdnI; function=-
- `represses` --> [[gene.b1501|gene.b1501]] `RegulonDB` `S` - regulator=NarP; target=ydeP; function=-
- `represses` --> [[gene.b1669|gene.b1669]] `RegulonDB` `C` - regulator=NarP; target=ydhT; function=-
- `represses` --> [[gene.b1670|gene.b1670]] `RegulonDB` `C` - regulator=NarP; target=ydhU; function=-
- `represses` --> [[gene.b1671|gene.b1671]] `RegulonDB` `C` - regulator=NarP; target=ydhX; function=-
- `represses` --> [[gene.b1672|gene.b1672]] `RegulonDB` `C` - regulator=NarP; target=ydhW; function=-
- `represses` --> [[gene.b1673|gene.b1673]] `RegulonDB` `C` - regulator=NarP; target=ydhV; function=-
- `represses` --> [[gene.b1674|gene.b1674]] `RegulonDB` `C` - regulator=NarP; target=ydhY; function=-
- `represses` --> [[gene.b2194|gene.b2194]] `RegulonDB` `S` - regulator=NarP; target=ccmH; function=-+
- `represses` --> [[gene.b2195|gene.b2195]] `RegulonDB` `S` - regulator=NarP; target=ccmG; function=-+
- `represses` --> [[gene.b2196|gene.b2196]] `RegulonDB` `S` - regulator=NarP; target=ccmF; function=-+
- `represses` --> [[gene.b2197|gene.b2197]] `RegulonDB` `S` - regulator=NarP; target=ccmE; function=-+
- `represses` --> [[gene.b2198|gene.b2198]] `RegulonDB` `S` - regulator=NarP; target=ccmD; function=-+
- `represses` --> [[gene.b2199|gene.b2199]] `RegulonDB` `S` - regulator=NarP; target=ccmC; function=-+
- `represses` --> [[gene.b2200|gene.b2200]] `RegulonDB` `S` - regulator=NarP; target=ccmB; function=-+
- `represses` --> [[gene.b2201|gene.b2201]] `RegulonDB` `S` - regulator=NarP; target=ccmA; function=-+
- `represses` --> [[gene.b2202|gene.b2202]] `RegulonDB` `S` - regulator=NarP; target=napC; function=-+
- `represses` --> [[gene.b2203|gene.b2203]] `RegulonDB` `S` - regulator=NarP; target=napB; function=-+
- `represses` --> [[gene.b2204|gene.b2204]] `RegulonDB` `S` - regulator=NarP; target=napH; function=-+
- `represses` --> [[gene.b2205|gene.b2205]] `RegulonDB` `S` - regulator=NarP; target=napG; function=-+
- `represses` --> [[gene.b2206|gene.b2206]] `RegulonDB` `S` - regulator=NarP; target=napA; function=-+
- `represses` --> [[gene.b2207|gene.b2207]] `RegulonDB` `S` - regulator=NarP; target=napD; function=-+
- `represses` --> [[gene.b2208|gene.b2208]] `RegulonDB` `S` - regulator=NarP; target=napF; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2193|gene.b2193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31802`
- `KEGG:ecj:JW2181;eco:b2193;ecoc:C3026_12260;`
- `GeneID:949081;`
- `GO:GO:0000160; GO:0000976; GO:0003677; GO:0003700; GO:0005524; GO:0006355; GO:0042128`

## Notes

Nitrate/nitrite response regulator protein NarP
