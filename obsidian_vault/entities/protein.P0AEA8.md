---
entity_id: "protein.P0AEA8"
entity_type: "protein"
name: "cysG"
source_database: "UniProt"
source_id: "P0AEA8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysG b3368 JW3331"
---

# cysG

`protein.P0AEA8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEA8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Multifunctional enzyme that catalyzes the SAM-dependent methylations of uroporphyrinogen III at position C-2 and C-7 to form precorrin-2 via precorrin-1. Then it catalyzes the NAD-dependent ring dehydrogenation of precorrin-2 to yield sirohydrochlorin. Finally, it catalyzes the ferrochelation of sirohydrochlorin to yield siroheme. {ECO:0000255|HAMAP-Rule:MF_01646, ECO:0000269|PubMed:2407234, ECO:0000269|PubMed:2407558, ECO:0000269|PubMed:8243665, ECO:0000269|PubMed:8573073, ECO:0000269|PubMed:9461500}.

## Biological Role

Catalyzes S-adenosyl-L-methionine:uroporphyrin-III C-methyltransferase (reaction.R02864), S-adenosyl-L-methionine:uroporphyrinogen-III C-methyltransferase (reaction.R03194). Component of siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Multifunctional enzyme that catalyzes the SAM-dependent methylations of uroporphyrinogen III at position C-2 and C-7 to form precorrin-2 via precorrin-1. Then it catalyzes the NAD-dependent ring dehydrogenation of precorrin-2 to yield sirohydrochlorin. Finally, it catalyzes the ferrochelation of sirohydrochlorin to yield siroheme. {ECO:0000255|HAMAP-Rule:MF_01646, ECO:0000269|PubMed:2407234, ECO:0000269|PubMed:2407558, ECO:0000269|PubMed:8243665, ECO:0000269|PubMed:8573073, ECO:0000269|PubMed:9461500}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02864|reaction.R02864]] `KEGG` `database` - via EC:4.99.1.4
- `catalyzes` --> [[reaction.R03194|reaction.R03194]] `KEGG` `database` - via EC:2.1.1.107
- `is_component_of` --> [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3368|gene.b3368]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEA8`
- `KEGG:ecj:JW3331;eco:b3368;ecoc:C3026_18290;`
- `GeneID:75173526;947880;`
- `GO:GO:0004851; GO:0006970; GO:0009236; GO:0019354; GO:0032259; GO:0042803; GO:0043115; GO:0051266; GO:0051287`
- `EC:1.3.1.76; 2.1.1.107; 4.99.1.4`

## Notes

Siroheme synthase [Includes: Uroporphyrinogen-III C-methyltransferase (Urogen III methylase) (EC 2.1.1.107) (SUMT) (Uroporphyrinogen III methylase) (UROM); Precorrin-2 dehydrogenase (EC 1.3.1.76); Sirohydrochlorin ferrochelatase (EC 4.99.1.4)]
