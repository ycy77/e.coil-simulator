---
entity_id: "molecule.C00089"
entity_type: "small_molecule"
name: "Sucrose"
source_database: "KEGG"
source_id: "C00089"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Sucrose"
  - "Cane sugar"
  - "Saccharose"
  - "1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside"
---

# Sucrose

`molecule.C00089`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00089`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Sucrose; Cane sugar; Saccharose; 1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside SUCROSE Sucrose is the major product of photosynthesis in most plants and is known to be essential for their growth, development, carbon storage, signal transduction and stress protection . Sucrose is also found in cyanobacteria, and the ability to synthesize sucrose is a widespread feature of these organisms . In addition, sucrose is produced by many nonphotosynthetic aerobic methanotrophic and methanol-utilizing bacteria . In photosynthetic organisms, the product of photosynthetic carbon fixation (GAP) is transported from the chloroplast into the cytoplasm, where it is transformed to hexose phosphate by enzymes of the GLUCONEO-PWY gluconeogenesis pathway. In plants, these hexose phosphates are used to synthesize sucrose, the form in which most fixed organic carbon is translocated from photosynthetic tissue to non-photosynthetic organs. Sucrose also provides substrates for plant storage glycosides such as Starch starch and Fructans fructans. Storage glycosides, including sucrose, are mobilized and utilized during seed germination and plant growth. In marine and freshwater cyanobacteria sucrose fulfils a different role...

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Sucrose; Cane sugar; Saccharose; 1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R00801|reaction.R00801]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_substrate_of` --> [[reaction.R00802|reaction.R00802]] `KEGG` `database` - C00089 + C00001 <=> C02336 + C00267

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00089`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
