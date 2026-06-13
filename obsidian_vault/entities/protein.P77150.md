---
entity_id: "protein.P77150"
entity_type: "protein"
name: "pdxY"
source_database: "UniProt"
source_id: "P77150"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxY ydgS b1636 JW1628"
---

# pdxY

`protein.P77150`

## Static

- Type: `protein`
- Source: `UniProt:P77150`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Pyridoxal kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxal to PLP in vivo, but shows very low activity compared to PdxK. Displays a low level of pyridoxine kinase activity when overexpressed, which is however not physiologically relevant. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}.

## Biological Role

Catalyzes ATP:pyridoxal 5'-phosphotransferase (reaction.R00174), ATP:pyridoxine 5'-phosphotransferase (reaction.R01909). Component of pyridoxal kinase 2 (complex.ecocyc.CPLX0-8031).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Pyridoxal kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxal to PLP in vivo, but shows very low activity compared to PdxK. Displays a low level of pyridoxine kinase activity when overexpressed, which is however not physiologically relevant. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00174|reaction.R00174]] `KEGG` `database` - via EC:2.7.1.35
- `catalyzes` --> [[reaction.R01909|reaction.R01909]] `KEGG` `database` - via EC:2.7.1.35
- `is_component_of` --> [[complex.ecocyc.CPLX0-8031|complex.ecocyc.CPLX0-8031]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1636|gene.b1636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77150`
- `KEGG:ecj:JW1628;eco:b1636;`
- `GeneID:75204481;946162;`
- `GO:GO:0000287; GO:0005524; GO:0005829; GO:0008478; GO:0009443; GO:0042803; GO:0042817; GO:0042819`
- `EC:2.7.1.35`

## Notes

Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (Pyridoxal kinase 2) (PL kinase 2)
