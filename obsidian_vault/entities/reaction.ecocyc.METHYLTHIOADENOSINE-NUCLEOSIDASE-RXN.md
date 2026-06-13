---
entity_id: "reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-METHYLTHIOADENOSINE + WATER -> CPD-560 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-METHYLTHIOADENOSINE + WATER -> CPD-560 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (complex.ecocyc.CPLX0-1541). Substrates: H2O (molecule.C00001), 5'-Methylthioadenosine (molecule.C00170). Products: Adenine (molecule.C00147), 5-Methylthio-D-ribose (molecule.C03089).

## Enriched Pathways

- `ecocyc.PWY0-1391` S-methyl-5'-thioadenosine degradation IV (EcoCyc)

## Annotation

5-METHYLTHIOADENOSINE + WATER -> CPD-560 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1391` S-methyl-5'-thioadenosine degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1541|complex.ecocyc.CPLX0-1541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03089|molecule.C03089]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-N-PROPYLTHIOADENOSINE|molecule.ecocyc.5-N-PROPYLTHIOADENOSINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-P-NITROPHENYLTHIOADENOSINE|molecule.ecocyc.5-P-NITROPHENYLTHIOADENOSINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN`

## Notes

5-METHYLTHIOADENOSINE + WATER -> CPD-560 + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
