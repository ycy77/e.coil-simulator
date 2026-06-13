---
entity_id: "protein.P69681"
entity_type: "protein"
name: "amtB"
source_database: "UniProt"
source_id: "P69681"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:12023896, ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:17040913}; Multi-pass membrane protein {ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:17040913}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amtB ybaG b0451 JW0441"
---

# amtB

`protein.P69681`

## Static

- Type: `protein`
- Source: `UniProt:P69681`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:12023896, ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:17040913}; Multi-pass membrane protein {ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:17040913}.

## Enriched Summary

FUNCTION: Involved in the uptake of ammonium/ammonia (NH(4)(+)/NH(3)) (PubMed:14668330, PubMed:15361618, PubMed:15563598, PubMed:15876187, PubMed:16910683, PubMed:30211659, PubMed:32662768). Transport is electrogenic (PubMed:30211659, PubMed:32662768). Following sequestration of NH(4)(+) at the periplasmic face, NH(4)(+) is deprotonated and neutral NH(3) is transported into the cytoplasm (PubMed:15876187, PubMed:16910683, PubMed:18362341, PubMed:19278252, PubMed:32662768). Neutral NH(3) and charged H(+) are carried separately across the membrane on a unique two-lane pathway, before recombining to NH(4)(+) inside the cell (PubMed:32662768). In vitro can also transport the larger analogs methylamine and methylammonium (PubMed:11847102, PubMed:12023896, PubMed:14668330, PubMed:15876187, PubMed:17998534, PubMed:18362341). Also acts as a sensor of the extracellular ammonium concentration (PubMed:14668330). {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:12023896, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:15876187, ECO:0000269|PubMed:16910683, ECO:0000269|PubMed:17998534, ECO:0000269|PubMed:18362341, ECO:0000269|PubMed:19278252, ECO:0000269|PubMed:30211659, ECO:0000269|PubMed:32662768}...

## Biological Role

Component of ammonium transporter (complex.ecocyc.CPLX0-7532).

## Annotation

FUNCTION: Involved in the uptake of ammonium/ammonia (NH(4)(+)/NH(3)) (PubMed:14668330, PubMed:15361618, PubMed:15563598, PubMed:15876187, PubMed:16910683, PubMed:30211659, PubMed:32662768). Transport is electrogenic (PubMed:30211659, PubMed:32662768). Following sequestration of NH(4)(+) at the periplasmic face, NH(4)(+) is deprotonated and neutral NH(3) is transported into the cytoplasm (PubMed:15876187, PubMed:16910683, PubMed:18362341, PubMed:19278252, PubMed:32662768). Neutral NH(3) and charged H(+) are carried separately across the membrane on a unique two-lane pathway, before recombining to NH(4)(+) inside the cell (PubMed:32662768). In vitro can also transport the larger analogs methylamine and methylammonium (PubMed:11847102, PubMed:12023896, PubMed:14668330, PubMed:15876187, PubMed:17998534, PubMed:18362341). Also acts as a sensor of the extracellular ammonium concentration (PubMed:14668330). {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:12023896, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:15361618, ECO:0000269|PubMed:15563598, ECO:0000269|PubMed:15876187, ECO:0000269|PubMed:16910683, ECO:0000269|PubMed:17998534, ECO:0000269|PubMed:18362341, ECO:0000269|PubMed:19278252, ECO:0000269|PubMed:30211659, ECO:0000269|PubMed:32662768}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7532|complex.ecocyc.CPLX0-7532]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0451|gene.b0451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69681`
- `KEGG:ecj:JW0441;eco:b0451;ecoc:C3026_02210;`
- `GeneID:86862996;93776999;945084;`
- `GO:GO:0005886; GO:0008519; GO:0015670; GO:0042802; GO:0072488`

## Notes

Ammonium transporter AmtB (Ammonia channel AmtB) (Ammonium channel AmtB)
