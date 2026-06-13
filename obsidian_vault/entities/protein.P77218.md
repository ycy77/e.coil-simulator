---
entity_id: "protein.P77218"
entity_type: "protein"
name: "eutD"
source_database: "UniProt"
source_id: "P77218"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:21046341}. Note=It is not clear if this enzyme is found in the cytoplasm or the bacterial microcompartment. {ECO:0000305|PubMed:21046341}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutD eutI ypfA b2458 JW2442"
---

# eutD

`protein.P77218`

## Static

- Type: `protein`
- Source: `UniProt:P77218`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:21046341}. Note=It is not clear if this enzyme is found in the cytoplasm or the bacterial microcompartment. {ECO:0000305|PubMed:21046341}.

## Enriched Summary

FUNCTION: When expressed independently of the eut operon it can restore growth to a double pta-acs deletion mutant. {ECO:0000269|PubMed:21046341}.

## Biological Role

Component of phosphate acetyltransferase EutD (complex.ecocyc.CPLX0-7912).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: When expressed independently of the eut operon it can restore growth to a double pta-acs deletion mutant. {ECO:0000269|PubMed:21046341}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7912|complex.ecocyc.CPLX0-7912]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2458|gene.b2458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77218`
- `KEGG:ecj:JW2442;eco:b2458;ecoc:C3026_13640;`
- `GeneID:75172563;946940;`
- `GO:GO:0005737; GO:0008959; GO:0009408; GO:0016746; GO:0042803; GO:0046336`
- `EC:2.3.1.8`

## Notes

Phosphate acetyltransferase EutD (EC 2.3.1.8) (Ethanolamine utilization protein EutD)
