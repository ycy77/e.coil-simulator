---
entity_id: "molecule.C00580"
entity_type: "small_molecule"
name: "Dimethyl sulfide"
source_database: "KEGG"
source_id: "C00580"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dimethyl sulfide"
  - "Methyl sulfide"
  - "Methyl thioether"
  - "DMS"
---

# Dimethyl sulfide

`molecule.C00580`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00580`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dimethyl sulfide; Methyl sulfide; Methyl thioether; DMS CPD-7670 Dimethylsulfide (DMS) is a major contributor to the total sulfur emissions to the atmosphere from land and the ocean. In marine, estuarine, and salt marsh systems, the main source of DMS is the degradation of SS-DIMETHYL-BETA-PROPIOTHETIN (DMSP), an osmolyte of many marine algae and certain plants . DMSP is readily degraded in a variety of biological systems, including bacterial cultures, salt marsh sediments, and seawater samples containing algae and zooplankton . There are two main routes for DMSP degradation, leading to formation of either CPD-7670 or CPD-7672. Other sources for DMS include the reduction of DMSO, the methylation of CPD-7671, and the degradation of sulfur-containing amino acids. DMS, which is very volatile, is exchanged freely between the ocean and the atmosphere, and is considered the main natural source of sulfur to the atmosphere. Once in the troposphere, DMS is oxidized to SULFATE and CPD-3746, which attract water and promote cloud formation and thus influence the climate . However, up to 90% of the DMS in the ocean is degraded biologically . DMS is toxic, and attempts to isolate in pure culture DMS-degrading organisms that can use it as the sole carbon and energy source have been often unsuccessful due to this toxicity...

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Dimethyl sulfide; Methyl sulfide; Methyl thioether; DMS

## Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5262|reaction.ecocyc.RXN0-5262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIMESULFREDUCT-RXN|reaction.ecocyc.DIMESULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00580`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
