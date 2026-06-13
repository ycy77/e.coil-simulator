---
entity_id: "molecule.C01502"
entity_type: "small_molecule"
name: "o-Methoxyphenol"
source_database: "KEGG"
source_id: "C01502"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "o-Methoxyphenol"
  - "Guaiacol"
  - "Catechol mono methyl ether"
  - "2-Methoxyphenol"
---

# o-Methoxyphenol

`molecule.C01502`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01502`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: o-Methoxyphenol; Guaiacol; Catechol mono methyl ether; 2-Methoxyphenol EcoCyc common name: guaiacol.

## Enriched Pathways

- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: o-Methoxyphenol; Guaiacol; Catechol mono methyl ether; 2-Methoxyphenol

## Pathways

- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01502`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
