---
entity_id: "protein.P77315"
entity_type: "protein"
name: "yphD"
source_database: "UniProt"
source_id: "P77315"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yphD b2546 JW2530"
---

# yphD

`protein.P77315`

## Static

- Type: `protein`
- Source: `UniProt:P77315`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Probably part of the binding-protein-dependent transport system YphDEF. Probably responsible for the translocation of the substrate across the membrane. YphD is predicted to be the membrane subunit of a putative ATP-dependent transporter . YphD is predicted to be an inner membrane protein with 9 transmembrane domains . YphD is implicated in maintaining antibiotic tolerance under starvation; yphD is upregulated during nutrient starvation and the starvation-induced ampicillin tolerance levels of a yphD knockout strain are significantly reduced over both a 6 and 30 day period .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-60-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably part of the binding-protein-dependent transport system YphDEF. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-60-CPLX|complex.ecocyc.ABC-60-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2546|gene.b2546]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77315`
- `KEGG:ecj:JW2530;eco:b2546;ecoc:C3026_14100;`
- `GeneID:949063;`
- `GO:GO:0005886; GO:0016020; GO:0022857; GO:0043190; GO:0055052; GO:0055085`

## Notes

Probable ABC transporter permease protein YphD
