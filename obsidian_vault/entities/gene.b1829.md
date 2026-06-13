---
entity_id: "gene.b1829"
entity_type: "gene"
name: "htpX"
source_database: "NCBI RefSeq"
source_id: "gene-b1829"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1829"
  - "htpX"
---

# htpX

`gene.b1829`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1829`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

htpX (gene.b1829) is a gene entity. It encodes htpX (protein.P23894). Encoded protein function: FUNCTION: Membrane-localized protease able to endoproteolytically degrade overproduced SecY but not YccA, another membrane protein. It seems to cleave SecY at specific cytoplasmic sites. Does not require ATP. Its natural substrate has not been identified. Probably plays a role in the quality control of integral membrane proteins. {ECO:0000269|PubMed:16076848}. EcoCyc product frame: EG10462-MONOMER. Genomic coordinates: 1911695-1912576. EcoCyc protein note: HtpX is a heat shock protein that may be involved in degrading misfolded proteins . Expression of HtpX is controlled by the CpxR-CpxA signal system, which senses abnormal proteins. The Cpx pathway has been shown to become activated by abnormal folding of proteins at the periplasmic surface of the cytoplasmic membrane . Overexpression of HtpX leads to enhanced degradation of partial-length puromycyl peptides . The putative zinc metalloproteinase active site of HtpX is located on the cytosolic side of the inner membrane. Mutations in this site abrogate HtpX function . HtpX is integrated into the inner membrane with two N-terminally located transmembrane segments . Review:

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), nac (protein.Q47005). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23894|protein.P23894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=htpX; function=+
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=htpX; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=htpX; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006087,ECOCYC:EG10462,GeneID:946076`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1911695-1912576:-; feature_type=gene
