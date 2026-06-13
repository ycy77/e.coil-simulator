---
entity_id: "gene.b0621"
entity_type: "gene"
name: "dcuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0621"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0621"
  - "dcuC"
---

# dcuC

`gene.b0621`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0621`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcuC (gene.b0621) is a gene entity. It encodes dcuC (protein.P0ABP3). Encoded protein function: FUNCTION: Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:10368146, PubMed:8955408). Catalyzes the uptake of fumarate coupled to the export of succinate (PubMed:8955408). Can also catalyze the uptake of fumarate and the efflux of succinate, without exchange (PubMed:10368146, PubMed:8955408). Shows low rates of transport, which are sufficient for succinate export during fermentation but not for fumarate-succinate exchange in fumarate respiration, indicating that it may function in vivo as the succinate efflux carrier for glucose fermentation, even if it is also able to operate as a fumarate-succinate antiporter (PubMed:10368146). {ECO:0000269|PubMed:10368146, ECO:0000269|PubMed:8955408}. EcoCyc product frame: DCUC-MONOMER. Genomic coordinates: 654583-655968. EcoCyc protein note: DcuC is a C4-dicarboxylate transporter which may function primarily as a succinate efflux transporter during glucose fermentation. When grown under anaerobic conditions E. coli K-12 displays transport activities for uptake, efflux and exchange of C4-dicarboxylates...

## Biological Role

Repressed by yeiE (protein.P0ACR4). Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABP3|protein.P0ABP3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=dcuC; function=+
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002133,ECOCYC:G6347,GeneID:945000`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:654583-655968:-; feature_type=gene
