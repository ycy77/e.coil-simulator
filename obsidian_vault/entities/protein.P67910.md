---
entity_id: "protein.P67910"
entity_type: "protein"
name: "hldD"
source_database: "UniProt"
source_id: "P67910"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hldD htrM rfaD waaD b3619 JW3594"
---

# hldD

`protein.P67910`

## Static

- Type: `protein`
- Source: `UniProt:P67910`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion between ADP-D-glycero-beta-D-manno-heptose and ADP-L-glycero-beta-D-manno-heptose via an epimerization at carbon 6 of the heptose. {ECO:0000269|PubMed:6337148, ECO:0000269|PubMed:7929099}. The rfaD gene encodes ADP-L-glycero-D-mannoheptose-6-epimerase, the last enzyme in the pathway for synthesis of the ADP-heptose precursor of core LPS . The enzyme is glycosylated . It was initially thought to contain NAD+ as a cofactor , but the cofactor found in the crystal structure was NADP+ . Subsequent studies showed that the enzyme has a preference of NADP+ over NAD+ . A crystal structure of RfaD has been solved at 2 Å resolution . The enzyme was initially thought to form a homohexamer , but appears as a homopentamer in the crystal structure . A reaction mechanism involving transient oxidation of the C-6'' stereocenter of the substrate and transient reduction of the NADP+ cofactor has been proposed . Catalysis involves two basic residues, Tyr140 and Lys178 . Only very small amounts of the transiently oxidized 6''-keto intermediate are released from the enzyme during catalysis . An rfaD null mutant strain is unable to grow above 42°C and has a mucoid phenotype...

## Biological Role

Component of ADP-L-glycero-D-mannoheptose 6-epimerase (complex.ecocyc.CPLX0-3681).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion between ADP-D-glycero-beta-D-manno-heptose and ADP-L-glycero-beta-D-manno-heptose via an epimerization at carbon 6 of the heptose. {ECO:0000269|PubMed:6337148, ECO:0000269|PubMed:7929099}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3681|complex.ecocyc.CPLX0-3681]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b3619|gene.b3619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67910`
- `KEGG:ecj:JW3594;eco:b3619;ecoc:C3026_19620;`
- `GeneID:86861737;86944394;948134;`
- `GO:GO:0005829; GO:0008712; GO:0009244; GO:0016020; GO:0070401; GO:0097171`
- `EC:5.1.3.20`

## Notes

ADP-L-glycero-D-manno-heptose-6-epimerase (EC 5.1.3.20) (ADP-L-glycero-beta-D-manno-heptose-6-epimerase) (ADP-glyceromanno-heptose 6-epimerase) (ADP-hep 6-epimerase) (AGME)
