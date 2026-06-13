---
entity_id: "protein.P37745"
entity_type: "protein"
name: "rfbC"
source_database: "UniProt"
source_id: "P37745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rfbC rmlC b2038 JW2023"
---

# rfbC

`protein.P37745`

## Static

- Type: `protein`
- Source: `UniProt:P37745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the epimerization of the C3' and C5'positions of dTDP-6-deoxy-D-xylo-4-hexulose, forming dTDP-6-deoxy-L-lyxo-4-hexulose. {ECO:0000250|UniProtKB:P26394}. dTDP-4-dehydrorhamnose 3,5-epimerase is involved in the dTDP-rhamnose biosynthesis pathway, which is important for the synthesis of O-specific LPS. dTDP-4-dehydrorhamnose 3,5-epimerase forms a complex with dTDP-4-dehydrorhamnose reductase, which is known as dTDP-L-rhamnose synthetase. The epimerase catalyzes inversion at C-3 and C-5 via corresponding enediols, but these molecules cannot be released from the enzyme. The reductase then catalyzes the stereospecific reduction of the 4-keto group of dTDP-4-dehydro-6-deoxy-L-mannose. dTDP-4-dehydrorhamnose 3,5-epimerase is coded for by the rfbC gene. rfbC was identified in a screen for genes that reduce the lethal effects of stress. An rfbC insertion mutant is more sensitive than wild type to mitomycin C and other stresses . The genes encoding the enzymes involved in the biosynthesis of O-specific polysaccharides are clustered in the rfb region. E. coli K-12 is phenotypically rough and does not express O-specific LPS due to mutations in the rfb region; E. coli K-12 MG1655 contains the rfb-50 mutation - an IS5 element which disrupts wbbL encoding rhamnose transferase; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes O16 antigen...

## Biological Role

Catalyzes DTDPDEHYDRHAMEPIM-RXN (reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the epimerization of the C3' and C5'positions of dTDP-6-deoxy-D-xylo-4-hexulose, forming dTDP-6-deoxy-L-lyxo-4-hexulose. {ECO:0000250|UniProtKB:P26394}.

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN|reaction.ecocyc.DTDPDEHYDRHAMEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2038|gene.b2038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37745`
- `KEGG:ecj:JW2023;eco:b2038;ecoc:C3026_11480;`
- `GeneID:947482;`
- `GO:GO:0000271; GO:0005829; GO:0006974; GO:0008830; GO:0009103; GO:0009243; GO:0009411; GO:0019305; GO:0046677`
- `EC:5.1.3.13`

## Notes

dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (dTDP-4-keto-6-deoxyglucose 3,5-epimerase) (dTDP-6-deoxy-D-xylo-4-hexulose 3,5-epimerase) (dTDP-L-rhamnose synthase)
