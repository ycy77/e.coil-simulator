---
entity_id: "gene.b0449"
entity_type: "gene"
name: "mdlB"
source_database: "NCBI RefSeq"
source_id: "gene-b0449"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0449"
  - "mdlB"
---

# mdlB

`gene.b0449`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0449`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdlB (gene.b0449) is a gene entity. It encodes mdlB (protein.P0AAG5). Encoded protein function: Multidrug resistance-like ATP-binding protein MdlB (EC 7.6.2.2) EcoCyc product frame: MDLB-MONOMER. EcoCyc synonyms: mdl. Genomic coordinates: 470636-472417. EcoCyc protein note: In the Transporter Classification Database MdlAB is annotated as a putative multidrug resistance-like ABC exporter . MdlA and MdlB each contain a TMD-ABC domain . MdlB contains 6 putative transmembrane regions and a sinlge nucleotide-binding domain; overexpression of mdlA (cloned from E. coli W3104) in the drug supersensitive strain KAM3 did not alter its resistance phenotype against a large number of different drug and toxic compounds . mdlB is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . mdl: multidrug resistance-like .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAG5|protein.P0AAG5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001557,ECOCYC:EG11622,GeneID:945088`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:470636-472417:+; feature_type=gene
