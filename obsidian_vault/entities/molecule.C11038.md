---
entity_id: "molecule.C11038"
entity_type: "small_molecule"
name: "2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate"
source_database: "KEGG"
source_id: "C11038"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate"
---

# 2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate

`molecule.C11038`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11038`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate EcoCyc common name: hydroxymethyl-dCDP.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: 2'-Deoxy-5-hydroxymethylcytidine-5'-diphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_substrate_of` --> [[reaction.R00139|reaction.R00139]] `KEGG` `database` - C11038 + C00002 <=> C11039 + C00008

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11038`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
