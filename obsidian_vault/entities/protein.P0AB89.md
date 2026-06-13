---
entity_id: "protein.P0AB89"
entity_type: "protein"
name: "purB"
source_database: "UniProt"
source_id: "P0AB89"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purB b1131 JW1117"
---

# purB

`protein.P0AB89`

## Static

- Type: `protein`
- Source: `UniProt:P0AB89`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes two reactions in de novo purine nucleotide biosynthesis. Catalyzes the breakdown of 5-aminoimidazole- (N-succinylocarboxamide) ribotide (SAICAR or 2-[5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamido]succinate) to 5-aminoimidazole-4-carboxamide ribotide (AICAR or 5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) and fumarate, and of adenylosuccinate (ADS or N(6)-(1,2-dicarboxyethyl)-AMP) to adenosine monophosphate (AMP) and fumarate. {ECO:0000269|PubMed:17531264}.; FUNCTION: (Microbial infection) Catalyzes the conversion of 2-amino-2'-deoxyadenylo-succinate to dZMP and fumarate, when the bacterium is infected by a phage that produces the substrate of this reaction, a step in the synthesis of dZTP (2-amino-2'-deoxyadenosine 5'-triphosphate), which is a nucleotide then used by the phage as a DNA polymerase substrate. {ECO:0000269|PubMed:33926954}.

## Biological Role

Component of adenylosuccinate lyase (complex.ecocyc.CPLX0-7959).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes two reactions in de novo purine nucleotide biosynthesis. Catalyzes the breakdown of 5-aminoimidazole- (N-succinylocarboxamide) ribotide (SAICAR or 2-[5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamido]succinate) to 5-aminoimidazole-4-carboxamide ribotide (AICAR or 5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) and fumarate, and of adenylosuccinate (ADS or N(6)-(1,2-dicarboxyethyl)-AMP) to adenosine monophosphate (AMP) and fumarate. {ECO:0000269|PubMed:17531264}.; FUNCTION: (Microbial infection) Catalyzes the conversion of 2-amino-2'-deoxyadenylo-succinate to dZMP and fumarate, when the bacterium is infected by a phage that produces the substrate of this reaction, a step in the synthesis of dZTP (2-amino-2'-deoxyadenosine 5'-triphosphate), which is a nucleotide then used by the phage as a DNA polymerase substrate. {ECO:0000269|PubMed:33926954}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7959|complex.ecocyc.CPLX0-7959]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1131|gene.b1131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB89`
- `KEGG:ecj:JW1117;eco:b1131;ecoc:C3026_06805;`
- `GeneID:945695;`
- `GO:GO:0004018; GO:0005829; GO:0006163; GO:0006189; GO:0006974; GO:0044208; GO:0070626; GO:0097216`
- `EC:4.3.2.2`

## Notes

Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) (ASase)
