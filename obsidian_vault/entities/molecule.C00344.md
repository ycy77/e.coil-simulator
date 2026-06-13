---
entity_id: "molecule.C00344"
entity_type: "small_molecule"
name: "Phosphatidylglycerol"
source_database: "KEGG"
source_id: "C00344"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidylglycerol"
  - "3-(3-sn-Phosphatidyl)glycerol"
  - "3(3-Phosphatidyl-)glycerol"
  - "PtdGro"
---

# Phosphatidylglycerol

`molecule.C00344`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00344`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidylglycerol; 3-(3-sn-Phosphatidyl)glycerol; 3(3-Phosphatidyl-)glycerol; PtdGro EcoCyc common name: a phosphatidylglycerol. The structure of L-1-PHOSPHATIDYL-GLYCEROL phosphatidylglycerol (PG) was determined in 1958 from lipid isolates of single-cell green algae from the TAX-3087 genus . Its structure is analogous to phosphatidylinositol (PI), but with a glyceryl moiety replacing the inosityl moiety of PI. Within a decade it has been found in higher plants , Gram-negative bacteria and mammals . It was later discovered in the archaeon TAX-2246, indicating that it is produced by all three domains of life. The biosynthetic pathway was elucidated in the early 60s , and a laboratory synthesis was completed a few years later . The abundance of PG is relatively low compared with phosphatidylethanolamine (PE) in prokaryotes or with either PE or phosphatidylcholine (PC) in eukaryotes . It is typically more concentrated in plant systems than in animals, forming 1.5-4·5% of the lipid fraction Since its discovery, biochemical research into PG has been dominated by its roles in the surfactant of lung tissue (PG is the second largest lipid constituent of lung surfactant in almost all mammals), chloroplast membranes (PG is the only phospholipid found in chloroplast thylakoids) and in both bacterial and mammalian systems.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidylglycerol; 3-(3-sn-Phosphatidyl)glycerol; 3(3-Phosphatidyl-)glycerol; PtdGro

## Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (10)

- `activates` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.PGPPHOSPHA-RXN|reaction.ecocyc.PGPPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7272|reaction.ecocyc.RXN0-7272]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PGLYCEROLTRANSI-RXN|reaction.ecocyc.PGLYCEROLTRANSI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24050|reaction.ecocyc.RXN-24050]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-20|reaction.ecocyc.RXN0-20]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5223|reaction.ecocyc.RXN0-5223]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7012|reaction.ecocyc.RXN0-7012]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00344`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
