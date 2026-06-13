---
entity_id: "gene.b3181"
entity_type: "gene"
name: "greA"
source_database: "NCBI RefSeq"
source_id: "gene-b3181"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3181"
  - "greA"
---

# greA

`gene.b3181`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3181`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

greA (gene.b3181) is a gene entity. It encodes greA (protein.P0A6W5). Encoded protein function: FUNCTION: Necessary for efficient RNA polymerase transcription elongation past template-encoded arresting sites. The arresting sites in DNA have the property of trapping a certain fraction of elongating RNA polymerases that pass through, resulting in locked ternary complexes. Cleavage of the nascent transcript by cleavage factors such as GreA or GreB allows the resumption of elongation from the new 3'terminus. GreA releases sequences of 2 to 3 nucleotides. EcoCyc product frame: EG10415-MONOMER. Genomic coordinates: 3328239-3328715. EcoCyc protein note: GreA stimulates the mRNA cleavage activity of RNA polymerase , which acts to release a polymerase complex that has stalled or has incorporated an incorrect nucleotide . GreA (and GreB) is also required for wild-type transcription of some regulatory regions within lambda phage . GreA stimulates shortening of the 3' end of the transcript by a dinucleotide, and the new 3' end is subject to elongation by RNA polymerase . GreA decreases abortive initiation and increases productive initiation . GreA activity requires that GreA associate with RNA polymerase before the complex stalls , or even before RNA transcription begins . The transcription complex moves backward in conjunction with GreA activity...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6W5|protein.P0A6W5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=greA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010454,ECOCYC:EG10415,GeneID:947696`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3328239-3328715:-; feature_type=gene
