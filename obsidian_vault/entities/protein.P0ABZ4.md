---
entity_id: "protein.P0ABZ4"
entity_type: "protein"
name: "kdsC"
source_database: "UniProt"
source_id: "P0ABZ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdsC yrbI yrbJ b3198 JW3165"
---

# kdsC

`protein.P0ABZ4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABZ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 3-deoxy-D-manno-octulosonate 8-phosphate (KDO 8-P) to 3-deoxy-D-manno-octulosonate (KDO) and inorganic phosphate. {ECO:0000250|UniProtKB:A0A140N5J7}. 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase (KdsC) is specific for the hydrolysis of 3-deoxy-D-manno-octulosonate 8-phosphate. The product of this reaction, Kdo, is a unique eight-carbon keto sugar that is an integral part of lipopolysaccharide, providing the link between lipid A and the outer core and O-antigen polysaccharide chain. KdsC is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . Biochemical characterization of KdsC was done with the E. coli B enzyme , whose protein sequence is 99% identical to that of K-12 MG1655. The reaction kinetics and optimal conditions have been determined; the enzyme exhibits tight substrate specificity and shows a requirement for divalent cations . Crystal structures of the enzyme from a pathogenic E. coli strain have been solved. The active site is located at the interface between adjacent monomers of the homotetrameric enzyme . kdsC is not essential for growth, suggesting that another protein can compensate for the loss of KdsC . The transcription of the kdsC gene appears to be positively regulated by the protein BglG . Review:

## Biological Role

Component of 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC (complex.ecocyc.KDO-8PPHOSPHAT-CPLX).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 3-deoxy-D-manno-octulosonate 8-phosphate (KDO 8-P) to 3-deoxy-D-manno-octulosonate (KDO) and inorganic phosphate. {ECO:0000250|UniProtKB:A0A140N5J7}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.KDO-8PPHOSPHAT-CPLX|complex.ecocyc.KDO-8PPHOSPHAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3198|gene.b3198]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABZ4`
- `KEGG:ecj:JW3165;eco:b3198;ecoc:C3026_17405;`
- `GeneID:93778783;947717;`
- `GO:GO:0005829; GO:0009103; GO:0019143; GO:0046872`
- `EC:3.1.3.45`

## Notes

3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC (EC 3.1.3.45) (KDO 8-P phosphatase)
