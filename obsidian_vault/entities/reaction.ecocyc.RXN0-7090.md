---
entity_id: "reaction.ecocyc.RXN0-7090"
entity_type: "reaction"
name: "RXN0-7090"
source_database: "EcoCyc"
source_id: "RXN0-7090"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7090

`reaction.ecocyc.RXN0-7090`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7090`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

50S-Ribosomal-subunit-protein-L16-Arg + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 50S-Ribo-protein-L16-Hydroxylarginine + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 50S-Ribosomal-subunit-protein-L16-Arg + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 50S-Ribo-protein-L16-Hydroxylarginine + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 50S ribosomal protein L16-arginine 3-hydroxylase (complex.ecocyc.CPLX0-8112). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), a [50S ribosomal subunit protein L16]-L-arginine81 (molecule.ecocyc.50S-Ribosomal-subunit-protein-L16-Arg). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), a [50S ribosomal subunit protein L16]-(3R)-3-hydroxy-L-arginine81 (molecule.ecocyc.50S-Ribo-protein-L16-Hydroxylarginine).

## Annotation

50S-Ribosomal-subunit-protein-L16-Arg + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 50S-Ribo-protein-L16-Hydroxylarginine + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8112|complex.ecocyc.CPLX0-8112]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.50S-Ribo-protein-L16-Hydroxylarginine|molecule.ecocyc.50S-Ribo-protein-L16-Hydroxylarginine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.50S-Ribosomal-subunit-protein-L16-Arg|molecule.ecocyc.50S-Ribosomal-subunit-protein-L16-Arg]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7090`

## Notes

50S-Ribosomal-subunit-protein-L16-Arg + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> 50S-Ribo-protein-L16-Hydroxylarginine + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
