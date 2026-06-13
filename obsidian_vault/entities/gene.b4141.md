---
entity_id: "gene.b4141"
entity_type: "gene"
name: "yjeH"
source_database: "NCBI RefSeq"
source_id: "gene-b4141"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4141"
  - "yjeH"
---

# yjeH

`gene.b4141`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4141`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjeH (gene.b4141) is a gene entity. It encodes yjeH (protein.P39277). Encoded protein function: FUNCTION: Catalyzes the efflux of L-methionine, L-leucine, L-isoleucine and L-valine (PubMed:26319875). Activity is dependent on electrochemical potential (PubMed:26319875). {ECO:0000269|PubMed:26319875}. EcoCyc product frame: B4141-MONOMER. Genomic coordinates: 4369156-4370412. EcoCyc protein note: yjeH encodes an L-methionine and branched chain amino acid (BCAA) efflux transporter in E. coli K-12. Over-expression of yjeH results in increased tolerance to L-methionine and BCAA structural analogues (DL-ethionine, DL-norleucine, DL-norvaline); over-expression of yjeH is associated with increased export of methionine and the BCAAs when cells are grown in the presence of Met-Met, Ile-Ile, Leu-Leu or Val-Val dipeptides. Additionally, cells lacking yjeH have increased levels of intracellular methionine or BCAAs when grown in the presence of the relevant dipeptides and increased sensitivity to the structural analogues . YjeH efflux activity is dependent on the proton motive force . Expression of yjeH is induced by increased cytoplasmic levels of L-methionine, L-leucine or L-isoleucine; expression of yjeH is not regulated by the transcriptional repressor, PD04032 "MetJ"...

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39277|protein.P39277]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjeH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013559,ECOCYC:G7833,GeneID:948656`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4369156-4370412:-; feature_type=gene
