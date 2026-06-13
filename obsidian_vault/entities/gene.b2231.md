---
entity_id: "gene.b2231"
entity_type: "gene"
name: "gyrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2231"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2231"
  - "gyrA"
---

# gyrA

`gene.b2231`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2231`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gyrA (gene.b2231) is a gene entity. It encodes gyrA (protein.P0AES4). Encoded protein function: FUNCTION: A type II topoisomerase that negatively supercoils closed circular double-stranded (ds) DNA in an ATP-dependent manner to maintain chromosomes in an underwound state (PubMed:12051842, PubMed:18642932, PubMed:186775, PubMed:19060136, PubMed:19965760, PubMed:20356737, PubMed:22457353, PubMed:23294697, PubMed:3031051, PubMed:7811004, PubMed:9148951). This makes better substrates for topoisomerase IV (ParC and ParE) which is the main enzyme that unlinks newly replicated chromosomes in E.coli (PubMed:9334322). Gyrase catalyzes the interconversion of other topological isomers of dsDNA rings, including catenanes (PubMed:22457352). Relaxes negatively supercoiled DNA in an ATP-independent manner (PubMed:337300). E.coli gyrase has higher supercoiling activity than many other bacterial gyrases; at comparable concentrations E.coli gyrase introduces more supercoils faster than M.tuberculosis gyrase, while M.tuberculosis gyrase has higher decatenation than supercoiling activity compared to E.coli (PubMed:22457352). E.coli makes 15% more negative supercoils in pBR322 plasmid DNA than S.typhimurium; the S.typhimurium GyrB subunit is toxic in E.coli, while the E.coli copy can be expressed in S.typhimurium even though the 2 subunits have 777/804 residues identical (PubMed:17400739)...

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AES4|protein.P0AES4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gyrA; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gyrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007370,ECOCYC:EG10423,GeneID:946614`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2336793-2339420:-; feature_type=gene
