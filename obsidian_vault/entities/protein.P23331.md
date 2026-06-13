---
entity_id: "protein.P23331"
entity_type: "protein"
name: "tdk"
source_database: "UniProt"
source_id: "P23331"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00124}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdk b1238 JW1226"
---

# tdk

`protein.P23331`

## Static

- Type: `protein`
- Source: `UniProt:P23331`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00124}.

## Enriched Summary

FUNCTION: Phosphorylates both thymidine and deoxyuridine.

## Biological Role

Component of thymidine kinase / deoxyuridine kinase (complex.ecocyc.CPLX0-8261).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Phosphorylates both thymidine and deoxyuridine.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8261|complex.ecocyc.CPLX0-8261]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1238|gene.b1238]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23331`
- `KEGG:ecj:JW1226;eco:b1238;ecoc:C3026_07280;`
- `GeneID:945834;`
- `GO:GO:0004797; GO:0005524; GO:0005829; GO:0008270; GO:0036198; GO:0042802; GO:0046104; GO:0071897`
- `EC:2.7.1.21`

## Notes

Thymidine kinase (EC 2.7.1.21)
