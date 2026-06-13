---
entity_id: "protein.P0AEB2"
entity_type: "protein"
name: "dacA"
source_database: "UniProt"
source_id: "P0AEB2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Note=N-terminal lies in the periplasmic space."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dacA pfv b0632 JW0627"
---

# dacA

`protein.P0AEB2`

## Static

- Type: `protein`
- Source: `UniProt:P0AEB2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Note=N-terminal lies in the periplasmic space.

## Enriched Summary

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors.

## Biological Role

Component of D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0632|gene.b0632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEB2`
- `KEGG:ecj:JW0627;eco:b0632;ecoc:C3026_03160;`
- `GeneID:93776850;945222;`
- `GO:GO:0000270; GO:0004180; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008800; GO:0009002; GO:0009252; GO:0030288; GO:0042803; GO:0051301; GO:0071555`
- `EC:3.4.16.4; 3.5.2.6`

## Notes

D-alanyl-D-alanine carboxypeptidase DacA (DD-carboxypeptidase) (DD-peptidase) (EC 3.4.16.4) (Beta-lactamase) (EC 3.5.2.6) (Penicillin-binding protein 5) (PBP-5)
