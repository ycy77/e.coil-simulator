---
entity_id: "gene.b0649"
entity_type: "gene"
name: "djlC"
source_database: "NCBI RefSeq"
source_id: "gene-b0649"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0649"
  - "djlC"
---

# djlC

`gene.b0649`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0649`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

djlC (gene.b0649) is a gene entity. It encodes djlC (protein.P77359). Encoded protein function: FUNCTION: Regulatory HscC co-chaperone (PubMed:12054669, PubMed:12183460). Stimulates the ATPase activity of the chaperone protein HscC (Hsc62) but not the activity of the other Hsp70 homologs, DnaK and HscA (PubMed:12054669, PubMed:12183460). {ECO:0000269|PubMed:12054669, ECO:0000269|PubMed:12183460}. EcoCyc product frame: G6356-MONOMER. EcoCyc synonyms: hscD, ybeV, hsc56. Genomic coordinates: 680212-681663. EcoCyc protein note: DjlC, also known as Hsc56 (heat shock cognate protein with a molecular weight of 56,000), is a DnaJ-like protein that stimulates the ATPase activity of the chaperone G6357-MONOMER "HscC". Purified DjlC stimulates the ATPase activity of HscC (Hsc62) in vitro; DjlC exhibits specificity towards HscC - it does not activate the ATPase activity of EG10241-MONOMER "DnaK" or EG12130 "HscA" (Hsc66) . The nucleotide exchange factor CPLX0-8192 "GrpE" may or may not enhance the ATPase activity of the DjlC-HscC system. DjlC contains a J-domain sequence (characteristic of DnaJ homologues) and a C-terminal transmembrane domain . DjlC belongs to the heterogeneous group of C-tail-anchored membrane proteins (TAMPs)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77359|protein.P77359]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002222,ECOCYC:G6356,GeneID:945253`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:680212-681663:+; feature_type=gene
