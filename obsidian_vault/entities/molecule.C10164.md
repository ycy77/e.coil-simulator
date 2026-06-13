---
entity_id: "molecule.C10164"
entity_type: "small_molecule"
name: "Picolinic acid"
source_database: "KEGG"
source_id: "C10164"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Picolinic acid"
  - "2-Pyridinecarboxylic acid"
---

# Picolinic acid

`molecule.C10164`

## Static

- Type: `small_molecule`
- Source: `KEGG:C10164`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Picolinic acid; 2-Pyridinecarboxylic acid EcoCyc common name: picolinate. PICOLINATE Picolinate is a C-2-carboxylated pyridine derivate that is generated from physiological metabolism in mammalian and microbial cells . PICOLINATE Picolinate is formed spontaneously from 2-AMINOMUCONATE_SEMIALDEHYDE, an intermediate in the microbial degradation of 2-AMINOPHENOL, CATECHOL, and BENZENE-NO2 . It is also formed as a dead-end metabolite of TRP degradation by mammals , which excrete it through urine or sweat. PICOLINATE Picolinate was found to be toxic to mammalian cells, enhancing seizure activity in mice and inducing cell death via apoptosis . However, it is degraded by many different bacterial species .

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)

## Annotation

KEGG compound: Picolinic acid; 2-Pyridinecarboxylic acid

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.PPGPPSYN-RXN|reaction.ecocyc.PPGPPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C10164`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
