---
entity_id: "molecule.C00669"
entity_type: "small_molecule"
name: "gamma-L-Glutamyl-L-cysteine"
source_database: "KEGG"
source_id: "C00669"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "gamma-L-Glutamyl-L-cysteine"
  - "L-gamma-Glutamylcysteine"
  - "5-L-Glutamyl-L-cysteine"
  - "gamma-Glutamylcysteine"
---

# gamma-L-Glutamyl-L-cysteine

`molecule.C00669`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00669`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: gamma-L-Glutamyl-L-cysteine; L-gamma-Glutamylcysteine; 5-L-Glutamyl-L-cysteine; gamma-Glutamylcysteine EcoCyc common name: γ-L-glutamyl-L-cysteine. L-GAMMA-GLUTAMYLCYSTEINE is the major low molecular weight thiol in halobacteria .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: gamma-L-Glutamyl-L-cysteine; L-gamma-Glutamylcysteine; 5-L-Glutamyl-L-cysteine; gamma-Glutamylcysteine

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00497|reaction.R00497]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_substrate_of` --> [[reaction.ecocyc.GLUTATHIONE-SYN-RXN|reaction.ecocyc.GLUTATHIONE-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00669`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
