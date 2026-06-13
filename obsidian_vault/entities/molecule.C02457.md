---
entity_id: "molecule.C02457"
entity_type: "small_molecule"
name: "Propane-1,3-diol"
source_database: "KEGG"
source_id: "C02457"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Propane-1,3-diol"
  - "1,3-Propanediol"
  - "Trimethylene glycol"
---

# Propane-1,3-diol

`molecule.C02457`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02457`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Propane-1,3-diol; 1,3-Propanediol; Trimethylene glycol EcoCyc common name: 1,3-propanediol. CPD-347 (PDO) is produced in nature by a large number of bacteria, including Citrobacter, Clostridium, Enterobacter, Klebsiella and Lactobacillus species, via the fermentation of GLYCEROL. A common problem with anaerobic growth is the generation of excess reducing equivalents in the form of NADH, whose reoxidation to NAD+ requires formation of a by-product that can serve as an electron sink. In the case of glycerol, the process comprises two steps - the rearrangement of glycerol to HYDROXYPROPANAL, followed by its NADH-dependent reduction to CPD-347, which is excreted from the cell. PDO is used for the production of poly(propylene terephtalate), a polyester prepared from TEREPHTHALATE and PDO that has highly desired properties for some large volume markets (such as fibers used in apparel and carpet applications). The pathway PWY-7385 describes the production of PDO from D-glucose in an engineered TAX-562 strain that incorporates glycerol fermentation enzymes from TAX-573 and TAX-4932.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Annotation

KEGG compound: Propane-1,3-diol; 1,3-Propanediol; Trimethylene glycol

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6487|reaction.ecocyc.RXN0-6487]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02457`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
