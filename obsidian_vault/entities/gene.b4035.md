---
entity_id: "gene.b4035"
entity_type: "gene"
name: "malK"
source_database: "NCBI RefSeq"
source_id: "gene-b4035"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4035"
  - "malK"
---

# malK

`gene.b4035`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4035`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malK (gene.b4035) is a gene entity. It encodes malK (protein.P68187). Encoded protein function: FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. EcoCyc product frame: MALK-MONOMER. EcoCyc synonyms: malB. Genomic coordinates: 4246784-4247899. EcoCyc protein note: MalK is the ATP-binding component of the maltose ABC transporter . Opening and closing of the MalK dimer which is associated with ATP binding and hydrolysis is thought to be a key event in the transport cycle. Crystal structures are available for MalK with bound ATP ; MalK without nucleotide (in both an open and semi-open conformation) and MalK with bound ADP . In computer simulations, the introduction of MgATP into the active site of MalK is associated with transition from semi-open to closed conformation and from open to semi-open conformation . Computer simulations also suggest that the closed form of MalK is stable when it contains two bound ATP molecules and that a single ATP hydrolysis will induce opening of the dimer...

## Biological Role

Activated by malT (protein.P06993), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68187|protein.P68187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malK; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013216,ECOCYC:EG10558,GeneID:948537`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4246784-4247899:+; feature_type=gene
