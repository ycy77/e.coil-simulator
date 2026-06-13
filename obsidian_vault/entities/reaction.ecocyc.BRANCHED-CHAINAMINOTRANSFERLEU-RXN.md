---
entity_id: "reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN"
entity_type: "reaction"
name: "BRANCHED-CHAINAMINOTRANSFERLEU-RXN"
source_database: "EcoCyc"
source_id: "BRANCHED-CHAINAMINOTRANSFERLEU-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BRANCHED-CHAINAMINOTRANSFERLEU-RXN

`reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BRANCHED-CHAINAMINOTRANSFERLEU-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in the synthesis of L-leucine. EcoCyc reaction equation: LEU + 2-KETOGLUTARATE -> 2K-4CH3-PENTANOATE + GLT; direction=REVERSIBLE. The final reaction in the synthesis of L-leucine.

## Biological Role

Catalyzed by branched-chain-amino-acid aminotransferase (complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX), tyrosine aminotransferase (complex.ecocyc.TYRB-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Leucine (molecule.C00123). Products: L-Glutamate (molecule.C00025), 4-Methyl-2-oxopentanoate (molecule.C00233).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

The final reaction in the synthesis of L-leucine.

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00233|molecule.C00233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:BRANCHED-CHAINAMINOTRANSFERLEU-RXN`

## Notes

LEU + 2-KETOGLUTARATE -> 2K-4CH3-PENTANOATE + GLT; direction=REVERSIBLE
