---
entity_id: "protein.P36655"
entity_type: "protein"
name: "dsbD"
source_database: "UniProt"
source_id: "P36655"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbD cutA2 cycZ dipZ b4136 JW5734"
---

# dsbD

`protein.P36655`

## Static

- Type: `protein`
- Source: `UniProt:P36655`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required to facilitate the formation of correct disulfide bonds in some periplasmic proteins and for the assembly of the periplasmic c-type cytochromes. Acts by transferring electrons from cytoplasmic thioredoxin to the periplasm, thereby maintaining the active site of DsbC, DsbE and DsbG in a reduced state. This transfer involves a cascade of disulfide bond formation and reduction steps. Represents the oxidized form of thiol-disulfide exchange protein DsbD DsbD is an inner membrane protein which acts within a reductive pathway that maintains the periplasmic disulfide oxidoreductases DsbC and DsbG and the cytochrome c maturation protein CcmG in their catalytically active reduced form. DsbD mediates electron transfer from cytoplasmic thioredoxin to the periplasmic substrate proteins via inter and intra molecular disulfide exchange reactions DsbD consists of three domains: a periplasmic N-terminal domain (nDsbD or DsbDα) which contains an immunoglobulin-like fold, a central transmembrane (TM) domain (tmDsbD or DsbDβ) with eight predicted TM helices and a periplasmic C-terminal domain (cDsbD or DsbDγ) which contains a thioredoxin-like fold . Each domain contains a pair of cysteines which are essential for function...

## Biological Role

Catalyzes RXN-21410 (reaction.ecocyc.RXN-21410), RXN-24006 (reaction.ecocyc.RXN-24006).

## Annotation

FUNCTION: Required to facilitate the formation of correct disulfide bonds in some periplasmic proteins and for the assembly of the periplasmic c-type cytochromes. Acts by transferring electrons from cytoplasmic thioredoxin to the periplasm, thereby maintaining the active site of DsbC, DsbE and DsbG in a reduced state. This transfer involves a cascade of disulfide bond formation and reduction steps.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21410|reaction.ecocyc.RXN-21410]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24006|reaction.ecocyc.RXN-24006]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4136|gene.b4136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36655`
- `KEGG:ecj:JW5734;eco:b4136;ecoc:C3026_22355;`
- `GeneID:948649;`
- `GO:GO:0005886; GO:0009055; GO:0015035; GO:0017004; GO:0045454; GO:0046688; GO:0047134`
- `EC:1.8.1.8`

## Notes

Thiol:disulfide interchange protein DsbD (EC 1.8.1.8) (C-type cytochrome biogenesis protein CycZ) (Inner membrane copper tolerance protein) (Protein-disulfide reductase) (Disulfide reductase)
