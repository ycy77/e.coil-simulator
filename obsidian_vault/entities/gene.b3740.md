---
entity_id: "gene.b3740"
entity_type: "gene"
name: "rsmG"
source_database: "NCBI RefSeq"
source_id: "gene-b3740"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3740"
  - "rsmG"
---

# rsmG

`gene.b3740`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3740`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmG (gene.b3740) is a gene entity. It encodes rsmG (protein.P0A6U5). Encoded protein function: FUNCTION: Specifically methylates the N7 position of guanine in position 527 of 16S rRNA. Requires the intact 30S subunit for methylation. {ECO:0000255|HAMAP-Rule:MF_00074, ECO:0000269|PubMed:17238915}. EcoCyc product frame: EG10376-MONOMER. EcoCyc synonyms: gidB. Genomic coordinates: 3923057-3923680. EcoCyc protein note: RsmG is the methyltransferase responsible for methylation of 16S rRNA at the N7 position of the G527 nucleotide. In vitro, the enzyme is able to methylate 16S rRNA within the 30S ribosomal subunit, but not naked 16S rRNA . RsmG is highly conserved in Gram-negative as well as Gram-positive bacteria . A crystal structure of RsmG has been solved at 2.4 Å resolution . Amino acids that are important for catalytic activity of RsmG were identified by site-directed mutagenesis of conserved residues . An rsmG mutation has no apparent growth defect and confers low-level resistance to streptomycin. rsmG mutations are found at high frequency in streptomycin-resistant clinical isolates of Mycobacterium tuberculosis . GidB: "glucose-inhibited division" RsmG: "rRNA small subunit methyltransferase G" Review:

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6U5|protein.P0A6U5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rsmG; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rsmG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012229,ECOCYC:EG10376,GeneID:948250`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3923057-3923680:-; feature_type=gene
