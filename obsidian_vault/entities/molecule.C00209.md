---
entity_id: "molecule.C00209"
entity_type: "small_molecule"
name: "Oxalate"
source_database: "KEGG"
source_id: "C00209"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxalate"
  - "Oxalic acid"
  - "Ethanedioic acid"
---

# Oxalate

`molecule.C00209`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00209`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxalate; Oxalic acid; Ethanedioic acid OXALATE Oxalate is the most oxidized two-carbon compound. It is made in high concentrations by some plants and fungi and can reach high micromolar concentrations in soil. Oxalate is toxic to mammals but is metabolized by many bacteria and plants by various pathways. In high concentrations, it causes death in humans and animals because of its corrosive effects, while smaller amounts can cause various pathological disorders, including hyperoxaluria, calcium oxalate stones, pyridoxine deficiency, and even renal failure. In oxalate-accumulating plants, calcium oxalate crystal accumulation occurs in specialized idioblast cells. The crystals are thought to deter herbivore feeding and may also serve a role in regulating free calcium levels .

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: Oxalate; Oxalic acid; Ethanedioic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (13)

- `is_substrate_of` --> [[reaction.R07290|reaction.R07290]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7075|reaction.ecocyc.RXN0-7075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN|reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.2.7.3.9-RXN|reaction.ecocyc.2.7.3.9-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DLACTDEHYDROGFAD-RXN|reaction.ecocyc.DLACTDEHYDROGFAD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00209`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
