---
entity_id: "gene.b3305"
entity_type: "gene"
name: "rplF"
source_database: "NCBI RefSeq"
source_id: "gene-b3305"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3305"
  - "rplF"
---

# rplF

`gene.b3305`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3305`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplF (gene.b3305) is a gene entity. It encodes rplF (protein.P0AG55). Encoded protein function: FUNCTION: This protein binds directly to at least 2 domains of the 23S ribosomal RNA, thus is important in its secondary structure. It is located near the subunit interface in the base of the L7/L12 stalk, and near the tRNA binding site of the peptidyltransferase center. {ECO:0000269|PubMed:6170935}.; FUNCTION: Gentamicin-resistant mutations in this protein affect translation fidelity. {ECO:0000269|PubMed:369594}. EcoCyc product frame: EG10869-MONOMER. Genomic coordinates: 3445607-3446140. EcoCyc protein note: The L6 protein is a component of the 50S subunit of the ribosome and is involved in the late stage assembly of 50S ribosomal subunits. L6 interacts with 23S rRNA . Interaction appears to be cooperative with L3 . L6 crosslinks to the stem-loop structure in domain V of 23S rRNA , but assembles to domain VI . The L6 binding site within domain VI has been identified . L6 is altered in a gentamicin-resistant mutant . Ribosomes of gentamicin-resistant L6 mutants have altered misreading properties; the L6 alteration is thought to change a parameter of the ribosome function involved in codon recognition . L6 also participates in the binding of dibekacin to ribosomes...

## Biological Role

Repressed by rpsH (protein.P0A7W7), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG55|protein.P0AG55]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplF; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010827,ECOCYC:EG10869,GeneID:947803`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3445607-3446140:-; feature_type=gene
