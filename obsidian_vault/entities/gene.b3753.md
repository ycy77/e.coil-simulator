---
entity_id: "gene.b3753"
entity_type: "gene"
name: "rbsR"
source_database: "NCBI RefSeq"
source_id: "gene-b3753"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3753"
  - "rbsR"
---

# rbsR

`gene.b3753`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3753`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsR (gene.b3753) is a gene entity. It encodes rbsR (protein.P0ACQ0). Encoded protein function: FUNCTION: Transcriptional repressor for the ribose rbsDACBK operon. RbsR binds to a region of perfect dyad symmetry spanning the rbs operon transcriptional start site. The affinity for the rbs operator is reduced by addition of ribose, consistent with ribose being the inducer of the operon. EcoCyc product frame: PD03867. Genomic coordinates: 3938227-3939219. EcoCyc protein note: The transcription factor RbsR, for "Ribose Repressor," is negatively autoregulated and controls the transcription of the operon involved in ribose catabolism and transport . Transcription of this operon is induced when E. coli is grown in the absence of glucose and when the physiological inducer D-ribose binds to the RbsR repressor . When D-ribose binds to RbsR, the protein becomes inactive because the binding affinity of RbsR decreases . RbsR represses not only the rbs operon for transport and utilization of D-ribose but also the de novo synthesis of purine nucleotides from D-ribose 5-phosphate. In the presence of the inducer D-ribose, RbsR activates the salvage pathway of purine nucleotide synthesis . Although little is known about the mechanism of regulation of the RbsR transcription factor, Mauzy et al...

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACQ0|protein.P0ACQ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsR; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012271,ECOCYC:EG10819,GeneID:948266`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3938227-3939219:+; feature_type=gene
