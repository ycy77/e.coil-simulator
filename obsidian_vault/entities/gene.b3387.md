---
entity_id: "gene.b3387"
entity_type: "gene"
name: "dam"
source_database: "NCBI RefSeq"
source_id: "gene-b3387"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3387"
  - "dam"
---

# dam

`gene.b3387`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3387`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dam (gene.b3387) is a gene entity. It encodes dam (protein.P0AEE8). Encoded protein function: FUNCTION: An alpha subtype methylase that recognizes the double-stranded sequence 5'-GATC-3' and methylates A-2 on both strands (Probable) (PubMed:12654995). Although it shares sequence specificity with a number of type II restriction endonucleases and methylases, it is thought to act in methyl-directed mismatch repair, initiation of chromosome replication and gene expression. Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440, ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:6300769}. EcoCyc product frame: EG10204-MONOMER. Genomic coordinates: 3515077-3515913. EcoCyc protein note: DNA adenine methyltransferase (Dam) is responsible for methylation of nearly all GATC sequences in the E. coli genome . Dam activity is involved in methyl-directed mismatch repair, initiation of chromosome replication, and gene expression. The intracellular level of Dam is limiting ; Dam occurs at about 130 molecules per rapidly growing cell . Dam transfers a methyl group from S-adenosyl-L-methionine (AdoMet) to create a N6-methyladenine at the GATC site...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEE8|protein.P0AEE8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dam; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011063,ECOCYC:EG10204,GeneID:947893`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3515077-3515913:-; feature_type=gene
