---
entity_id: "gene.b4200"
entity_type: "gene"
name: "rpsF"
source_database: "NCBI RefSeq"
source_id: "gene-b4200"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4200"
  - "rpsF"
---

# rpsF

`gene.b4200`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4200`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsF (gene.b4200) is a gene entity. It encodes rpsF (protein.P02358). Encoded protein function: FUNCTION: Binds together with bS18 to 16S ribosomal RNA. EcoCyc product frame: EG10905-MONOMER. EcoCyc synonyms: sdgH. Genomic coordinates: 4425118-4425513. EcoCyc protein note: The S6 protein is a component of the 30S subunit of the ribosome. S6 interacts with the central domain of 16S rRNA . Protein-Protein Interaction (PPI) networks have been examined with algebraic topology analysis showing that most interacting proteins with S6 protein are related to the protein translation . The S6 protein contains glutamate residues at the C-terminus, only two of which are encoded by the rpsF gene ; up to four additional glutamate residues are added post-translationally by the EG10852-MONOMER RimK enzyme . This form of S6 accumulates when the soxR regulon is activated . In bacteriophage T7-infected cells, S6 is phosphorylated . Expression analysis of rpsFp indicates that it may be autoregulated by one or more of its operon components . Coexpressed S6:S18 were found to bind to the rpsF 5'-UTR in a region with structural similarity to their binding site in 16S rRNA . The S6:S18 complex was shown to repress translation of rpsF . A class of mutations in rpsF supresses the temperature-sensitive growth defect of certain dnaG alleles...

## Biological Role

Activated by crp (protein.P0ACJ8), glaR (protein.P37338).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02358|protein.P02358]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpsF; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rpsF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013740,ECOCYC:EG10905,GeneID:948723`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4425118-4425513:+; feature_type=gene
