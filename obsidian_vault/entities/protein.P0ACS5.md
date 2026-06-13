---
entity_id: "protein.P0ACS5"
entity_type: "protein"
name: "zntR"
source_database: "UniProt"
source_id: "P0ACS5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zntR yhdM b3292 JW3254"
---

# zntR

`protein.P0ACS5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACS5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Zinc-responsive transcriptional regulator of zntA.

## Biological Role

Component of ZntR-Zn2+ transcriptional activator (complex.ecocyc.CPLX0-7677), ZntR-Zn2+ DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7678).

## Annotation

FUNCTION: Zinc-responsive transcriptional regulator of zntA.

## Outgoing Edges (6)

- `activates` --> [[gene.b3469|gene.b3469]] `RegulonDB` `C` - regulator=ZntR; target=zntA; function=-+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7677|complex.ecocyc.CPLX0-7677]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7678|complex.ecocyc.CPLX0-7678]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=ZntR; target=rmf; function=-
- `represses` --> [[gene.b3469|gene.b3469]] `RegulonDB` `C` - regulator=ZntR; target=zntA; function=-+
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=ZntR; target=rsd; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3292|gene.b3292]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACS5`
- `KEGG:ecj:JW3254;eco:b3292;ecoc:C3026_17900;`
- `GeneID:86862310;93778695;947786;`
- `GO:GO:0000987; GO:0001216; GO:0003700; GO:0006351; GO:0008270; GO:0045893`

## Notes

HTH-type transcriptional regulator ZntR (Zn(II)-responsive regulator of zntA)
