---
entity_id: "molecule.C00714"
entity_type: "small_molecule"
name: "Pectin"
source_database: "KEGG"
source_id: "C00714"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pectin"
  - "Poly(1,4-alpha-D-galacturonide)"
---

# Pectin

`molecule.C00714`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00714`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pectin; Poly(1,4-alpha-D-galacturonide) EcoCyc common name: a pectin. Pectin "Pectin" is a structural heteropolysaccharide consisting of a complex set of polysaccharides that is present in most primary cell walls and is particularly abundant in the non-woody parts of terrestrial plants. It is involved in crosslinking cellulose and hemicellulose fibers, which provides rigidity to the cell wall. The characteristic structure of pectin is a linear chain of α-(1-4)-linked D-GALACTURONATE that forms the pectin-backbone, 1-4-alpha-D-galacturonosyl. Diferent components of pectin have different substitutions and additions. A common type is Rhamnogalacturonans-I "rhamnogalacturonan I" (RG-I), which makes up 20-35% of pectin. In RG-I some of the D-GALACTURONATE units in the backbone are replaced by (1-2)-linked L-rhamnose, to which side chains of various neutral sugars branch off, mostly D-Galactose, L-ARABINOSE and CPD-25028. Another common type is CPD-14581 "rhamnogalacturonan II" (RG-II), which makes up about 10% of pectin. RG-II is based on a backbone of 8-9 galacturonate units, which are decorated by four side chains consisting of 12 different types of sugars in more than 20 different linkages. RG-II usually forms dimeric structures via the formation of crosslinks by a 1:2 borate diol ester between apiosyl residues in one of the side chains...

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: Pectin; Poly(1,4-alpha-D-galacturonide)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.R02362|reaction.R02362]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00714`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
