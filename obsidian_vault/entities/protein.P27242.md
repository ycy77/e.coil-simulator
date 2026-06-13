---
entity_id: "protein.P27242"
entity_type: "protein"
name: "waaU"
source_database: "UniProt"
source_id: "P27242"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaU rfaK waaK b3623 JW3598"
---

# waaU

`protein.P27242`

## Static

- Type: `protein`
- Source: `UniProt:P27242`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May catalyze the addition of the terminal heptose (heptose IV) to the outer-core glucose III, the last step of the lipid A-core oligosaccharide biosynthesis (Probable). {ECO:0000269|PubMed:1385388, ECO:0000305|PubMed:9791168}. WaaU is a putative ADP-heptose:LPS heptosyltransferase which may be responsible for the attachment of the fourth heptose residue (HepIV) residue to the third glucose (GlcIII) residue in the outer core of K-12 lipopolysaccharide; WaaU contains 2 glycosyltransferase motifs and shares regions of local similarity with the EG11189-MONOMER "WaaC" and EG12210 "WaaF" heptosyltransferases . O-antigen cannot be detected in the waaU (formerly rfaK) knockout mutant (rfaK2::ΩKMr) of an E. coli K-12 strain engineered to express Shigella dysenteriae O-antigen . WaaU is implicated in phage specificity: in contrast to the parental strain, an E. coli K-12 waaU knockout mutant is sensitive to the rough specific phage Br2; WaaU may be a transferase which adds N-acetyl D-glucosamine (GlcNAc) to an inner core heptose . It is also possible that WaaU mediates the non stoichiometric substitution of HepIV with an N-acetyl D-glucosamine residue as shown CPD0-939 "here" (see )...

## Biological Role

Catalyzes RXN0-5127 (reaction.ecocyc.RXN0-5127).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May catalyze the addition of the terminal heptose (heptose IV) to the outer-core glucose III, the last step of the lipid A-core oligosaccharide biosynthesis (Probable). {ECO:0000269|PubMed:1385388, ECO:0000305|PubMed:9791168}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5127|reaction.ecocyc.RXN0-5127]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3623|gene.b3623]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27242`
- `KEGG:ecj:JW3598;eco:b3623;ecoc:C3026_19640;`
- `GeneID:948147;`
- `GO:GO:0005829; GO:0008713; GO:0009103; GO:0009244; GO:0071968`
- `EC:2.4.1.-`

## Notes

Putative lipopolysaccharide heptosyltransferase 4 (EC 2.4.1.-) (ADP-heptose:LPS heptosyltransferase 4) (HepIV transferase)
