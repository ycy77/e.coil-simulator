---
entity_id: "protein.P27830"
entity_type: "protein"
name: "rffG"
source_database: "UniProt"
source_id: "P27830"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rffG b3788 JW5598"
---

# rffG

`protein.P27830`

## Static

- Type: `protein`
- Source: `UniProt:P27830`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000269|PubMed:11380254, ECO:0000269|PubMed:11601973, ECO:0000269|PubMed:7559340}. dTDP-glucose 4,6-dehydratase 2 (RffG) is involved in the biosynthesis of enterobacterial common antigen (ECA). This enzyme catalyzes the conversion of dTDP-α-D-glucose into dTDP-4-keto-6-deoxyglucose. This reaction occurs in three steps: dehydrogenation, dehydration, and rereduction. The coenzyme NAD+ mediates the dehydrogenation and rereduction steps of the reaction. . dTDP-glucose 4,6-dehydratase is encoded by the rffG gene which is paralogous to rfbB. The product of rfbB is another dTDP-glucose 4,6-dehydratase which catalyzes the same reaction as RffG, but functions in the rhamnose biosynthesis pathway . A model of the active site has been generated and site directed mutagenesis studies have identified several residues which are essential for catalysis . Specific residues which are the acid and base catalysts for the dehydration step have been determined .

## Biological Role

Catalyzes DTDPGLUCDEHYDRAT-RXN (reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN). Bound by NAD+ (molecule.C00003).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000269|PubMed:11380254, ECO:0000269|PubMed:11601973, ECO:0000269|PubMed:7559340}.

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN|reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3788|gene.b3788]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27830`
- `KEGG:ecj:JW5598;eco:b3788;ecoc:C3026_20510;`
- `GeneID:948300;`
- `GO:GO:0000271; GO:0008460; GO:0009103; GO:0009225; GO:0009246`
- `EC:4.2.1.46`

## Notes

dTDP-glucose 4,6-dehydratase 2 (EC 4.2.1.46)
