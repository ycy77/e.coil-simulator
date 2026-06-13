---
entity_id: "gene.b1831"
entity_type: "gene"
name: "proQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1831"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1831"
  - "proQ"
---

# proQ

`gene.b1831`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1831`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proQ (gene.b1831) is a gene entity. It encodes proQ (protein.P45577). Encoded protein function: FUNCTION: RNA chaperone with significant RNA binding, RNA strand exchange and RNA duplexing activities. May regulate ProP activity through an RNA-based, post-transcriptional mechanism. {ECO:0000255|HAMAP-Rule:MF_00749, ECO:0000269|PubMed:21381725}. EcoCyc product frame: EG12866-MONOMER. EcoCyc synonyms: yoeC, yobE, yebJ. Genomic coordinates: 1914836-1915534. EcoCyc protein note: ProQ is an RNA-binding protein involved in global small RNA-dependent regulation. It binds double-stranded RNA and has both strand exchange and RNA duplexing activities. ProQ is a soluble protein that occurs at approximately 2,000 copies per cell . It belongs to the FinO family of proteins, whose members contain a conserved RNA-binding domain (named after the founding member of this family, the F-like plasmid (F') FinO protein) . The protein also contains a C-terminal Tudor domain , and the two domains are connected by a long, flexible, protease-sensitive linker region . All three domains contain potential RNA-binding surfaces. ProQ was initially characterized as a positive regulator of the osmosensing transporter PROP-MONOMER "ProP", which mediates the uptake of zwitterionic osmolytes such as proline and glycine betaine (hence its name) . proQ-deficient mutants have significantly reduced ProP activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45577|protein.P45577]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006092,ECOCYC:EG12866,GeneID:948950`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1914836-1915534:-; feature_type=gene
