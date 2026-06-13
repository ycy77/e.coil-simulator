---
entity_id: "protein.Q47377"
entity_type: "protein"
name: "arnE"
source_database: "UniProt"
source_id: "Q47377"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnE pmrL yfbW b4544 JW2252"
---

# arnE

`protein.Q47377`

## Static

- Type: `protein`
- Source: `UniProt:Q47377`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Translocates 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol (alpha-L-Ara4N-phosphoundecaprenol) from the cytoplasmic to the periplasmic side of the inner membrane. {ECO:0000269|PubMed:17928292}. ArnE is an integral membrane component of the ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase.

## Biological Role

Component of undecaprenyl-phosphate-α-L-Ara4N flippase (complex.ecocyc.CPLX0-7720).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Translocates 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol (alpha-L-Ara4N-phosphoundecaprenol) from the cytoplasmic to the periplasmic side of the inner membrane. {ECO:0000269|PubMed:17928292}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7720|complex.ecocyc.CPLX0-7720]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4544|gene.b4544]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47377`
- `KEGG:ecj:JW2252;eco:b4544;ecoc:C3026_12610;`
- `GeneID:1450282;93774916;`
- `GO:GO:0005886; GO:0009103; GO:0009245; GO:0010041; GO:0022857; GO:0055085; GO:1901264; GO:1901505`

## Notes

Probable 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol flippase subunit ArnE (L-Ara4N-phosphoundecaprenol flippase subunit ArnE) (Undecaprenyl phosphate-aminoarabinose flippase subunit ArnE)
