---
entity_id: "molecule.C00490"
entity_type: "small_molecule"
name: "Itaconate"
source_database: "KEGG"
source_id: "C00490"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Itaconate"
  - "Itaconic acid"
  - "Methylenesuccinic acid"
---

# Itaconate

`molecule.C00490`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00490`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Itaconate; Itaconic acid; Methylenesuccinic acid ITACONATE Itaconate is an unsaturated acid with conjugated double bonds and two carboxyl groups. The acid was discovered in 1837 and named ITACONATE as an anagram of CIS-ACONITATE, from which it was first derived by Crasso in 1840 . Because of its unique structure and characteristics, itaconate and its ester are useful materials for the bioindustry. It is used for the synthesis of fiber, resin, plastic, rubber, paints, surfactant, ion-exchange resins and lubricant . ITACONATE Itaconate inhibits EC-4.1.3.1, the key enzyme of the GLYOXYLATE-BYPASS "glyoxylate shunt", which is essential for bacterial growth under specific conditions . Its production by mammalian macrophages can inhibit the growth of pathogenic bacteria and is considered an immune defense .

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Annotation

KEGG compound: Itaconate; Itaconic acid; Methylenesuccinic acid

## Pathways

- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R02404|reaction.R02404]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00490`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
