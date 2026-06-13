---
entity_id: "protein.P21165"
entity_type: "protein"
name: "pepQ"
source_database: "UniProt"
source_id: "P21165"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepQ b3847 JW3823"
---

# pepQ

`protein.P21165`

## Static

- Type: `protein`
- Source: `UniProt:P21165`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Splits dipeptides with a prolyl residue in the C-terminal position and a polar or nonpolar amino acid at the N-terminal position. With much lower efficiency, also catalyzes the stereoselective hydrolysis of a wide variety of organophosphate triesters and organophosphonate diesters. Is able to hydrolyze the organophosphorus insecticide paraoxon and the p-nitrophenyl analogs of the nerve agents GB (sarin), GD (soman), GF, Vx and rVX. {ECO:0000269|PubMed:15313226}.

## Biological Role

Component of Xaa-Pro dipeptidase (complex.ecocyc.CPLX0-8156).

## Annotation

FUNCTION: Splits dipeptides with a prolyl residue in the C-terminal position and a polar or nonpolar amino acid at the N-terminal position. With much lower efficiency, also catalyzes the stereoselective hydrolysis of a wide variety of organophosphate triesters and organophosphonate diesters. Is able to hydrolyze the organophosphorus insecticide paraoxon and the p-nitrophenyl analogs of the nerve agents GB (sarin), GD (soman), GF, Vx and rVX. {ECO:0000269|PubMed:15313226}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8156|complex.ecocyc.CPLX0-8156]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3847|gene.b3847]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21165`
- `KEGG:ecj:JW3823;eco:b3847;ecoc:C3026_20800;`
- `GeneID:86861950;948335;`
- `GO:GO:0004177; GO:0005829; GO:0006508; GO:0016795; GO:0016805; GO:0030145; GO:0042803; GO:0043171; GO:0070573; GO:0102009`
- `EC:3.4.13.9`

## Notes

Xaa-Pro dipeptidase (X-Pro dipeptidase) (EC 3.4.13.9) (Imidodipeptidase) (Proline dipeptidase) (Prolidase)
