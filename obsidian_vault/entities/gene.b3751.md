---
entity_id: "gene.b3751"
entity_type: "gene"
name: "rbsB"
source_database: "NCBI RefSeq"
source_id: "gene-b3751"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3751"
  - "rbsB"
---

# rbsB

`gene.b3751`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3751`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsB (gene.b3751) is a gene entity. It encodes rbsB (protein.P02925). Encoded protein function: FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Binds ribose. Also serves as the primary chemoreceptor for chemotaxis. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:4608146, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:7982928}. EcoCyc product frame: RBSB-MONOMER. EcoCyc synonyms: prlB, rbsP. Genomic coordinates: 3936278-3937168. EcoCyc protein note: RbsB is the periplasmic ribose binding protein of an ATP-dependent ribose uptake system; ligand bound RbsB also interacts with the EG11018 "Trg" sensory protein to mediate taxis to ribose. The ribose binding protein is required for chemotaxis towards ribose; mutants lacking this protein do not demonstrate ribose mediated taxis . The RbsB molecule consists of two similar structured domains linked by a hinge region consisting of three short peptide stretches; bound β-D-ribopyranose is completely enclosed in a cleft between the domains . Non-liganded (open) structures of RbsB have also been obtained and conformational changes that the molecule undergoes during ligand binding and release are proposed . Regions/residues of RbsB involved in interaction with RbsC and with the chemosensory receptor have been identified RbsB has been used in the development of a TNT bioreporter...

## Biological Role

Repressed by dsrA (gene.b1954), rybB (gene.b4417), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02925|protein.P02925]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsB; function=-
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=rbsB; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012264,ECOCYC:EG10815,GeneID:948261`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3936278-3937168:+; feature_type=gene
