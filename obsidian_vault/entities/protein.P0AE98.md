---
entity_id: "protein.P0AE98"
entity_type: "protein"
name: "csgF"
source_database: "UniProt"
source_id: "P0AE98"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csgF b1038 JW1021"
---

# csgF

`protein.P0AE98`

## Static

- Type: `protein`
- Source: `UniProt:P0AE98`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795}.

## Enriched Summary

FUNCTION: May be involved in the biogenesis of curli organelles. The curli specific genes are present in two divergently transcribed operons, csgDEFG and csgBAC, which encode the structural, accessory and regulatory proteins of the curli biosynthetic pathway (reviewed in ). CsgF localizes to the outer membrane where it interacts with CsgG to form the curli secretion channel complex; CsgF also interacts with the the curli nucleator protein G6547-MONOMER "CsgB" to promote curli subunit polymerisation. A polar mutation in csgF (csgF1::Tn104) abolishes curli formation . CsgF is localized on the outer surface of the outer membrane; in the absence of CsgF, both CsgB and EG11489-MONOMER "CsgA" are secreted away from the cell; CsgF has a role in CsgB nucleator function . CsgF and CsgG physically interact at the outer membrane . CsgF interacts with CsgB and accelerates self assembly of CsgB into an amyloid-templating conformation in vitro . CsgG and CsgF from a stable complex with a 9:9 stoichiometric ratio . The N-terminal domain of CsgF inserts into the CsgG complex to form a pore inside the CsgG channel; the C-terminal domain of CsgF is located on the extracellular side of the CsgG channel and is responsible for binding to CsgB...

## Biological Role

Component of curli secretion and assembly complex (complex.ecocyc.CPLX-3945).

## Annotation

FUNCTION: May be involved in the biogenesis of curli organelles.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-3945|complex.ecocyc.CPLX-3945]] `EcoCyc` `database` - EcoCyc component coefficient=9 | EcoCyc protcplxs.col coefficient=9 | EcoCyc transporter component coefficient=9

## Incoming Edges (1)

- `encodes` <-- [[gene.b1038|gene.b1038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE98`
- `KEGG:ecj:JW1021;eco:b1038;ecoc:C3026_06320;`
- `GeneID:93776380;945622;`
- `GO:GO:0009279; GO:0042802; GO:0062155; GO:0098775; GO:0098777`

## Notes

Curli production assembly/transport component CsgF
