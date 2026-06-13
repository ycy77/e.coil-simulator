---
entity_id: "gene.b2713"
entity_type: "gene"
name: "hydN"
source_database: "NCBI RefSeq"
source_id: "gene-b2713"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2713"
  - "hydN"
---

# hydN

`gene.b2713`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2713`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hydN (gene.b2713) is a gene entity. It encodes hydN (protein.P0AAK4). Encoded protein function: FUNCTION: Electron transport from formate to hydrogen. {ECO:0000269|PubMed:8661925}. EcoCyc product frame: EG11552-MONOMER. Genomic coordinates: 2837578-2838105. EcoCyc protein note: HydN is a ferredoxin-like protein containing cysteine-rich motifs that indicate the presence of iron-sulfur clusters . The EG12277-MONOMER YsaA protein is the most closely related paralog within the E. coli K-12 genome . Bacterial two-hybrid assays were used to build an interaction network for the ferredoxin-like family of proteins; HydN was shown to interact with itself as well as YsaA, AegA, HycB and HycF . It was suggested that HydN is an electron carrier accepting electrons from FDH-H, with fumarate as the terminal electron acceptor . However, a ΔhydN strain is still able to transfer electrons from formate to fumarate (Maier, T.H.P., dissertation, Ludwig-Maximilian-Universität München 1997, cited in ). A hydN in-frame deletion mutation causes only weak reduction in hydrogenase activity, but loss of more than 60% of FORMATEDEHYDROGH-MONOMER (FDH-H) activity . Complementation of the mutant with plasmid-encoded hydN does not restore wild-type FDH-H activity...

## Biological Role

Activated by fhlA (protein.P19323).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAK4|protein.P0AAK4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hydN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008919,ECOCYC:EG11552,GeneID:947190`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2837578-2838105:-; feature_type=gene
