---
entity_id: "molecule.C06026"
entity_type: "small_molecule"
name: "KDO2-lipid A"
source_database: "KEGG"
source_id: "C06026"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "KDO2-lipid A"
  - "Di[3-deoxy-D-manno-octulosonyl]-lipid A"
  - "alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-lipid A"
  - "Dodecanoyl-(tetradecanoyl)-KDO2-lipid IV(A)"
---

# KDO2-lipid A

`molecule.C06026`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06026`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: KDO2-lipid A; Di[3-deoxy-D-manno-octulosonyl]-lipid A; alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-lipid A; Dodecanoyl-(tetradecanoyl)-KDO2-lipid IV(A) EcoCyc common name: α-D-Kdo-(2→4)-α-D-Kdo-(2→6)-lipid A (E. coli).

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: KDO2-lipid A; Di[3-deoxy-D-manno-octulosonyl]-lipid A; alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-lipid A; Dodecanoyl-(tetradecanoyl)-KDO2-lipid IV(A)

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.MYRISTOYLACYLTRAN-RXN|reaction.ecocyc.MYRISTOYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R09781|reaction.R09781]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16281|reaction.ecocyc.RXN-16281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16286|reaction.ecocyc.RXN-16286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20918|reaction.ecocyc.RXN-20918]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2001|reaction.ecocyc.RXN0-2001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5118|reaction.ecocyc.RXN0-5118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06026`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
