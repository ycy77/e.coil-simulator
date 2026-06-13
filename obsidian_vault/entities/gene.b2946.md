---
entity_id: "gene.b2946"
entity_type: "gene"
name: "rsmE"
source_database: "NCBI RefSeq"
source_id: "gene-b2946"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2946"
  - "rsmE"
---

# rsmE

`gene.b2946`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2946`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmE (gene.b2946) is a gene entity. It encodes rsmE (protein.P0AGL7). Encoded protein function: FUNCTION: Specifically methylates the N3 position of the uracil ring of uridine 1498 (m3U1498) in 16S rRNA. Acts on the fully assembled 30S ribosomal subunit. {ECO:0000269|PubMed:16431987, ECO:0000269|PubMed:17872509}. EcoCyc product frame: EG12366-MONOMER. EcoCyc synonyms: yggJ. Genomic coordinates: 3091134-3091865. EcoCyc protein note: RsmE is the methyltransferase responsible for methylation of 16S rRNA at the N3 position of the U1498 nucleotide . In vitro, RsmE can methylate 16S rRNA within the assembled 30S ribosomal subunit, but not 70S ribosomes or naked 16S rRNA . RsmE belongs to the DUF family of predicted α/β trefoil knot methyltransferases . Crystal and solution structures of RsmE showed an N-terminal RNA recognition and binding domain and a C-terminal conserved methyltransferase domain containing a deep trefoil knot. Site-directed mutagenesis of residues based on the RsmE structure confirmed the key residues required for methyltransferase activity. A catalytic mechanism has been proposed . A strain carrying a deletion of rsmE appears to have no growth defect when grown alone, but can not compete with isogenic wild-type cells when grown in mixed culture .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGL7|protein.P0AGL7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009665,ECOCYC:EG12366,GeneID:945816`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3091134-3091865:+; feature_type=gene
