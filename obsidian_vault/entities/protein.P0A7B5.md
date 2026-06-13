---
entity_id: "protein.P0A7B5"
entity_type: "protein"
name: "proB"
source_database: "UniProt"
source_id: "P0A7B5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00456}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proB b0242 JW0232"
---

# proB

`protein.P0A7B5`

## Static

- Type: `protein`
- Source: `UniProt:P0A7B5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00456}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of a phosphate group to glutamate to form L-glutamate 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_00456, ECO:0000269|PubMed:6319365}.

## Biological Role

Catalyzes ATP:L-glutamate 5-phosphotransferase (reaction.R00239). Component of glutamate 5-kinase (complex.ecocyc.GLUTKIN-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a phosphate group to glutamate to form L-glutamate 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_00456, ECO:0000269|PubMed:6319365}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00239|reaction.R00239]] `KEGG` `database` - via EC:2.7.2.11
- `is_component_of` --> [[complex.ecocyc.GLUTKIN-CPLX|complex.ecocyc.GLUTKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0242|gene.b0242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7B5`
- `KEGG:ecj:JW0232;eco:b0242;ecoc:C3026_01150;ecoc:C3026_23885;`
- `GeneID:93777151;946425;`
- `GO:GO:0000287; GO:0003723; GO:0004349; GO:0005524; GO:0005829; GO:0042802; GO:0042803; GO:0055129; GO:1901973`
- `EC:2.7.2.11`

## Notes

Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK)
