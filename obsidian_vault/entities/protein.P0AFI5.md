---
entity_id: "protein.P0AFI5"
entity_type: "protein"
name: "pbpG"
source_database: "UniProt"
source_id: "P0AFI5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pbpG yohB b2134 JW5355"
---

# pbpG

`protein.P0AFI5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFI5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Cell wall formation. May play a specialized role in remodeling the cell wall. Specifically hydrolyzes the DD-diaminopimelate-alanine bonds in high-molecular-mass murein sacculi. pbpG encodes penicillin-binding protein 7 (PBP7) and it's cleavage product, penicillin-binding protein 8 (PBP8) . PBP8 is likely an artifact that results from contact with OmpT, an outer membrane protease, during purification procedures . PPB7 is a soluble, periplasmic protein that is loosely membrane associated; the protein is non-essential when cells are grown in rich or minimal media under typical laboratory conditions . Purified PBP7/8 is a penicillin-sensitive DD endopeptidase with a preference for cleaving the D-ala-m-DAP (4→3) cross link in high-molecular mass sacculi; PBP7/8 has minor LD-endopeptidase activity and no apparent carboxypeptidase activity . Purified PBP7 cleaves 4→3 cross-links specifically and has no activity on 3→3 (m-DAP-m-DAP) cross-links . PBP7/8 binds to EG10950-MONOMER (Slt70) in vitro; PBP7/8 stimulates Slt70 activity in vitro . Loss of PBP7 accentuates the morphological abnormality of a mutant that lacks CPLX0-8252 PBP5 . PBP7 may act at the septum . PBP7 localizes in the lateral wall and at the division septum; midcell localization of PBP7 is dependent on an active divisome; loss of PBP7 reduces septal PG synthesis and affects the timing of divisome assembly...

## Biological Role

Catalyzes RXN0-3461 (reaction.ecocyc.RXN0-3461).

## Annotation

FUNCTION: Cell wall formation. May play a specialized role in remodeling the cell wall. Specifically hydrolyzes the DD-diaminopimelate-alanine bonds in high-molecular-mass murein sacculi.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2134|gene.b2134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFI5`
- `KEGG:ecj:JW5355;eco:b2134;ecoc:C3026_11965;`
- `GeneID:75206381;946662;`
- `GO:GO:0000270; GO:0004175; GO:0006508; GO:0008360; GO:0009002; GO:0009252; GO:0042597; GO:0071555`
- `EC:3.4.21.-`

## Notes

D-alanyl-D-alanine endopeptidase (DD-endopeptidase) (EC 3.4.21.-) (Penicillin-binding protein 7) (PBP-7)
