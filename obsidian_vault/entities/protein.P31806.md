---
entity_id: "protein.P31806"
entity_type: "protein"
name: "nnr"
source_database: "UniProt"
source_id: "P31806"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nnr yjeF b4167 JW4125"
---

# nnr

`protein.P31806`

## Static

- Type: `protein`
- Source: `UniProt:P31806`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional enzyme that catalyzes the epimerization of the S- and R-forms of NAD(P)HX and the dehydration of the S-form of NAD(P)HX at the expense of ADP, which is converted to AMP. This allows the repair of both epimers of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration. {ECO:0000269|PubMed:21994945}. The Nnr protein is a bifunctional enzyme that catalyzes both the epimerization between the R and S forms of NAD(P)HX and the ADP-dependent repair of (S)-NAD(P)HX to NAD(P)H. The N-terminal domain appears to be responsible for the epimerase activity, while the C-terminal domain is responsible for the dehydratase activity . Comparative genomics and metabolomics experiments suggest that Nnr, and in particular the epimerase domain, may have a moonlighting function that involves pyridoxal phosphate metabolism . Studies in the 1950s have shown that eukaryotic GAPOXNPHOSPHN-RXN "glyceraldehyde 3-phosphate dehydrogenase" slowly catalyzes the formation of a hydrated form of NADH, called NADHX, from NADH . The equilibrium of this hydration reaction is in favor (100/1) of the hydrated form , making the reaction virtually irreversible. In addition, NADHX can be formed spontaneously from NADH under slightly acidic conditions...

## Biological Role

Catalyzes (6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide hydro-lyase (ADP-hydrolysing; NADH-forming) (reaction.R10267), (6S)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide-phosphate hydro-lyase (ADP-hydrolysing; NADPH-forming) (reaction.R10268), (6R)-6beta-hydroxy-1,4,5,6-tetrahydronicotinamide-adenine-dinucleotide 6-epimerase (reaction.R10280), RXN-12752 (reaction.ecocyc.RXN-12752), RXN-13141 (reaction.ecocyc.RXN-13141), RXN-13142 (reaction.ecocyc.RXN-13142), RXN0-6727 (reaction.ecocyc.RXN0-6727).

## Annotation

FUNCTION: Bifunctional enzyme that catalyzes the epimerization of the S- and R-forms of NAD(P)HX and the dehydration of the S-form of NAD(P)HX at the expense of ADP, which is converted to AMP. This allows the repair of both epimers of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration. {ECO:0000269|PubMed:21994945}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R10267|reaction.R10267]] `KEGG` `database` - via EC:4.2.1.136
- `catalyzes` --> [[reaction.R10268|reaction.R10268]] `KEGG` `database` - via EC:4.2.1.136
- `catalyzes` --> [[reaction.R10280|reaction.R10280]] `KEGG` `database` - via EC:5.1.99.6
- `catalyzes` --> [[reaction.ecocyc.RXN-12752|reaction.ecocyc.RXN-12752]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13141|reaction.ecocyc.RXN-13141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13142|reaction.ecocyc.RXN-13142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6727|reaction.ecocyc.RXN0-6727]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4167|gene.b4167]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31806`
- `KEGG:ecj:JW4125;eco:b4167;`
- `GeneID:948685;`
- `GO:GO:0005524; GO:0046496; GO:0046872; GO:0052855; GO:0052856; GO:0110051`
- `EC:4.2.1.136; 5.1.99.6`

## Notes

Bifunctional NAD(P)H-hydrate repair enzyme Nnr (Nicotinamide nucleotide repair protein) [Includes: ADP-dependent (S)-NAD(P)H-hydrate dehydratase (EC 4.2.1.136) (ADP-dependent NAD(P)HX dehydratase); NAD(P)H-hydrate epimerase (EC 5.1.99.6) (NAD(P)HX epimerase)]
