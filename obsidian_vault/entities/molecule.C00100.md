---
entity_id: "molecule.C00100"
entity_type: "small_molecule"
name: "Propanoyl-CoA"
source_database: "KEGG"
source_id: "C00100"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Propanoyl-CoA"
  - "Propionyl-CoA"
  - "Propionyl coenzyme A"
---

# Propanoyl-CoA

`molecule.C00100`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00100`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Propanoyl-CoA; Propionyl-CoA; Propionyl coenzyme A

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00984` Steroid degradation (KEGG)

## Annotation

KEGG compound: Propanoyl-CoA; Propionyl-CoA; Propionyl coenzyme A

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00984` Steroid degradation (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R06987|reaction.R06987]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_product_of` --> [[reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN|reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-310|reaction.ecocyc.RXN0-310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN|reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HYDGLUTSYN-RXN|reaction.ecocyc.HYDGLUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN|reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PTAALT-RXN|reaction.ecocyc.PTAALT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9087|reaction.ecocyc.RXN-9087]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-268|reaction.ecocyc.RXN0-268]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00100`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
