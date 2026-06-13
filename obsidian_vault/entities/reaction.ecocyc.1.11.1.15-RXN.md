---
entity_id: "reaction.ecocyc.1.11.1.15-RXN"
entity_type: "reaction"
name: "1.11.1.15-RXN"
source_database: "EcoCyc"
source_id: "1.11.1.15-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.11.1.15-RXN

`reaction.ecocyc.1.11.1.15-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.11.1.15-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Red-Thioredoxin + Alkyl-Hydro-Peroxides -> Ox-Thioredoxin + WATER + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Red-Thioredoxin + Alkyl-Hydro-Peroxides -> Ox-Thioredoxin + WATER + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipid hydroperoxide peroxidase (complex.ecocyc.CPLX0-7747), osmotically inducible peroxiredoxin OsmC (complex.ecocyc.CPLX0-8157), bcp (protein.P0AE52). Substrates: an organic hydroperoxide (molecule.ecocyc.Alkyl-Hydro-Peroxides). Products: H2O (molecule.C00001), an alcohol (molecule.ecocyc.Alcohols).

## Annotation

Red-Thioredoxin + Alkyl-Hydro-Peroxides -> Ox-Thioredoxin + WATER + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7747|complex.ecocyc.CPLX0-7747]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8157|complex.ecocyc.CPLX0-8157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AE52|protein.P0AE52]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Alkyl-Hydro-Peroxides|molecule.ecocyc.Alkyl-Hydro-Peroxides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.11.1.15-RXN`

## Notes

Red-Thioredoxin + Alkyl-Hydro-Peroxides -> Ox-Thioredoxin + WATER + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT
