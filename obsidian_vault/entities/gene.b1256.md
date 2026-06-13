---
entity_id: "gene.b1256"
entity_type: "gene"
name: "ompW"
source_database: "NCBI RefSeq"
source_id: "gene-b1256"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1256"
  - "ompW"
---

# ompW

`gene.b1256`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1256`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompW (gene.b1256) is a gene entity. It encodes ompW (protein.P0A915). Encoded protein function: FUNCTION: Acts as a receptor for colicin S4. {ECO:0000269|PubMed:10348872}. EcoCyc product frame: EG11124-MONOMER. EcoCyc synonyms: yciD. Genomic coordinates: 1314020-1314658. EcoCyc protein note: In the Transporter Classification Database OmpW belongs to the Bacterial Porin, OmpW Family (see also . OmpW is the receptor for Colicin S4 . OmpW is enriched in minicell membranes; epitope-tagged OmpW (expressed from a low-copy number plasmid) localizes predominantly to the cell poles . OmpW forms an 8-stranded β-barrel structure with a narrow hydrophobic channel; OmpW functions as an ion channel when reconstituted in planar lipid bilayers OmpW participates in CPLX0-7963 EmrE-mediated substrate efflux . Proteomic analysis indicates that the expression of OmpW is upregulated in response to tetracycline and ampicillin . Expression is downregulated upon induction of the small noncoding RNA, RybB, which is a member of the σE regulon . OmpW is subject to both repression and activation by a series of global regulators - FNR, ArcA, CRP, H-NS and NarL - involved in anaerobic carbon and energy metabolism; OmpW may play a role under microaerobic conditions during the transition from aerobic to anaerobic growth . The folding behaviour of OmpW has been investigated in vitro...

## Biological Role

Repressed by fnr (protein.P0A9E5), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), narL (protein.P0AF28). Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A915|protein.P0A915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ompW; function=-+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ompW; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ompW; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ompW; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ompW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004210,ECOCYC:EG11124,GeneID:945128`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1314020-1314658:+; feature_type=gene
