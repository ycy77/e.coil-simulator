---
entity_id: "reaction.ecocyc.TRANS-RXN0-466"
entity_type: "reaction"
name: "TRANS-RXN0-466"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-466"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-466

`reaction.ecocyc.TRANS-RXN0-466`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-466`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Trans-cinnamate can induce the hca genes in E. coli and is converted to 2,3-dihydroxy-trans-cinnamate but E. coli cannot grow on trans-cinnamate as the sole source of carbon . EcoCyc reaction equation: CPD-674 -> CPD-674; direction=LEFT-TO-RIGHT. Trans-cinnamate can induce the hca genes in E. coli and is converted to 2,3-dihydroxy-trans-cinnamate but E. coli cannot grow on trans-cinnamate as the sole source of carbon .

## Biological Role

Substrates: trans-Cinnamate (molecule.C00423). Products: trans-Cinnamate (molecule.C00423).

## Annotation

Trans-cinnamate can induce the hca genes in E. coli and is converted to 2,3-dihydroxy-trans-cinnamate but E. coli cannot grow on trans-cinnamate as the sole source of carbon .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00423|molecule.C00423]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00423|molecule.C00423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-466`

## Notes

CPD-674 -> CPD-674; direction=LEFT-TO-RIGHT
