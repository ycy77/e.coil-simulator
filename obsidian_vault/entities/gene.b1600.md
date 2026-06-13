---
entity_id: "gene.b1600"
entity_type: "gene"
name: "mdtJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1600"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1600"
  - "mdtJ"
---

# mdtJ

`gene.b1600`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1600`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtJ (gene.b1600) is a gene entity. It encodes mdtJ (protein.P69212). Encoded protein function: FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}. EcoCyc product frame: B1600-MONOMER. EcoCyc synonyms: ydgF. Genomic coordinates: 1673136-1673501. EcoCyc protein note: MdtJ is one of two integral membrane subunits which constitute a heterodimeric multidrug / spermidine efflux transporter. MdtJ (Em121) shares 32% sequence identity with the multidrug efflux pump, EmrE; purified MdtJ doesn't bind TPP+ and cannot form mixed oligomers with EmrE in vitro . Expression of chromosomal mdtJI is very low in both the presence and absence of spermidine . Transcription of mdtUJI is induced by spermidine at pH 9; translation of MdtU is required for spermidine-mediated expression of MdtJ . mdtJ is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69212|protein.P69212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdtJ; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=mdtJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005345,ECOCYC:G6858,GeneID:946139`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1673136-1673501:-; feature_type=gene
