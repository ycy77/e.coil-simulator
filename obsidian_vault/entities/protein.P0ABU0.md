---
entity_id: "protein.P0ABU0"
entity_type: "protein"
name: "menB"
source_database: "UniProt"
source_id: "P0ABU0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menB b2262 JW2257"
---

# menB

`protein.P0ABU0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABU0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts o-succinylbenzoyl-CoA (OSB-CoA) to 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA). {ECO:0000255|HAMAP-Rule:MF_01934, ECO:0000269|PubMed:1091286, ECO:0000269|PubMed:20643650, ECO:0000269|PubMed:21830810, ECO:0000269|PubMed:23658663}.

## Biological Role

Catalyzes O-succinylbenzoyl-CoA 1,4-dihydroxy-2-naphthoate-lyase (reaction.R04150). Component of 1,4-dihydroxy-2-naphthoyl-CoA synthase (complex.ecocyc.CPLX0-7882).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Converts o-succinylbenzoyl-CoA (OSB-CoA) to 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA). {ECO:0000255|HAMAP-Rule:MF_01934, ECO:0000269|PubMed:1091286, ECO:0000269|PubMed:20643650, ECO:0000269|PubMed:21830810, ECO:0000269|PubMed:23658663}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04150|reaction.R04150]] `KEGG` `database` - via EC:4.1.3.36
- `is_component_of` --> [[complex.ecocyc.CPLX0-7882|complex.ecocyc.CPLX0-7882]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2262|gene.b2262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABU0`
- `KEGG:ecj:JW2257;eco:b2262;ecoc:C3026_12635;`
- `GeneID:75172394;75205687;946747;`
- `GO:GO:0005829; GO:0008935; GO:0009234; GO:0071890`
- `EC:4.1.3.36`

## Notes

1,4-dihydroxy-2-naphthoyl-CoA synthase (DHNA-CoA synthase) (EC 4.1.3.36)
