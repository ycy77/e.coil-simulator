---
entity_id: "gene.b3415"
entity_type: "gene"
name: "gntT"
source_database: "NCBI RefSeq"
source_id: "gene-b3415"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3415"
  - "gntT"
---

# gntT

`gene.b3415`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3415`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gntT (gene.b3415) is a gene entity. It encodes gntT (protein.P39835). Encoded protein function: FUNCTION: Part of the gluconate utilization system Gnt-I; high-affinity intake of gluconate. EcoCyc product frame: GNTT-MONOMER. EcoCyc synonyms: gntTalpha, yhgC, gntM, usgA. Genomic coordinates: 3546559-3547875. EcoCyc protein note: GntT is one of four known transporters for gluconate in E. coli, the others being the homologous GntU, GntP and IdnT transporters. Whole cell experiments have shown that the cloned gntT gene was able to complement a gluconate transport negative mutant and confers high affinity gluconate transport with a Km of approx 6 μM . Transcriptional analysis has shown that gntT constitutes a monocistronic operon. Analysis of gntT-lacZ fusions has indicated that gntT expression is induced at low levels of gluconate, partially repressed by glucose, and increased in early logarithmic phase . Expression of both gntT and gntU is controlled by the GntR repressor and by cyclic AMP-CRP . GntT is a member of the Gnt family of gluconate transporters . Gluconate uptake has been reported to occur via a proton-symport mechanism in E. coli . It seems likely that GntT is a high affinity gluconate uptake system that functions via D-gluconate/proton symport...

## Biological Role

Repressed by gntR (protein.P0ACP5). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39835|protein.P39835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gntT; function=+
- `represses` <-- [[protein.P0ACP5|protein.P0ACP5]] `RegulonDB` `S` - regulator=GntR; target=gntT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011148,ECOCYC:EG12380,GeneID:947924`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3546559-3547875:+; feature_type=gene
