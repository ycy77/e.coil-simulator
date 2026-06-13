---
entity_id: "protein.P17445"
entity_type: "protein"
name: "betB"
source_database: "UniProt"
source_id: "P17445"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "betB b0312 JW0304"
---

# betB

`protein.P17445`

## Static

- Type: `protein`
- Source: `UniProt:P17445`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the irreversible oxidation of betaine aldehyde to the corresponding acid. It is highly specific for betaine and has a significantly higher affinity for NAD than for NADP. {ECO:0000255|HAMAP-Rule:MF_00804, ECO:0000269|PubMed:2194570, ECO:0000269|PubMed:3512525}. Betaine aldehyde dehydrogenase (BADH) catalyzes the second step in the biosynthesis of the osmoprotectant glycine betaine from choline . Expression of the bet operon is regulated by oxygen, choline, osmotic stress, and temperature . Inactivation of six genes encoding aldehyde dehydrogenases (EG12292, EG10036, EG10110, G6755, G7961, and EG11329) resulted in a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . BetB: "betaine"

## Biological Role

Component of betaine aldehyde dehydrogenase (complex.ecocyc.BADH-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the irreversible oxidation of betaine aldehyde to the corresponding acid. It is highly specific for betaine and has a significantly higher affinity for NAD than for NADP. {ECO:0000255|HAMAP-Rule:MF_00804, ECO:0000269|PubMed:2194570, ECO:0000269|PubMed:3512525}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.BADH-CPLX|complex.ecocyc.BADH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0312|gene.b0312]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17445`
- `KEGG:ecj:JW0304;eco:b0312;ecoc:C3026_01525;ecoc:C3026_24700;`
- `GeneID:947376;`
- `GO:GO:0005829; GO:0006970; GO:0008802; GO:0010165; GO:0019285; GO:0032991; GO:0042802; GO:0046872; GO:0051289`
- `EC:1.2.1.8`

## Notes

Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8)
