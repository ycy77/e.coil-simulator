---
entity_id: "molecule.C01083"
entity_type: "small_molecule"
name: "alpha,alpha-Trehalose"
source_database: "KEGG"
source_id: "C01083"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha,alpha-Trehalose"
  - "alpha,alpha'-Trehalose"
  - "Trehalose"
---

# alpha,alpha-Trehalose

`molecule.C01083`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01083`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha,alpha-Trehalose; alpha,alpha'-Trehalose; Trehalose EcoCyc common name: α,α-trehalose. The name trehalose was introduced in 1858 to describe a main constituent of shells that are secreted by various insects on tree leaves in the middle east. These shells were often dried and used as a sweetening agents, and are believed to be related to the biblical Manna, the food supplied to the Israelites in their journey through the wilderness of Arabia. One variety of these shells, produced by some beetles from the TAX-202007 genus (Larinus maculatus and Larinus nidificans) was called "trehala manna", and the sugar extracted from it was named trehalique glucose, or trehalose . In fact, TREHALOSE is a disaccharide that is ubiquitous in the biosphere. It consists of two subunits of glucose bound by their reducing ends in an α:1-1 linkage (α-D-glucopyranosyl α-D-glucopyranoside) and thus does not have a reducing end. Trehalose has been isolated and characterized from many prokaryotic and eukaryotic organisms, including bacteria, yeast, plants, insects and mammals . In addition to being nonreducing, trehalose possesses several unique properties, including high hydrophilicity, chemical stability, nonhygroscopic glass formation and no internal hydrogen bond formation. The combination of these features explains the principal role of trehalose as a stress metabolite...

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: alpha,alpha-Trehalose; alpha,alpha'-Trehalose; Trehalose

## Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TREHALOSEPHOSPHA-RXN|reaction.ecocyc.TREHALOSEPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00010|reaction.R00010]] `KEGG` `database` - C01083 + C00001 <=> 2 C00031
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-168|reaction.ecocyc.TRANS-RXN-168]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TREHALA-RXN|reaction.ecocyc.TREHALA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01083`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
