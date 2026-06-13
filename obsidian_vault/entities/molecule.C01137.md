---
entity_id: "molecule.C01137"
entity_type: "small_molecule"
name: "S-Adenosylmethioninamine"
source_database: "KEGG"
source_id: "C01137"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Adenosylmethioninamine"
  - "(5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium"
  - "(5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium cation"
  - "S-Adenosyl-(5')-3-methylthiopropylamine"
  - "S-Adenosyl 3-(methylthio)propylamine"
  - "S-Adenosyl 3-(methylsulfanyl)propylamine"
  - "Decarboxy-AdoMet"
---

# S-Adenosylmethioninamine

`molecule.C01137`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01137`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Adenosylmethioninamine; (5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium; (5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium cation; S-Adenosyl-(5')-3-methylthiopropylamine; S-Adenosyl 3-(methylthio)propylamine; S-Adenosyl 3-(methylsulfanyl)propylamine; Decarboxy-AdoMet EcoCyc common name: S-adenosyl 3-(methylsulfanyl)propylamine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)

## Annotation

KEGG compound: S-Adenosylmethioninamine; (5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium; (5-Deoxy-5-adenosyl)(3-aminopropyl)methylsulfonium cation; S-Adenosyl-(5')-3-methylthiopropylamine; S-Adenosyl 3-(methylthio)propylamine; S-Adenosyl 3-(methylsulfanyl)propylamine; Decarboxy-AdoMet

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00178|reaction.R00178]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011
- `is_product_of` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5217|reaction.ecocyc.RXN0-5217]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01137`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
