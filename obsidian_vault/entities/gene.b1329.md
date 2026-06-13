---
entity_id: "gene.b1329"
entity_type: "gene"
name: "mppA"
source_database: "NCBI RefSeq"
source_id: "gene-b1329"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1329"
  - "mppA"
---

# mppA

`gene.b1329`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1329`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mppA (gene.b1329) is a gene entity. It encodes mppA (protein.P77348). Encoded protein function: FUNCTION: Part of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Is involved in the recycling of cell wall peptides (PubMed:9495761). Binds the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338, PubMed:9495761). Can also transport ordinary alpha-linked tripeptides such as Pro-Phe-Lys, but with much lower efficiency than OppA (PubMed:9495761). Cannot bind typical tripeptides such as Lys-Glu-Lys, Lys-Lys-Lys or Ala-Ala-Ala (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:9495761}. EcoCyc product frame: G6665-MONOMER. EcoCyc synonyms: ynaH. Genomic coordinates: 1393227-1394840. EcoCyc protein note: MppA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of murein tripeptides . mppA mutants cannot use murein tripeptide (L-alanyl-γ-D-glutamyl-meso-diaminopimelate) as a source of diaminopimelic acid (Dap) in a strain that requires Dap for growth . MppA (in the absence of the periplasmic oligopeptide binding protein OppA) supports growth of a proline auxotroph on Pro-Phe-Lys tripeptide; MppA transports murein tripeptide more efficiently than Pro-Phe-Lys...

## Biological Role

Repressed by pgrR (protein.P77333).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77348|protein.P77348]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=mppA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004460,ECOCYC:G6665,GeneID:945951`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1393227-1394840:+; feature_type=gene
