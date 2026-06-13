---
entity_id: "gene.b0736"
entity_type: "gene"
name: "ybgC"
source_database: "NCBI RefSeq"
source_id: "gene-b0736"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0736"
  - "ybgC"
---

# ybgC

`gene.b0736`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0736`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgC (gene.b0736) is a gene entity. It encodes ybgC (protein.P0A8Z3). Encoded protein function: FUNCTION: Thioesterase that appears to be involved in phospholipid metabolism. Some specific acyl-ACPs could be physiological substrates. Displays acyl-CoA thioesterase activity on malonyl-CoA in vitro, catalyzing the hydrolysis of the thioester bond. {ECO:0000269|PubMed:16294310}. EcoCyc product frame: EG11110-MONOMER. Genomic coordinates: 774752-775156. EcoCyc protein note: Esterase/thioesterase activity of YbgC was discovered in a high-throughput screen of purified proteins . The Haemophilus influenzae ortholog YbgC was shown to be an acyl-coenzyme A thioesterase . The Synechocystis ortholog is a 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA) thioesterase which generates 1,4-dihydroxy-2-naphthoate, an intermediate in menaquinone biosynthesis . However, YbgC has no detectable activity with DHNA-CoA or aryl-CoA analogues . YbgC interacts with ACP and may be involved in phospholipid metabolism . ybgC is the first gene in an operon together with tolQRA ; however, a ybgC::Cm insertion strain does not have an obvious phenotype and does not appear to have a polar effect on tolQ .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Z3|protein.P0A8Z3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybgC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002508,ECOCYC:EG11110,GeneID:948907`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:774752-775156:+; feature_type=gene
