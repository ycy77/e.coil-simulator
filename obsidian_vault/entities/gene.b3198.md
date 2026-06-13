---
entity_id: "gene.b3198"
entity_type: "gene"
name: "kdsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3198"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3198"
  - "kdsC"
---

# kdsC

`gene.b3198`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3198`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdsC (gene.b3198) is a gene entity. It encodes kdsC (protein.P0ABZ4). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 3-deoxy-D-manno-octulosonate 8-phosphate (KDO 8-P) to 3-deoxy-D-manno-octulosonate (KDO) and inorganic phosphate. {ECO:0000250|UniProtKB:A0A140N5J7}. EcoCyc product frame: G7663-MONOMER. EcoCyc synonyms: yrbJ, yrbI. Genomic coordinates: 3342273-3342839. EcoCyc protein note: 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase (KdsC) is specific for the hydrolysis of 3-deoxy-D-manno-octulosonate 8-phosphate. The product of this reaction, Kdo, is a unique eight-carbon keto sugar that is an integral part of lipopolysaccharide, providing the link between lipid A and the outer core and O-antigen polysaccharide chain. KdsC is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . Biochemical characterization of KdsC was done with the E. coli B enzyme , whose protein sequence is 99% identical to that of K-12 MG1655. The reaction kinetics and optimal conditions have been determined; the enzyme exhibits tight substrate specificity and shows a requirement for divalent cations . Crystal structures of the enzyme from a pathogenic E. coli strain have been solved. The active site is located at the interface between adjacent monomers of the homotetrameric enzyme...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABZ4|protein.P0ABZ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdsC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010506,ECOCYC:G7663,GeneID:947717`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3342273-3342839:+; feature_type=gene
