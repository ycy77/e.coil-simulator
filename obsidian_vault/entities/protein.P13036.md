---
entity_id: "protein.P13036"
entity_type: "protein"
name: "fecA"
source_database: "UniProt"
source_id: "P13036"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecA b4291 JW4251"
---

# fecA

`protein.P13036`

## Static

- Type: `protein`
- Source: `UniProt:P13036`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|PROSITE-ProRule:PRU01360}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU01360}.

## Enriched Summary

FUNCTION: FecA is the outer membrane receptor protein in the Fe(3+) dicitrate transport system. FecA is an outer membrane (OM) protein which mediates the citrate dependent import of ferric iron; FecA mediated transport across the OM is energized by the inner membrane proton gradient; energy transduction is facilitated by the CPLX0-1923 (reviewed in ). FecA also signals the extracellular presence of iron to the FecR/FecI anti-sigma factor/sigma factor pair in the Fec signaling pathway. The outer membrane protein, FecA, is expressed under iron-limiting growth conditions in the presence of citrate . fecA forms an operon with fecBCDE encoding a ferric dicitrate ABC transporter; the operon responds to ferric citrate induction and Fur-Fe2+ repression . Ferric citrate does not have to enter the cell to induce transcription of the operon; FecA (and the Ton complex) are directly involved in fec operon induction independent of their role in transport; substrate binding to FecA initiates a signal that is transferred across the inner membrane by EG10292-MONOMER "FecR" to activate the the iron starvation responsive sigma factor PD00440 "FecI", which facilitates binding of RNA polymerase to the upstream region of fecA (and see ). The N-terminal, periplasmic region of FecA interacts with the C-terminal portion of FecR (see further )...

## Biological Role

Component of ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943).

## Annotation

FUNCTION: FecA is the outer membrane receptor protein in the Fe(3+) dicitrate transport system.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4291|gene.b4291]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13036`
- `KEGG:ecj:JW4251;eco:b4291;ecoc:C3026_23140;`
- `GeneID:946427;`
- `GO:GO:0006355; GO:0006879; GO:0009279; GO:0015343; GO:0015891; GO:0016020; GO:0023019; GO:0033214; GO:0038023; GO:1902495; GO:1990641`

## Notes

Fe(3+) dicitrate transport protein FecA (Iron(III) dicitrate transport protein FecA)
