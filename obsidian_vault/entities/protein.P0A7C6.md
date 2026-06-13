---
entity_id: "protein.P0A7C6"
entity_type: "protein"
name: "pepE"
source_database: "UniProt"
source_id: "P0A7C6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00510}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepE b4021 JW3981"
---

# pepE

`protein.P0A7C6`

## Static

- Type: `protein`
- Source: `UniProt:P0A7C6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00510}.

## Enriched Summary

FUNCTION: Hydrolyzes dipeptides containing N-terminal aspartate residues. May play a role in allowing the cell to use peptide aspartate to spare carbon otherwise required for the synthesis of the aspartate family of amino acids. {ECO:0000255|HAMAP-Rule:MF_00510}. PepE hydrolyzes peptides bond in dipeptides where the first amino acid is aspartate .

## Biological Role

Catalyzes 3.4.13.21-RXN (reaction.ecocyc.3.4.13.21-RXN).

## Annotation

FUNCTION: Hydrolyzes dipeptides containing N-terminal aspartate residues. May play a role in allowing the cell to use peptide aspartate to spare carbon otherwise required for the synthesis of the aspartate family of amino acids. {ECO:0000255|HAMAP-Rule:MF_00510}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.13.21-RXN|reaction.ecocyc.3.4.13.21-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4021|gene.b4021]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7C6`
- `KEGG:ecj:JW3981;eco:b4021;ecoc:C3026_21720;`
- `GeneID:93777874;948520;`
- `GO:GO:0005737; GO:0006508; GO:0008233; GO:0008236; GO:0016805`
- `EC:3.4.13.21`

## Notes

Peptidase E (EC 3.4.13.21) (Alpha-aspartyl dipeptidase) (Asp-specific dipeptidase) (Dipeptidase E)
