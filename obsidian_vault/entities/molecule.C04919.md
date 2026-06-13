---
entity_id: "molecule.C04919"
entity_type: "small_molecule"
name: "2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate"
source_database: "KEGG"
source_id: "C04919"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate"
  - "2,3,2'3'-Tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate"
  - "Lipid A disaccharide bisphosphate"
  - "Lipid IV(A)"
  - "Lipid IVA"
  - "2-Deoxy-2-{[(3R)-3-hydroxytetradecanoyl]amino}-3-O-[(3R)-3-hydroxytetradecanoyl]-4-O-phospho-beta-D-glucopyranosyl-(1->6)-2-deoxy-3-O-[(3R)-3-hydroxytetradecanoyl]-2-{[(3R)-3-hydroxytetradecanoyl]amino}-1-O-phospho-alpha-D-glucopyranose"
---

# 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate

`molecule.C04919`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04919`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; 2,3,2'3'-Tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; Lipid A disaccharide bisphosphate; Lipid IV(A); Lipid IVA; 2-Deoxy-2-{[(3R)-3-hydroxytetradecanoyl]amino}-3-O-[(3R)-3-hydroxytetradecanoyl]-4-O-phospho-beta-D-glucopyranosyl-(1->6)-2-deoxy-3-O-[(3R)-3-hydroxytetradecanoyl]-2-{[(3R)-3-hydroxytetradecanoyl]amino}-1-O-phospho-alpha-D-glucopyranose EcoCyc common name: lipid IVA (E. coli). LIPID-IV-A "Lipid IVA (E. coli)" is a tetra-acylated Lipid-A "lipid A" produced by TAX-562 as an intermediate in the lipid A biosynthetic pathway.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; 2,3,2'3'-Tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; Lipid A disaccharide bisphosphate; Lipid IV(A); Lipid IVA; 2-Deoxy-2-{[(3R)-3-hydroxytetradecanoyl]amino}-3-O-[(3R)-3-hydroxytetradecanoyl]-4-O-phospho-beta-D-glucopyranosyl-(1->6)-2-deoxy-3-O-[(3R)-3-hydroxytetradecanoyl]-2-{[(3R)-3-hydroxytetradecanoyl]amino}-1-O-phospho-alpha-D-glucopyranose

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R04657|reaction.R04657]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919
- `is_product_of` --> [[reaction.ecocyc.TETRAACYLDISACC4KIN-RXN|reaction.ecocyc.TETRAACYLDISACC4KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04658|reaction.R04658]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_substrate_of` --> [[reaction.R09773|reaction.R09773]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556
- `is_substrate_of` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20919|reaction.ecocyc.RXN-20919]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04919`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
