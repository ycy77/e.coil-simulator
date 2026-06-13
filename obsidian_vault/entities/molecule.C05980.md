---
entity_id: "molecule.C05980"
entity_type: "small_molecule"
name: "Cardiolipin"
source_database: "KEGG"
source_id: "C05980"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cardiolipin"
  - "Diphosphatidylglycerol"
  - "1',3'-Bis(1,2-diacyl-sn-glycero-3-phospho)-sn-glycerol"
---

# Cardiolipin

`molecule.C05980`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05980`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cardiolipin; Diphosphatidylglycerol; 1',3'-Bis(1,2-diacyl-sn-glycero-3-phospho)-sn-glycerol EcoCyc common name: a cardiolipin. A cardiolipin is a diphosphatidylglycerol, composed of two L-PHOSPHATIDATE phosphatidate molecules covalently linked to a molecule of glycerol at positions 1 and 3. It is an abundant anionic lipid in bacteria and in eukaryotes , where it is exclusively present in the inner mitochondrial membrane. Cardiolipin was first isolated from beef heart , hence its name. Many enzymes involved in energy metabolism interact with cardiolipin. EC-7.1.1.9, also known as Complex IV, requires two associated cardiolipin molecules in order to maintain its full enzymatic function . EC-7.1.1.8 (cytochrome bc1, Complex III) also needs cardiolipin to maintain its quaternary structure and functional role . EC-7.1.2.2 (Complex V) binds four molecules of cardiolipin .

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Cardiolipin; Diphosphatidylglycerol; 1',3'-Bis(1,2-diacyl-sn-glycero-3-phospho)-sn-glycerol

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (10)

- `activates` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.TETRAACYLDISACC4KIN-RXN|reaction.ecocyc.TETRAACYLDISACC4KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7012|reaction.ecocyc.RXN0-7012]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.3.4.21.53-RXN|reaction.ecocyc.3.4.21.53-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05980`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
