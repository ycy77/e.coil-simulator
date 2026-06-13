---
entity_id: "protein.P0AFG6"
entity_type: "protein"
name: "sucB"
source_database: "UniProt"
source_id: "P0AFG6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sucB b0727 JW0716"
---

# sucB

`protein.P0AFG6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFG6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: E2 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the second step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000305|PubMed:17367808}.

## Biological Role

Component of 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX), 2-oxoglutarate dehydrogenase E2 subunit (complex.ecocyc.E2O).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

FUNCTION: E2 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the second step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000305|PubMed:17367808}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=24
- `is_component_of` --> [[complex.ecocyc.E2O|complex.ecocyc.E2O]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b0727|gene.b0727]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFG6`
- `KEGG:ecj:JW0716;eco:b0727;ecoc:C3026_03640;`
- `GeneID:93776758;945307;`
- `GO:GO:0004149; GO:0005737; GO:0005829; GO:0006099; GO:0031405; GO:0033512; GO:0045252`
- `EC:2.3.1.61`

## Notes

Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase complex component E2) (OGDC-E2) (Dihydrolipoamide succinyltransferase component of 2-oxoglutarate dehydrogenase complex)
