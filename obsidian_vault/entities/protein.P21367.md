---
entity_id: "protein.P21367"
entity_type: "protein"
name: "ycaC"
source_database: "UniProt"
source_id: "P21367"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycaC b0897 JW0880"
---

# ycaC

`protein.P21367`

## Static

- Type: `protein`
- Source: `UniProt:P21367`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Probable hydrolase YcaC (EC 4.-.-.-) The crystal structure of YcaC, solved at 1.8 Å resolution, indicates that YcaC has similarity to hydrolases and forms a homooctamer (a dimer of tetrameric ring structures) . The protein shows structural similarity to the pyrazinamidase encoded by the Pyrococcus horikoshii 999 gene . Cys118 is identified as a likely catalytic residue . A ΔycaC mutant shows increased resistance to the proline-rich antimicrobial peptide (PrAMP) apidaecin 1b and the designer peptide Api88 .

## Biological Role

Component of putative hydrolase YcaC (complex.ecocyc.CPLX0-661).

## Annotation

Probable hydrolase YcaC (EC 4.-.-.-)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-661|complex.ecocyc.CPLX0-661]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b0897|gene.b0897]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21367`
- `KEGG:ecj:JW0880;eco:b0897;ecoc:C3026_05545;`
- `GeneID:945512;`
- `GO:GO:0005829; GO:0016020; GO:0016787; GO:0016829; GO:0042802`
- `EC:4.-.-.-`

## Notes

Probable hydrolase YcaC (EC 4.-.-.-)
