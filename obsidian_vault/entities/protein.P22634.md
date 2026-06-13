---
entity_id: "protein.P22634"
entity_type: "protein"
name: "murI"
source_database: "UniProt"
source_id: "P22634"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murI dga glr yijA b3967 JW5550"
---

# murI

`protein.P22634`

## Static

- Type: `protein`
- Source: `UniProt:P22634`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides the (R)-glutamate required for cell wall biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00258, ECO:0000269|PubMed:1355768, ECO:0000269|PubMed:8098327, ECO:0000305|PubMed:17568739}. Glutamate racemase (MurI) catalyzes the racemization of L-glutamate to D-glutamate, an essential component that is unique to bacterial peptidoglycan . Physiological concentrations of UDP-N-acetylmuramyl-L-Ala, the second substrate of the subsequent reaction in peptidoglycan biosynthesis, specifically activates the enzyme . It was suggested that the unique N terminus of MurI is required for activation ; however, an N-terminally truncated enzyme is still activated by UDP-N-acetylmuramyl-L-Ala . Site-directed mutagenesis of the two conserved cysteine residues showed that they are essential for enzymatic activity, suggesting that they are involved in the two-base reaction mechanism . Evidence regarding the quarternary structure of MurI was contradictory: reported a homodimer, while report that the enzyme is monomeric. A crystal structure of MurI in complex with UDP-N-acetylmuramyl-L-Ala has been solved at 1.9 Å resolution and shows a monomer. The activator binds in a hinge region opposite to the catalytically active site . Activated MurI appears to inhibit CPLX0-2425 activity . A D-glutamate-requiring strain first isolated in the E...

## Biological Role

Catalyzes glutamate racemase (reaction.R00260), GLUTRACE-RXN (reaction.ecocyc.GLUTRACE-RXN).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Provides the (R)-glutamate required for cell wall biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00258, ECO:0000269|PubMed:1355768, ECO:0000269|PubMed:8098327, ECO:0000305|PubMed:17568739}.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00260|reaction.R00260]] `KEGG` `database` - via EC:5.1.1.3
- `catalyzes` --> [[reaction.ecocyc.GLUTRACE-RXN|reaction.ecocyc.GLUTRACE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3967|gene.b3967]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22634`
- `KEGG:ecj:JW5550;eco:b3967;`
- `GeneID:948467;`
- `GO:GO:0008360; GO:0008881; GO:0009252; GO:0071555`
- `EC:5.1.1.3`

## Notes

Glutamate racemase (EC 5.1.1.3)
