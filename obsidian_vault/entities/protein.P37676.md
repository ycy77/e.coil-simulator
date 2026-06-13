---
entity_id: "protein.P37676"
entity_type: "protein"
name: "yiaO"
source_database: "UniProt"
source_id: "P37676"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16385129}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaO b3579 JW3551"
---

# yiaO

`protein.P37676`

## Static

- Type: `protein`
- Source: `UniProt:P37676`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16385129}.

## Enriched Summary

FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. This protein specifically binds 2,3-diketo-L-gulonate. Is not able to bind either L-ascorbate or dehydroascorbate. {ECO:0000269|PubMed:16385129}. Based on sequence similarity, YiaO is the periplasmic solute-binding component of the YiaMNO Binding Protein-dependent Secondary (TRAP) transporter

## Biological Role

Component of 2,3-diketo-L-gulonate:Na+ symporter (complex.ecocyc.TRANS-CPLX-203).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. This protein specifically binds 2,3-diketo-L-gulonate. Is not able to bind either L-ascorbate or dehydroascorbate. {ECO:0000269|PubMed:16385129}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-203|complex.ecocyc.TRANS-CPLX-203]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3579|gene.b3579]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37676`
- `KEGG:ecj:JW3551;eco:b3579;ecoc:C3026_19405;`
- `GeneID:948091;`
- `GO:GO:0006974; GO:0008643; GO:0016020; GO:0030246; GO:0030288; GO:0031317; GO:0034219; GO:1900190; GO:1902075`

## Notes

2,3-diketo-L-gulonate-binding periplasmic protein YiaO (2,3-DKG-binding protein) (Extracytoplasmic solute receptor protein YiaO)
