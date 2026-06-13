---
entity_id: "gene.b0025"
entity_type: "gene"
name: "ribF"
source_database: "NCBI RefSeq"
source_id: "gene-b0025"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0025"
  - "ribF"
---

# ribF

`gene.b0025`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0025`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribF (gene.b0025) is a gene entity. It encodes ribF (protein.P0AG40). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of riboflavin to FMN followed by the adenylation of FMN to FAD. {ECO:0000250|UniProtKB:Q59263}. EcoCyc product frame: RIBF-MONOMER. EcoCyc synonyms: yaaC. Genomic coordinates: 21407-22348. EcoCyc protein note: It is thought that ribF encodes a bifunctional protein with riboflavin kinase and FMN adenylyltransferase activities. These enzymes transform riboflavin into the coenzyme forms of FMN and FAD, respectively . A published patent contains experimental evidence that partial deletions or point mutations in the N-terminal domain of RibF ("protein X") selectively affect the FMN adenylyltransferase activity of the enzyme . ribF can complement the lethal defect of a ribC mutant (lacking riboflavin kinase and FMN adenylyltransferase activities) in Bacillus subtilis . The G23 residue appears to be essential for the FMN adenylyltrasferase, but not the riboflavin kinase activity . ribF is likely essential for growth in E. coli .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG40|protein.P0AG40]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=ribF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000091,ECOCYC:EG11079,GeneID:949129`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:21407-22348:+; feature_type=gene
