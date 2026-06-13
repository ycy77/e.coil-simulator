---
entity_id: "gene.b1474"
entity_type: "gene"
name: "fdnG"
source_database: "NCBI RefSeq"
source_id: "gene-b1474"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1474"
  - "fdnG"
---

# fdnG

`gene.b1474`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1474`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdnG (gene.b1474) is a gene entity. It encodes fdnG (protein.P24183). Encoded protein function: FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The alpha subunit FdnG contains the formate oxidation site. Electrons are transferred from formate to menaquinone in the gamma subunit (FdnI), through the 4Fe-4S clusters in the beta subunit (FdnH). Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. EcoCyc product frame: FDNG-MONOMER. Genomic coordinates: 1547401-1550448. EcoCyc protein note: fdnG encodes the α subunit of formate dehydrogenase N (Fdh-N). The α subunit is the site of formate oxidation; it contains a CPD-15873 (bis-MGD) cofactor, a selenocysteine residue and a (4Fe-4S) cluster (FS0). Electrons are transferred from formate to the molybdenum cofactor and then passed to the β subunit possibly via the FS0 cluster . FdnG is translocated to the periplasm via the Tat system; interaction with the FdnI subunit localizes the protein to the periplasmic face of the cytoplasmic membrane . Production of FdnG is regulated at the translational level...

## Biological Role

Repressed by fnr (protein.P0A9E5), narP (protein.P31802). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24183|protein.P24183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fdnG; function=-+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=fdnG; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fdnG; function=-+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=fdnG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004917,ECOCYC:EG11227,GeneID:946035`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1547401-1550448:+; feature_type=gene
