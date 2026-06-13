---
entity_id: "reaction.ecocyc.RXN0-7310"
entity_type: "reaction"
name: "RXN0-7310"
source_database: "EcoCyc"
source_id: "RXN0-7310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7310

`reaction.ecocyc.RXN0-7310`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7310`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

The thiol:disulfide exchange reaction catalyzed by DsbA is a bimolecular nucleophilic substitution reaction (SN2) (see for details) EcoCyc reaction equation: an-oxidized-DsbA-protein + Protein-Dithiols -> a-reduced-DsbA-protein + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT. The thiol:disulfide exchange reaction catalyzed by DsbA is a bimolecular nucleophilic substitution reaction (SN2) (see for details)

## Biological Role

Substrates: a [protein]-dithiol (molecule.ecocyc.Protein-Dithiols). Products: a [protein]-disulfide (molecule.ecocyc.Protein-Disulfides).

## Enriched Pathways

- `ecocyc.PWY0-1599` periplasmic disulfide bond formation (EcoCyc)

## Annotation

The thiol:disulfide exchange reaction catalyzed by DsbA is a bimolecular nucleophilic substitution reaction (SN2) (see for details)

## Pathways

- `ecocyc.PWY0-1599` periplasmic disulfide bond formation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.Protein-Disulfides|molecule.ecocyc.Protein-Disulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Dithiols|molecule.ecocyc.Protein-Dithiols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7310`

## Notes

an-oxidized-DsbA-protein + Protein-Dithiols -> a-reduced-DsbA-protein + Protein-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT
