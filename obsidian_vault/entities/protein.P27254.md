---
entity_id: "protein.P27254"
entity_type: "protein"
name: "argK"
source_database: "UniProt"
source_id: "P27254"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argK ygfD b2918 JW2885"
---

# argK

`protein.P27254`

## Static

- Type: `protein`
- Source: `UniProt:P27254`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds and hydrolyzes GTP (PubMed:18950999). Likely functions as a G-protein chaperone that assists AdoCbl cofactor delivery to the methylmalonyl-CoA mutase (MCM) ScpA and reactivation of the enzyme during catalysis. {ECO:0000269|PubMed:18950999, ECO:0000305}. YgfD is a member of the G3E family of P-loop GTPases . The YgfD protein and CPLX0-7741 (encoded upstream of YgfD) interact both in vivo and in vitro; detection of the interaction depends on the presence of a non-hydrolyzable GTP analog . YgfD was first identified as an ATPase, ArgK, that appeared to phosphorylate the periplasmic binding proteins of the lysine, arginine, ornithine transport system as well as the arginine, ornithine transport system . However, the kinase activity of ArgK did not affect transport activity . Neither the molecular weight nor the pI of ArgK are similar to that of the protein kinase that was purified based on its activity . Overexpression of YgfD contributes to increased production of 1-propanol in an engineered E. coli strain .

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Enriched Pathways

- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

FUNCTION: Binds and hydrolyzes GTP (PubMed:18950999). Likely functions as a G-protein chaperone that assists AdoCbl cofactor delivery to the methylmalonyl-CoA mutase (MCM) ScpA and reactivation of the enzyme during catalysis. {ECO:0000269|PubMed:18950999, ECO:0000305}.

## Pathways

- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2918|gene.b2918]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27254`
- `KEGG:ecj:JW2885;eco:b2918;ecoc:C3026_15990;`
- `GeneID:75205244;947412;`
- `GO:GO:0003924; GO:0005524; GO:0005525; GO:0005737`
- `EC:3.6.5.-`

## Notes

GTPase ArgK (EC 3.6.5.-) (G-protein chaperone)
