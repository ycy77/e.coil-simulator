---
entity_id: "protein.P45523"
entity_type: "protein"
name: "fkpA"
source_database: "UniProt"
source_id: "P45523"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fkpA yzzS b3347 JW3309"
---

# fkpA

`protein.P45523`

## Static

- Type: `protein`
- Source: `UniProt:P45523`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.

## Biological Role

Component of peptidyl-prolyl cis-trans isomerase/OMP chaperone FkpA (complex.ecocyc.CPLX0-10157).

## Annotation

FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10157|complex.ecocyc.CPLX0-10157]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3347|gene.b3347]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45523`
- `KEGG:ecj:JW3309;eco:b3347;ecoc:C3026_18175;`
- `GeneID:947850;`
- `GO:GO:0003755; GO:0030288; GO:0042026; GO:0044183`
- `EC:5.2.1.8`

## Notes

FKBP-type peptidyl-prolyl cis-trans isomerase FkpA (PPIase) (EC 5.2.1.8) (Rotamase)
