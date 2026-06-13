---
entity_id: "protein.P0AF93"
entity_type: "protein"
name: "ridA"
source_database: "UniProt"
source_id: "P0AF93"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ridA yjgF b4243 JW5755"
---

# ridA

`protein.P0AF93`

## Static

- Type: `protein`
- Source: `UniProt:P0AF93`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Accelerates the release of ammonia from reactive enamine/imine intermediates of the PLP-dependent threonine dehydratase (IlvA) in the low water environment of the cell. It catalyzes the deamination of enamine/imine intermediates to yield 2-ketobutyrate and ammonia. It is required for the detoxification of reactive intermediates of IlvA due to their highly nucleophilic abilities. Involved in the isoleucine biosynthesis. {ECO:0000250|UniProtKB:Q7CP78}.

## Biological Role

Component of enamine/imine deaminase, redox-regulated chaperone (complex.ecocyc.CPLX0-1881).

## Annotation

FUNCTION: Accelerates the release of ammonia from reactive enamine/imine intermediates of the PLP-dependent threonine dehydratase (IlvA) in the low water environment of the cell. It catalyzes the deamination of enamine/imine intermediates to yield 2-ketobutyrate and ammonia. It is required for the detoxification of reactive intermediates of IlvA due to their highly nucleophilic abilities. Involved in the isoleucine biosynthesis. {ECO:0000250|UniProtKB:Q7CP78}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1881|complex.ecocyc.CPLX0-1881]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4243|gene.b4243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF93`
- `KEGG:ecj:JW5755;eco:b4243;ecoc:C3026_22900;`
- `GeneID:93777581;948771;`
- `GO:GO:0005829; GO:0009097; GO:0009636; GO:0016020; GO:0019239; GO:0032991; GO:0042802; GO:0051082; GO:0070207; GO:0120242; GO:0120243`
- `EC:3.5.99.10`

## Notes

2-iminobutanoate/2-iminopropanoate deaminase (EC 3.5.99.10) (Enamine/imine deaminase)
