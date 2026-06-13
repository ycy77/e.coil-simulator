---
entity_id: "protein.P63224"
entity_type: "protein"
name: "gmhA"
source_database: "UniProt"
source_id: "P63224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gmhA lpcA tfrA yafI b0222 JW0212"
---

# gmhA

`protein.P63224`

## Static

- Type: `protein`
- Source: `UniProt:P63224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the isomerization of sedoheptulose 7-phosphate in D-glycero-D-manno-heptose 7-phosphate. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:18056714}. Sedoheptulose 7-phosphate isomerase catalyzes the first committed step in the biosynthesis of a core component of lipopolysaccharide, the isomerization of D-sedoheptulose 7-phosphate to D-glycero-D-manno-heptose 7-phosphate. Crystal structures of GmhA alone and in complex with the substrate D-sedoheptulose 7-phosphate have been solved. The protein appears to be a tetramer in both the crystal structures and in solution. A reaction mechanism utilizing an enediol intermediate has been proposed . Potential active site residues were mutagenized and their enzymatic activity was measured both in vivo and in vitro . Mutations in gmhA confer novobiocin hypersensitivity and F plasmid conjugation deficiency ; gmhA mutants were shown to contain lipopolysaccharides lacking heptose . An IS1 insertion in the Shine-Dalgarno sequence of gmhA was isolated as a suppressor of a ΔlapB mutant . The LPS biosynthesis pathway including GmhA have been explored as a target for development of new antibacterial compounds. Under selection for reduced susceptibility to tigecycline, mutations in gmhA appear . These mutants show increased sensitivity to bile salts...

## Biological Role

Catalyzes D-glycero-D-manno-heptose 7-phosphate aldose-ketose-isomerase (reaction.R09768), D-glycero-alpha-D-manno-heptose 7-phosphate aldose-ketose-isomerase (reaction.R09769). Component of D-sedoheptulose 7-phosphate isomerase (complex.ecocyc.CPLX0-7660).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of sedoheptulose 7-phosphate in D-glycero-D-manno-heptose 7-phosphate. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:18056714}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R09768|reaction.R09768]] `KEGG` `database` - via EC:5.3.1.28
- `catalyzes` --> [[reaction.R09769|reaction.R09769]] `KEGG` `database` - via EC:5.3.1.28
- `is_component_of` --> [[complex.ecocyc.CPLX0-7660|complex.ecocyc.CPLX0-7660]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0222|gene.b0222]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63224`
- `KEGG:ecj:JW0212;eco:b0222;ecoc:C3026_01050;`
- `GeneID:89519637;93777173;949134;`
- `GO:GO:0005737; GO:0005829; GO:0008270; GO:0008968; GO:0009244; GO:0032991; GO:0042802; GO:0051289; GO:0097367; GO:2001061`
- `EC:5.3.1.28`

## Notes

Phosphoheptose isomerase (EC 5.3.1.28) (Sedoheptulose 7-phosphate isomerase)
