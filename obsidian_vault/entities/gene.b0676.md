---
entity_id: "gene.b0676"
entity_type: "gene"
name: "nagC"
source_database: "NCBI RefSeq"
source_id: "gene-b0676"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0676"
  - "nagC"
---

# nagC

`gene.b0676`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0676`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagC (gene.b0676) is a gene entity. It encodes nagC (protein.P0AF20). Encoded protein function: FUNCTION: Acts as a repressor of the nagEBACD operon and acts both as an activator and a repressor for the transcription of the glmSU operon (PubMed:7545108). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:7545108}. EcoCyc product frame: PD00266. EcoCyc synonyms: nagR. Genomic coordinates: 700374-701594. EcoCyc protein note: The NagC, "N-acetylglucosamine," transcriptional dual regulator participates in regulating the phosphotransferase system (PTS) . Its function is to coordinate the biosynthesis of the amino sugars, D-glucosamine (GlcN) and N-acetylglucosamine (GlcNAc) with their catabolism . The specific inducer for NagC is GlcNAc-6-P, the product of GlcNAc transport by the PTS . NagC is displaced from its DNA targets by interacting with GlcNAc-6-P . Mutation in the first two amino acids of the recognition helix of the DNA-binding motif causes GlcNAc6P to act with NagC as a corepressor instead of as an inducer . Proline at the first position of this helix seems to contribute to the distinction between the NagC binding sites and suboptimal sites...

## Biological Role

Repressed by crp (protein.P0ACJ8), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF20|protein.P0AF20]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nagC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagC; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagC; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nagC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002299,ECOCYC:EG10636,GeneID:945285`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:700374-701594:-; feature_type=gene
