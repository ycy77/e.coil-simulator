---
entity_id: "protein.P0AFM9"
entity_type: "protein"
name: "pspB"
source_database: "UniProt"
source_id: "P0AFM9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pspB b1305 JW1298"
---

# pspB

`protein.P0AFM9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFM9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein.

## Enriched Summary

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspB is involved in transcription regulation. {ECO:0000269|PubMed:1712397}. PspB and EG10778-MONOMER PspC together act to activate transcription of the TU00326 operon induced by infection with bacteriophage, exposure to ethanol, osmotic shock, or heat shock; PspC is essential for this activation, whereas PspB is not strictly required . PspC and PspB are also reported to be a toxin-antitoxin pair . EG10776-MONOMER PspA, PspB, and EG10778-MONOMER PspC form a complex, and PspC is required for PspA to bind to PspB . PspA, PspB, and PspC are not observed to cross-link with PspD . A pspB mutant exhibits a defect in protein translocation that is suppressed by production of PspA, which plays a role in maintenance of the protonmotive force under certain conditions of cellular stress . Multi-copy overexpression of the TU00326 operon increases survival upon stress caused by n-hexane treatment . The corresponding psp locus of Yersinia enterocolitica is virulence-related . Regulation has been described . The psp operon shows induction upon phage infection, temperature increase, or exposure to ethanol, osmotic shock , or the organic solvents n-hexane or cyclooctane . Induction is mediated by sigma54, PspB, PspC , PspF , and IHF...

## Biological Role

Component of PspABC complex (complex.ecocyc.CPLX0-10367).

## Annotation

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspB is involved in transcription regulation. {ECO:0000269|PubMed:1712397}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10367|complex.ecocyc.CPLX0-10367]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1305|gene.b1305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFM9`
- `KEGG:ecj:JW1298;eco:b1305;ecoc:C3026_07655;`
- `GeneID:75171430;75203420;945893;`
- `GO:GO:0005886; GO:0006355; GO:0009271; GO:0080135`

## Notes

Phage shock protein B
