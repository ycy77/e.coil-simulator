---
entity_id: "protein.P37759"
entity_type: "protein"
name: "rfbB"
source_database: "UniProt"
source_id: "P37759"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rfbB rmlB b2041 JW2026"
---

# rfbB

`protein.P37759`

## Static

- Type: `protein`
- Source: `UniProt:P37759`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000250|UniProtKB:P27830}. dTDP-glucose 4,6-dehydratase (RfbB) is involved in the dTDP-rhamnose biosynthesis pathway, which is important for the synthesis of O-specific LPS. This enzyme catalyzes the conversion of dTDP-α-D-glucose into dTDP-4-keto-6-deoxyglucose. This reaction occurs in three steps: dehydrogenation, dehydration, and rereduction. The coenzyme NAD+ mediates the dehydrogenation and rereduction steps of the reaction . The reduction of enzyme-bound NAD+ to NADH results in a conformational change in the protein such that the substrate cannot be released at a significant rate from this form of the enzyme, thus the intermediates in the normal catalytic process remain tightly bound to the enzyme . The genes encoding the enzymes involved in the biosynthesis of O-specific polysaccharides are clustered in the rfb region. E. coli K-12 does not normally express O-specific LPS due to mutations in the rfb region. However, genes in the rfb cluster have been identified. dTDP-glucose 4,6-dehydratase is encoded by the rfbB gene which is paralogous to rffG...

## Biological Role

Component of dTDP-glucose 4,6-dehydratase 1 (complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000250|UniProtKB:P27830}.

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX|complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2041|gene.b2041]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37759`
- `KEGG:ecj:JW2026;eco:b2041;ecoc:C3026_11495;`
- `GeneID:945276;`
- `GO:GO:0000271; GO:0005829; GO:0008460; GO:0009103; GO:0009226; GO:0009243; GO:0019305; GO:0042802; GO:0051287`
- `EC:4.2.1.46`

## Notes

dTDP-glucose 4,6-dehydratase 1 (EC 4.2.1.46)
