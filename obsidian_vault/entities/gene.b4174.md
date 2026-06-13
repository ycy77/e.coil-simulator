---
entity_id: "gene.b4174"
entity_type: "gene"
name: "hflK"
source_database: "NCBI RefSeq"
source_id: "gene-b4174"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4174"
  - "hflK"
---

# hflK

`gene.b4174`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4174`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hflK (gene.b4174) is a gene entity. It encodes hflK (protein.P0ABC7). Encoded protein function: FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}. EcoCyc product frame: EG10436-MONOMER. EcoCyc synonyms: hslY, hflA. Genomic coordinates: 4402038-4403297. EcoCyc protein note: HflK is an inner membrane protein which forms part of the HflCK complex that interacts with and regulates, the ATP-dependent protease FtsH . HflK expressed as a single subunit is unstable in vivo . HflK has been purified as a single subunit after overexpression of both hflK and hflC in an E. coli strain lacking the chromosomal hflCK genes. The purified subunit can inhibit FtsH mediated proteolysis of the bacteriophage lambda cII protein in vitro . Fluorescence microscopy of live cells indicated that expression of hflK is growth stage dependent - it is very low in exponential growing cells and significantly higher in stationary phase cells. In addition, the study found that HflK, tagged by fusion to mCherry (a red fluorescent protein) localizes in discrete foci on cell poles or on the septum region of the cells .

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABC7|protein.P0ABC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hflK; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hflK; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hflK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013663,ECOCYC:EG10436,GeneID:948698`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4402038-4403297:+; feature_type=gene
