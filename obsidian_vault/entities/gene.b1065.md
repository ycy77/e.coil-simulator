---
entity_id: "gene.b1065"
entity_type: "gene"
name: "mdtH"
source_database: "NCBI RefSeq"
source_id: "gene-b1065"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1065"
  - "mdtH"
---

# mdtH

`gene.b1065`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1065`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtH (gene.b1065) is a gene entity. It encodes mdtH (protein.P69367). Encoded protein function: FUNCTION: Confers resistance to norfloxacin and enoxacin. {ECO:0000269|PubMed:11566977}. EcoCyc product frame: B1065-MONOMER. EcoCyc synonyms: yceL. Genomic coordinates: 1124118-1125326. EcoCyc protein note: In the Transporter Classification Database MdtH is a member of the Drug:H+ Antiporter 1 (DHA1) family within the Major Facilitator Superfamily (MFS) . Overexpression of cloned mdtD in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a two-fold increase in resistance to norfloxacin and enoxacin (compared to the mutant parent) but does not impact the resistance to a range of other toxic compounds (dyes, detergents, antibiotics and others) . mdtH is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . MdtH exports the industrially important anthocyanin compound, cyanidin 3-O-glucoside (C3G); overexpression of mdtH in a strain engineered for the production of the C3G significantly improves extracellular production . mdt: multidrug transport

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69367|protein.P69367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003618,ECOCYC:G6559,GeneID:946920`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1124118-1125326:-; feature_type=gene
