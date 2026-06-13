---
entity_id: "gene.b4175"
entity_type: "gene"
name: "hflC"
source_database: "NCBI RefSeq"
source_id: "gene-b4175"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4175"
  - "hflC"
---

# hflC

`gene.b4175`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4175`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hflC (gene.b4175) is a gene entity. It encodes hflC (protein.P0ABC3). Encoded protein function: FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}. EcoCyc product frame: EG10435-MONOMER. EcoCyc synonyms: hflA. Genomic coordinates: 4403300-4404304. EcoCyc protein note: HflC is an inner membrane protein which forms part of the HflCK complex that interacts with and regulates, the ATP-dependent protease FtsH . HflC expressed as a single subunit is unstable in vivo . HflC has been purified as a single subunit after overexpression of both hflK and hflC in an E. coli strain lacking the chromosomal hflCK genes. The purified subunit can inhibit FtsH mediated proteolysis of the bacteriophage lambda cII protein in vitro . A study aiming to isolate detergent-resistant membranes (DRMs) has found that HflC, tagged by fusion with mCherry (a red monomeric fluorescent protein), was found to be localized on discrete foci on the poles of the normal cells .

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABC3|protein.P0ABC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hflC; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hflC; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hflC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013665,ECOCYC:EG10435,GeneID:948697`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4403300-4404304:+; feature_type=gene
