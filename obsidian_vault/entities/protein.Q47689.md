---
entity_id: "protein.Q47689"
entity_type: "protein"
name: "mmuP"
source_database: "UniProt"
source_id: "Q47689"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mmuP ykfD b0260 JW5027"
---

# mmuP

`protein.Q47689`

## Static

- Type: `protein`
- Source: `UniProt:Q47689`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Transporter for the intake of S-methylmethionine. MmuP belongs to the APC superfamily of amino acid transporters and is a putative S-methylmethionine transporter . A mutant with a non-polar in-frame deletion in mmuP is unable to utilize S-methylmethionine as a source of methionine in a metE metH mutant background . MmuP does not contribute to the uptake of L- or D-methionine . mmuP forms a putative operon with mmuM (encoding a homocysteine S-methyltransferase); mmuPM expression is regulated by methionine; the synthesis of MmuM is significantly reduced when high concentrations of L-methionine are present in the culture media . MmuP: "S-methylmethionine utilization"

## Biological Role

Catalyzes TRANS-RXN0-486 (reaction.ecocyc.TRANS-RXN0-486).

## Annotation

FUNCTION: Transporter for the intake of S-methylmethionine.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-486|reaction.ecocyc.TRANS-RXN0-486]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0260|gene.b0260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47689`
- `KEGG:ecj:JW5027;eco:b0260;ecoc:C3026_01255;`
- `GeneID:946284;`
- `GO:GO:0000100; GO:0003333; GO:0005886; GO:0009086; GO:0015171; GO:0015806; GO:0016020`

## Notes

Probable S-methylmethionine permease
