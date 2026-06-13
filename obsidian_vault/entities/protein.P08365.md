---
entity_id: "protein.P08365"
entity_type: "protein"
name: "chpS"
source_database: "UniProt"
source_id: "P08365"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chpS chpBI yjfB b4224 JW5750"
---

# chpS

`protein.P08365`

## Static

- Type: `protein`
- Source: `UniProt:P08365`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. May be involved in the regulation of cell growth. It acts as a suppressor of the endoribonuclease (inhibitory function) of ChpB protein. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:8226627}. ChpS is the antitoxin component of the ChpB-ChpS toxin-antitoxin system. See the the ChpB-ChpS complex entry for an explanAtion of ChpS's role in regulating this system.

## Biological Role

Component of ChpB-ChpS complex (complex.ecocyc.CPLX0-7561).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. May be involved in the regulation of cell growth. It acts as a suppressor of the endoribonuclease (inhibitory function) of ChpB protein. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:8226627}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7561|complex.ecocyc.CPLX0-7561]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4224|gene.b4224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08365`
- `KEGG:ecj:JW5750;eco:b4224;ecoc:C3026_22810;`
- `GeneID:75169746;75202463;948739;`
- `GO:GO:0003677; GO:0006355; GO:0030307; GO:0040008; GO:0044010; GO:0097351; GO:0110001`

## Notes

Antitoxin ChpS
