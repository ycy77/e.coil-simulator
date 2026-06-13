---
entity_id: "gene.b3313"
entity_type: "gene"
name: "rplP"
source_database: "NCBI RefSeq"
source_id: "gene-b3313"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3313"
  - "rplP"
---

# rplP

`gene.b3313`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3313`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplP (gene.b3313) is a gene entity. It encodes rplP (protein.P0ADY7). Encoded protein function: FUNCTION: Binds directly to 23S ribosomal RNA and is located at the A site of the peptidyltransferase center. It contacts the A and P site tRNAs (PubMed:8524654). One of the last ribosomal proteins to be assembled in the 50S subunit (PubMed:33639093). The simultaneous presence of uL16 and bL36 probably triggers ObgE's GTPase activity and eventual dissociation from the mature 50S ribosomal subunit (PubMed:33639093). It has an essential role in subunit assembly (PubMed:3298242). {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:33639093, ECO:0000269|PubMed:8524654}. EcoCyc product frame: EG10877-MONOMER. Genomic coordinates: 3448759-3449169. EcoCyc protein note: The L16 protein is a late assembly component of the 50S subunit of the ribosome; ribosomes lacking L16 are translationally active . L2 is required for assembly of L16 into the 50S subunit . L16 interacts with tRNA and can be crosslinked to aminoacylated tRNA in the A and P site . Conserved residues within L16 were shown to be involved in the translocation of tRNA from the A to the P site . L16 is located within 21 Å of nucleotide C2475 of 23S rRNA, near the peptidyltransferase center . L16 and a histidine residue within the N-terminal domain of L16 may be important for the correct conformation of the peptidyltransferase center...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADY7|protein.P0ADY7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplP; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010846,ECOCYC:EG10877,GeneID:947806`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3448759-3449169:-; feature_type=gene
