---
entity_id: "molecule.C00369"
entity_type: "small_molecule"
name: "Starch"
source_database: "KEGG"
source_id: "C00369"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Starch"
  - "Glycogen"
---

# Starch

`molecule.C00369`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00369`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Starch; Glycogen Starch is a glucose-based polysaccharide produced by plants, green algae, and cyanobacteria. Starch combines two polymeric carbohydrates (polysaccharides) called Alpha-Amyloses "α-amylose" and CPD-7043. Alpha-Amyloses "α-Amylose" contains up to several thousand α-glucosyl units linked almost exclusively in linear α(1->4) linkages, with very few branches of α(1->6) linkages. In CPD-7043, on the other hand, branching is common, and occurs approximately every 24-30 glucose monomer units. Amylopectin is one of (if not the) largest biological polymer known and contains from 105–106 glucose residues . Unlike Glycogens glycogen molecules, which is limited to ~55,000 glucose units, the starch branched structure leads to clusters of chains that allow for indefinite growth of the polysaccharide. Alpha-Amyloses "α-Amylose" accounts for 30% of starch, while CPD-7043 accounts for the other 70%. The dense packing of branches at the root of the clusters generates tightly packed glucan chains that are close enough to align and form parallel double helical structures. The helices within a single cluster and neighbouring clusters align and form sections of crystalline structures separated by sections of amorphous material (containing the branches) thereby generating the semi-crystalline nature of amylopectin and of the ensuing starch granule...

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: Starch; Glycogen

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R02108|reaction.R02108]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_product_of` --> [[reaction.R02110|reaction.R02110]] `KEGG` `database` - C00718 <=> C00369
- `is_substrate_of` --> [[reaction.R02108|reaction.R02108]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_substrate_of` --> [[reaction.R02111|reaction.R02111]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_substrate_of` --> [[reaction.R02112|reaction.R02112]] `KEGG` `database` - C00369 <=> C00721 + C00208

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00369`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
